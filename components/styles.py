import streamlit as st

def load_alf_css():
    """Load the custom CSS for ALF Abstractor aesthetic"""
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
        color: #00ff88;
    }
    
    .main-title {
        text-align: center;
        font-family: 'Courier New', monospace;
        font-size: 4rem;
        color: #00ff88;
        text-shadow: 0 0 20px #00ff88;
        margin-bottom: 2rem;
        animation: pulse 2s infinite;
    }
    
    .subtitle {
        text-align: center;
        font-family: 'Courier New', monospace;
        font-size: 1.2rem;
        color: #66ff99;
        margin-bottom: 3rem;
        opacity: 0.8;
    }
    
    .alf-quote {
        text-align: center;
        font-style: italic;
        color: #44ff77;
        font-size: 1.1rem;
        margin: 2rem 0;
        padding: 1rem;
        border: 1px solid #00ff88;
        border-radius: 10px;
        background: rgba(0, 255, 136, 0.05);
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #00ff88, #44ff77);
        color: black;
        font-weight: bold;
        border: none;
        border-radius: 20px;
        padding: 0.5rem 2rem;
        font-size: 1.1rem;
        transition: all 0.3s;
        box-shadow: 0 0 15px rgba(0, 255, 136, 0.3);
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 25px rgba(0, 255, 136, 0.5);
    }
    
    .stTextInput > div > div > input {
        background: rgba(0, 0, 0, 0.8);
        color: #00ff88;
        border: 2px solid #00ff88;
        border-radius: 10px;
        font-family: 'Courier New', monospace;
    }
    
    .stTextArea > div > div > textarea {
        background: rgba(0, 0, 0, 0.8);
        color: #00ff88;
        border: 2px solid #00ff88;
        border-radius: 10px;
        font-family: 'Courier New', monospace;
    }
    
    .generated-image {
        border: 3px solid #00ff88;
        border-radius: 15px;
        box-shadow: 0 0 30px rgba(0, 255, 136, 0.3);
        margin: 2rem 0;
    }
    
    @keyframes pulse {
        0% { text-shadow: 0 0 20px #00ff88; }
        50% { text-shadow: 0 0 40px #00ff88, 0 0 60px #00ff88; }
        100% { text-shadow: 0 0 20px #00ff88; }
    }
    
    .page-header {
        text-align: center;
        font-family: 'Courier New', monospace;
        font-size: 2.5rem;
        color: #00ff88;
        margin-bottom: 2rem;
        text-shadow: 0 0 15px #00ff88;
    }
    
    .spinner-text {
        color: #00ff88;
        font-family: 'Courier New', monospace;
        text-align: center;
    }
    
    .error-message {
        background: rgba(255, 0, 0, 0.1);
        border: 1px solid #ff4444;
        color: #ff6666;
        padding: 1rem;
        border-radius: 10px;
        font-family: 'Courier New', monospace;
    }
    
    .success-message {
        background: rgba(0, 255, 136, 0.1);
        border: 1px solid #00ff88;
        color: #00ff88;
        padding: 1rem;
        border-radius: 10px;
        font-family: 'Courier New', monospace;
    }
    
    .mystical-text {
        text-align: center;
        color: #66ff99;
        font-size: 1.1rem;
        margin: 2rem 0;
        font-style: italic;
        opacity: 0.8;
    }
    </style>
    """, unsafe_allow_html=True)

def create_title(text: str, css_class: str = "main-title") -> str:
    """Create a styled title with ALF aesthetic"""
    return f'<h1 class="{css_class}">{text}</h1>'

def create_subtitle(text: str) -> str:
    """Create a styled subtitle"""
    return f'<p class="subtitle">{text}</p>'

def create_quote(text: str) -> str:
    """Create a styled ALF quote box"""
    return f'<div class="alf-quote">"{text}"</div>'

def create_mystical_text(text: str) -> str:
    """Create mystical styled text"""
    return f'<p class="mystical-text">{text}</p>'