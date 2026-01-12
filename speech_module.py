import speech_recognition as sr
import os
import tempfile

class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
    
    def recognize_from_microphone(self, language_code="en-IN"):
        """
        Recognize speech from microphone
        """
        with sr.Microphone() as source:
            try:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=15)
                text = self.recognizer.recognize_google(audio, language=language_code)
                return {"status": "success", "text": text}
            except sr.WaitTimeoutError:
                return {"status": "error", "text": "No speech detected. Please try again."}
            except sr.UnknownValueError:
                return {"status": "error", "text": "Could not understand audio. Please speak clearly."}
            except sr.RequestError as e:
                return {"status": "error", "text": f"Could not request results: {e}"}
            except Exception as e:
                return {"status": "error", "text": f"An error occurred: {str(e)}"}
    
    def recognize_from_file(self, audio_file, language_code="en-IN"):
        """
        Recognize speech from uploaded audio file
        """
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(audio_file.name)[1]) as tmp_file:
            tmp_file.write(audio_file.getvalue())
            tmp_file_path = tmp_file.name
        
        try:
            with sr.AudioFile(tmp_file_path) as source:
                audio = self.recognizer.record(source)
                text = self.recognizer.recognize_google(audio, language=language_code)
                os.unlink(tmp_file_path)
                return {"status": "success", "text": text}
        except sr.UnknownValueError:
            os.unlink(tmp_file_path)
            return {"status": "error", "text": "Could not understand audio in file."}
        except sr.RequestError as e:
            os.unlink(tmp_file_path)
            return {"status": "error", "text": f"Could not request results: {e}"}
        except Exception as e:
            if os.path.exists(tmp_file_path):
                os.unlink(tmp_file_path)
            return {"status": "error", "text": f"Error processing file: {str(e)}"}


class DomainAnalyzer:
    def __init__(self):
        self.domains = {
            "Medical": ["doctor", "patient", "medicine", "hospital", "treatment", "disease", 
                       "health", "diagnosis", "surgery", "clinic", "prescription"],
            "Education": ["student", "teacher", "school", "college", "university", "exam", 
                         "study", "class", "education", "learn", "homework", "assignment"],
            "Business": ["company", "business", "market", "sales", "profit", "customer", 
                        "product", "investment", "meeting", "revenue", "management"],
            "Technology": ["software", "computer", "technology", "app", "system", "code", 
                          "programming", "data", "internet", "website", "digital"],
            "Sports": ["game", "player", "team", "match", "score", "cricket", "football", 
                      "win", "tournament", "championship", "athlete"],
            "Entertainment": ["movie", "music", "film", "actor", "song", "show", 
                            "entertainment", "dance", "concert", "drama"],
            "Politics": ["government", "minister", "election", "vote", "parliament", 
                        "policy", "political", "party", "democracy"],
            "Finance": ["money", "bank", "loan", "credit", "payment", "account", 
                       "transaction", "budget", "savings", "investment"],
            "Food": ["food", "restaurant", "cooking", "recipe", "eat", "dish", 
                    "meal", "dinner", "lunch", "breakfast"],
        }
    
    def analyze_domain(self, text):
        """
        Analyze the domain of the given text
        """
        if not text or len(text.strip()) == 0:
            return "No text to analyze"
        
        text_lower = text.lower()
        domain_scores = {}
        
        for domain, keywords in self.domains.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            domain_scores[domain] = score
        
        max_score = max(domain_scores.values())
        
        if max_score == 0:
            return "General Conversation"
        
        detected_domain = max(domain_scores, key=domain_scores.get)
        return detected_domain
    
    def get_statistics(self, text):
        """
        Get text statistics
        """
        if not text or len(text.strip()) == 0:
            return {"words": 0, "characters": 0, "sentences": 0}
        
        words = len(text.split())
        characters = len(text)
        sentences = text.count('.') + text.count('!') + text.count('?')
        
        return {
            "words": words,
            "characters": characters,
            "sentences": max(1, sentences)
        }