"""
GOD Prompt Page Component for ALF Abstractor
Where users create magical adventure prompts for ALF and GOD the Golden Dog
"""

import streamlit as st
import random
from components.styles import load_alf_css, create_title, create_subtitle, create_mystical_text
from utils.session_manager import SessionManager
from config import UI_TEXT

# GOD-specific prompt objects (dyslexic/golden themes)
GOD_PROMPT_OBJECTS = [
    "playing with backwards letters in a golden field",
    "spelling words in mixed-up but beautiful ways",
    "chasing dyslexic butterflies through golden gardens",
    "creating art with scrambled letter blocks",
    "reading upside-down books in a golden library",
    "writing poetry with letters floating in reverse",
    "solving word puzzles in golden dimensions",
    "teaching ALF about beautiful spelling mistakes",
    "dancing with backwards alphabet letters",
    "painting with golden, mixed-up words",
    "exploring a world where letters float freely",
    "creating dyslexic masterpieces together"
]

# GOD-specific emotions (dyslexic/confused but happy themes)
GOD_PROMPT_EMOTIONS = [
    "happily confused but determined",
    "joyfully mixing up words",
    "golden and slightly puzzled",
    "cheerfully dyslexic and proud",
    "warmly confused but loving",
    "playfully scrambling letters",
    "golden-hearted and mixed-up",
    "beautifully backwards thinking",
    "lovingly linguistic chaos",
    "bright and dyslexically creative",
    "golden and word-swirling",
    "charmingly letter-confused"
]

# GOD-specific settings (dyslexic/golden environments)
GOD_PROMPT_SETTINGS = [
    "in a golden library with backwards books",
    "among floating mixed-up letters",
    "in a dyslexic classroom of wonder", 
    "within a golden alphabet storm",
    "surrounded by scrambled word clouds",
    "in a spelling bee dimension",
    "among golden letter rain",
    "in a reversed-reading sanctuary",
    "within mixed-up message bubbles",
    "in a golden world of word art",
    "surrounded by beautiful spelling chaos",
    "in a dyslexic paradise realm"
]

def render_god_prompt_page():
    """Render the prompt creation page for ALF and GOD adventures"""
    load_alf_css()
    
    # Page header
    st.markdown(
        create_title(UI_TEXT["GOD"]["title"], "page-header"), 
        unsafe_allow_html=True
    )
    
    st.markdown(
        create_subtitle(UI_TEXT["GOD"]["subtitle"]), 
        unsafe_allow_html=True
    )
    
    # Create main layout
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        st.markdown(
            create_mystical_text(UI_TEXT["GOD"]["description"]), 
            unsafe_allow_html=True
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Prompt input area
        st.markdown("### 🐕 Describe Your Dyslexic Adventure:")
        
        prompt = st.text_area(
            "",
            placeholder="e.g., ALF and GOD reading backwards books while golden letters float around them...",
            height=120,
            key="god_prompt_input"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Action buttons
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            if st.button(UI_TEXT["GOD"]["random_button"], key="random_god_prompt"):
                random_prompt = _generate_random_god_prompt()
                st.session_state.god_prompt_input = random_prompt
                st.rerun()
        
        with col_b:
            if st.button(UI_TEXT["GOD"]["mix_button"], key="mix_god_prompt"):
                if prompt.strip():
                    mixed_prompt = _mix_god_prompt(prompt)
                    st.session_state.god_prompt_input = mixed_prompt
                    st.rerun()
                else:
                    st.warning("Enter a prompt first to mix it!")
        
        with col_c:
            if st.button(UI_TEXT["GOD"]["generate_button"], key="generate_god_adventure", type="primary"):
                if prompt.strip():
                    # Store the prompt and navigate to generation
                    SessionManager.set_current_prompt(prompt)
                    SessionManager.navigate_to_god_generating()
                    st.rerun()
                else:
                    st.warning("Please describe the dyslexic adventure first!")
        
        # Show some example prompts
        st.markdown("<br>", unsafe_allow_html=True)
        with st.expander("💡 Dyslexic Adventure Ideas"):
            st.markdown("""
            **Golden Letter Adventures:**
            - ALF and GOD playing word games with floating golden letters
            - Reading stories where all the words are beautifully mixed up
            - Creating art by arranging dyslexic poetry in golden frames
            
            **Spelling Bee Adventures:**
            - GOD teaching ALF that misspelled words can be beautiful
            - Exploring a world where backwards writing is the norm
            - Dancing with alphabet letters that float in golden spirals
            
            **Dyslexic Paradise:**
            - GOD showing ALF how mixed-up letters create magic
            - Playing in a golden field where words grow like flowers
            - Building castles out of scrambled letter blocks
            """)
        
        # Reference images info  
        _show_god_reference_info()
        
        # Navigation buttons
        st.markdown("<hr><br>", unsafe_allow_html=True)
        
        col_nav1, col_nav2 = st.columns(2)
        
        with col_nav1:
            if st.button(UI_TEXT["GOD"]["back_button"], key="back_to_friends"):
                SessionManager.navigate_to_friends()
                st.rerun()
        
        with col_nav2:
            # Empty for spacing
            pass

def _generate_random_god_prompt() -> str:
    """Generate a random GOD adventure prompt"""
    obj = random.choice(GOD_PROMPT_OBJECTS)
    emotion = random.choice(GOD_PROMPT_EMOTIONS) 
    setting = random.choice(GOD_PROMPT_SETTINGS)
    
    return f"ALF and GOD {obj}, feeling {emotion}, {setting}"

def _mix_god_prompt(original_prompt: str) -> str:
    """Mix the user's prompt with GOD-specific elements"""
    obj = random.choice(GOD_PROMPT_OBJECTS)
    emotion = random.choice(GOD_PROMPT_EMOTIONS)
    setting = random.choice(GOD_PROMPT_SETTINGS)
    
    # Mix original with new elements
    mixed = f"{original_prompt}, while also {obj}, feeling {emotion}, {setting}"
    
    return mixed

def _show_god_reference_info():
    """Show information about GOD reference images"""
    ref_info = SessionManager.get_god_reference_images_info()
    
    if ref_info.get("folder_exists"):
        if ref_info["image_count"] > 0:
            st.info(f"🐕 Using {ref_info['image_count']} GOD reference images for consistent character appearance")
        else:
            st.info("ℹ️ No GOD reference images found. Add images to 'references/god' folder for consistent character appearance.")
    else:
        st.info("ℹ️ GOD reference folder not found. The app will use default character descriptions.")