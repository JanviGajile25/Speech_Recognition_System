import streamlit as st
from datetime import datetime
from speech_module import SpeechRecognizer, DomainAnalyzer

# Page configuration
st.set_page_config(
    page_title="Speech Recognition System",
    page_icon="🎤",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load CSS
def load_css():
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

try:
    load_css()
except:
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        * {
            font-family: 'Inter', sans-serif;
        }
        
        .main-header {
            font-size: 3rem;
            color: #1a1a1a;
            text-align: center;
            margin-bottom: 0.3rem;
            font-weight: 700;
            letter-spacing: -1px;
        }
        
        .subtitle {
            text-align: center;
            color: #6b7280;
            font-size: 1rem;
            margin-bottom: 3rem;
            font-weight: 400;
        }
        
        .section-header {
            font-size: 1.4rem;
            color: #1a1a1a;
            margin-top: 2.5rem;
            margin-bottom: 1.5rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .card {
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            margin-bottom: 1.5rem;
            border: 1px solid #e5e7eb;
        }
        
        .recognized-text {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 12px;
            border: 2px solid #3b82f6;
            margin: 1rem 0;
            min-height: 180px;
            font-size: 1.2rem;
            line-height: 1.8;
            color: #1a1a1a;
            font-weight: 500;
            box-shadow: 0 4px 6px rgba(59, 130, 246, 0.1);
        }
        
        .live-transcript {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 12px;
            min-height: 120px;
            font-size: 1.1rem;
            line-height: 1.6;
            font-weight: 500;
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
            margin: 1rem 0;
        }
        
        .info-box {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1.8rem;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            transition: transform 0.2s;
        }
        
        .info-box:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        }
        
        .info-box h3 {
            color: white !important;
            margin: 0;
            font-size: 2.5rem;
            font-weight: 700;
        }
        
        .info-box p {
            color: rgba(255,255,255,0.95) !important;
            margin: 0.5rem 0 0 0;
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            font-weight: 500;
        }
        
        .listening-indicator {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: white;
            padding: 1.2rem;
            border-radius: 12px;
            text-align: center;
            font-weight: 600;
            font-size: 1.1rem;
            animation: pulse 1.5s infinite;
            box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
            margin: 1rem 0;
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.9; transform: scale(1.02); }
        }
        
        .status-badge {
            display: inline-block;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 600;
            margin: 0.5rem 0;
        }
        
        .status-active {
            background: #dcfce7;
            color: #166534;
        }
        
        .status-inactive {
            background: #f3f4f6;
            color: #6b7280;
        }
        
        .divider {
            height: 2px;
            background: linear-gradient(90deg, transparent, #e5e7eb, transparent);
            margin: 2rem 0;
        }
        
        /* Hide Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stDeployButton {display:none;}
        
        /* Button improvements */
        .stButton button {
            border-radius: 8px;
            font-weight: 600;
            padding: 0.75rem 1.5rem;
            transition: all 0.2s;
            border: none;
            font-size: 1rem;
        }
        
        .stButton button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'recognized_text' not in st.session_state:
    st.session_state.recognized_text = ""
if 'live_transcript' not in st.session_state:
    st.session_state.live_transcript = ""
if 'is_recording' not in st.session_state:
    st.session_state.is_recording = False
if 'show_listening' not in st.session_state:
    st.session_state.show_listening = False

# Initialize modules
speech_recognizer = SpeechRecognizer()
domain_analyzer = DomainAnalyzer()

# Header
st.markdown('<h1 class="main-header">🎤 Speech Recognition System</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Real-time speech-to-text conversion • Hindi • Marathi • English</p>', unsafe_allow_html=True)

# Language selection in a card
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="section-header">🌐 Language Settings</div>', unsafe_allow_html=True)

language_options = {
    "English (India)": "en-IN",
    "हिंदी (Hindi)": "hi-IN",
    "मराठी (Marathi)": "mr-IN"
}

col_lang, col_status = st.columns([2, 1])
with col_lang:
    selected_language = st.selectbox(
        "Select recognition language:",
        list(language_options.keys()),
        label_visibility="collapsed"
    )
    language_code = language_options[selected_language]

with col_status:
    if st.session_state.show_listening:
        st.markdown('<div class="status-badge status-active">🔴 Recording</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-badge status-inactive">⚫ Ready</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Live Speech Recognition Section
st.markdown('<div class="section-header">🎙️ Live Speech Recognition</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    if st.button("▶️ Start Recording", use_container_width=True, type="primary"):
        st.session_state.show_listening = True
        st.rerun()

with col2:
    if st.button("⏹️ Stop", use_container_width=True):
        st.session_state.is_recording = False
        st.session_state.show_listening = False
        st.session_state.live_transcript = ""
        st.success("Recording stopped!")

with col3:
    if st.button("🔄 Clear All", use_container_width=True):
        st.session_state.recognized_text = ""
        st.session_state.live_transcript = ""
        st.session_state.show_listening = False
        st.success("Cleared!")

# Show listening indicator and perform recognition
if st.session_state.show_listening:
    st.markdown('<div class="listening-indicator">🎤 Listening... Speak now!</div>', unsafe_allow_html=True)
    
    result = speech_recognizer.recognize_from_microphone(language_code)
    
    if result["status"] == "success":
        st.session_state.live_transcript = result["text"]
        st.session_state.recognized_text += result["text"] + " "
        st.session_state.show_listening = False
        st.rerun()
    else:
        st.error(f"❌ {result['text']}")
        st.session_state.show_listening = False

# Live Transcript Box - Shows current recording
if st.session_state.live_transcript:
    st.markdown("**Current Recording:**")
    st.markdown(
        f'<div class="live-transcript">{st.session_state.live_transcript}</div>',
        unsafe_allow_html=True
    )

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# File Upload Section
st.markdown('<div class="section-header">📁 Upload Audio File</div>', unsafe_allow_html=True)

col_upload, col_process = st.columns([3, 1])

with col_upload:
    uploaded_file = st.file_uploader(
        "Drag and drop or browse (.wav, .flac)",
        type=['wav', 'flac'],
        help="Upload a WAV or FLAC audio file for speech recognition",
        label_visibility="collapsed"
    )

if uploaded_file is not None:
    with col_upload:
        st.audio(uploaded_file, format='audio/wav')
    
    with col_process:
        if st.button("🔄 Process", use_container_width=True, type="primary"):
            with st.spinner("Processing..."):
                result = speech_recognizer.recognize_from_file(uploaded_file, language_code)
                
                if result["status"] == "success":
                    st.session_state.recognized_text += result["text"] + " "
                    st.success("✅ Done!")
                    st.rerun()
                else:
                    st.error(f"❌ {result['text']}")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Complete Transcript Section
st.markdown('<div class="section-header">📝 Complete Transcript</div>', unsafe_allow_html=True)

if st.session_state.recognized_text:
    st.markdown(
        f'<div class="recognized-text">{st.session_state.recognized_text}</div>',
        unsafe_allow_html=True
    )
    
    # Download button
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"transcript_{timestamp}.txt"
    
    col_download, col_space = st.columns([2, 2])
    with col_download:
        st.download_button(
            label="📥 Download Transcript",
            data=st.session_state.recognized_text,
            file_name=filename,
            mime="text/plain",
            use_container_width=True,
            type="primary"
        )
else:
    st.markdown(
        '<div class="recognized-text" style="color: #9ca3af; font-style: italic; border: 2px dashed #d1d5db;">No transcript yet. Start recording or upload an audio file to begin.</div>',
        unsafe_allow_html=True
    )

# Analysis Section - Only show when there is text
if st.session_state.recognized_text:
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-header">📊 Speech Analysis</div>', unsafe_allow_html=True)
    
    domain = domain_analyzer.analyze_domain(st.session_state.recognized_text)
    stats = domain_analyzer.get_statistics(st.session_state.recognized_text)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="info-box">
            <h3>{domain}</h3>
            <p>Domain</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="info-box">
            <h3>{stats['words']}</h3>
            <p>Words</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="info-box">
            <h3>{stats['characters']}</h3>
            <p>Characters</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="info-box">
            <h3>{stats['sentences']}</h3>
            <p>Sentences</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown(
    '<p style="text-align: center; color: #9ca3af; font-size: 0.9rem; padding: 2rem 0;">Made with ❤️ using Streamlit</p>',
    unsafe_allow_html=True
)