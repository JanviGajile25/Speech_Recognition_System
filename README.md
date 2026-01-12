# 🎤 Speech Recognition System - Setup Guide

## ✅ What This System Does

- **Live Speech Recognition** for Hindi, Marathi, and English
- **Start/Stop/Clear** buttons - YOU control when to stop recording
- **File Upload** - Transcribe .wav, .flac, .mp3 files
- **Download** - Save transcripts as .txt files
- **Domain Analysis** - Automatically detects speech topic
- **Simple UI** - Easy for beginners

---

## 📋 Installation Steps

### Step 1: Install Python
Download Python 3.8 or higher from [python.org](https://www.python.org/downloads/)

### Step 2: Install Required Packages

Open Command Prompt (Windows) or Terminal (Mac/Linux) and run:

```bash
pip install streamlit
pip install SpeechRecognition
pip install pyaudio
pip install pydub
```

**For Windows (if PyAudio fails):**
```bash
pip install pipwin
pipwin install pyaudio
```

**For Mac:**
```bash
brew install portaudio
pip install pyaudio
```

**For Linux:**
```bash
sudo apt-get install portaudio19-dev
pip install pyaudio
```

### Step 3: Save the Code

1. Create a new folder: `speech_recognition_app`
2. Save the main code as: `app.py`
3. Save the requirements as: `requirements.txt`

### Step 4: Run the Application

Open terminal in the folder and run:

```bash
streamlit run app.py
```

The app will open in your browser automatically!

---

## 🎯 How to Use

### For Live Recording:
1. **Select Language** - Choose Hindi, Marathi, or English
2. **Click START** - Begin speaking immediately
3. **Speak clearly** - Your words appear in the text box
4. **Click STOP** - When you finish (no auto-stop, you control it!)
5. **Click CLEAR** - To erase and start fresh

### For File Upload:
1. Click "Browse files"
2. Select .wav, .flac, or .mp3 file
3. Click "Transcribe File"
4. Text appears in the box

### To Download:
1. Click "Download [Language] Transcript"
2. File saves as `transcript_hindi_[timestamp].txt`

### Domain Analysis:
1. Click "Analyze Speech Domain"
2. See what topic your speech is about (Education, Technology, etc.)

---

## 🎨 Key Features You Asked For

✅ **Start Button** - Only shows "Recording..." when clicked, not entire speech
✅ **User Control** - No automatic timeout, YOU decide when to stop
✅ **Better Colors** - Cyan box for recording, light grey for text (clear contrast)
✅ **Separate Files** - Each language saves to its own transcript file
✅ **Simple Design** - No animations, beginner-friendly layout

---

## 🔧 Troubleshooting

### Microphone Not Working?
- Check browser permissions (allow microphone access)
- Try different browser (Chrome works best)
- Restart the app: Press Ctrl+C in terminal, then run `streamlit run app.py` again

### PyAudio Installation Error?
- Windows: Use `pipwin install pyaudio`
- Mac: Install portaudio first: `brew install portaudio`
- Linux: Install dev tools: `sudo apt-get install portaudio19-dev python3-dev`

### No Audio Recognized?
- Speak clearly and loudly
- Check microphone is working (test in other apps)
- Ensure internet connection (uses Google Speech API)

---

## 📁 File Structure

```
speech_recognition_app/
├── app.py              # Main application
├── requirements.txt    # Dependencies
└── README.md          # This file
```

---

## 🌟 Tips for Best Results

- **Speak Clearly** - Pronounce words properly
- **Reduce Background Noise** - Find quiet place
- **Good Microphone** - Use headset mic if possible
- **Internet Required** - For speech recognition API
- **One Language at a Time** - Don't mix languages in same recording

---

## 📝 What Changed From Your Request

### ✅ Fixed Issues:
1. **Start Button** - Now only shows "Recording..." message, not full transcript
2. **No Auto-Stop** - Recording continues until YOU click Stop
3. **Better Colors** - Cyan (#00ffff) for recording, light grey (#e8f4f8) for text
4. **User Control** - Complete manual control over start/stop

### ✅ Features Included:
- Separate transcripts for each language
- File upload with transcription (.wav, .flac, .mp3)
- Download as .txt with language name
- Simple domain analysis (Education, Technology, Business, Health, Entertainment)
- Clean, simple UI for beginners

---

## 🚀 Next Steps

1. Install all dependencies
2. Run the app: `streamlit run app.py`
3. Test with each language
4. Try uploading audio files
5. Download your transcripts

Need help? Check troubleshooting section above!

---

**Made with ❤️ for beginners - Simple, clean, and easy to use!**
