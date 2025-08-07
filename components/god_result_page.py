"""
GOD Result Page Component for ALF Abstractor
Where the summoned ALF and GOD the Golden Dog dyslexic adventure images are revealed and shared
"""

import streamlit as st
import time
from components.styles import load_alf_css, create_title, create_quote
from services.image_generator import ALFImageGenerator
from utils.helpers import create_share_text
from utils.session_manager import SessionManager
from config import UI_TEXT

# GOD-specific completion quotes (dyslexic themes)
GOD_QUOTES = [
    "ALF and GOD's misspelled magic creates perfect harmony.",
    "In the golden dimensions, backwards words spell friendship.",
    "Two friends, one dyslexic vision, infinite golden joy.",
    "Where letters get mixed up, hearts never do.",
    "Their scrambled adventures create the most beautiful stories.",
    "Green scales and golden fur, perfectly confused together.",
    "Every mixed-up word with GOD makes ALF's world brighter.",
    "Together they prove that mistakes make the best adventures.",
    "In friendship, even backwards spelling reads perfectly.",
    "The digital cosmos celebrates ALF and GOD's golden chaos."
]

def render_god_result_page():
    """Render the result page showing the generated ALF and GOD image"""
    load_alf_css()
    
    st.markdown(
        create_title("🎭 A Golden Adventure Has Emerged...", "page-header"), 
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        image = SessionManager.get_generated_image()
        current_prompt = SessionManager.get_current_prompt()
        
        if image:
            # Display the generated image with mystical border
            st.image(image, use_column_width=True)
            
            # Display the prompt used with mystical quote styling
            if current_prompt:
                prompt_display = f"Golden adventure created with: {current_prompt}"
                st.markdown(create_quote(prompt_display), unsafe_allow_html=True)
            
            # Add a GOD-specific completion quote
            import random
            completion_quote = random.choice(GOD_QUOTES)
            st.markdown(create_quote(completion_quote), unsafe_allow_html=True)
            
            # Action buttons
            _render_god_action_buttons(image, current_prompt)
            
        else:
            # No image found
            st.error("No golden adventure found in the digital realm...")
            if st.button("🔙 Return to Friends"):
                SessionManager.navigate_to_friends()
                st.rerun()

def _render_god_action_buttons(image, prompt: str):
    """
    Render the action buttons for the GOD result page
    
    Args:
        image: The generated PIL image
        prompt (str): The prompt used for generation
    """
    col_a, col_b, col_c, col_d = st.columns(4)
    
    with col_a:
        # Download button
        if image:
            image_bytes = ALFImageGenerator.image_to_bytes(image)
            filename = f"alf_god_adventure_{int(time.time())}.png"
            
            st.download_button(
                label="📥 Download Adventure",
                data=image_bytes,
                file_name=filename,
                mime="image/png"
            )
    
    with col_b:
        # Make another button
        if st.button("🔄 New Adventure"):
            SessionManager.navigate_to_god_prompt()
            SessionManager.set_current_prompt("")  # Clear previous prompt
            st.rerun()
    
    with col_c:
        # Back to friends button
        if st.button("👫 Other Friends"):
            SessionManager.navigate_to_friends()
            st.rerun()
    
    with col_d:
        # Share button
        if st.button("🎭 Share Adventure"):
            _show_god_share_options(prompt)

def _show_god_share_options(prompt: str):
    """
    Show sharing options for the generated ALF and GOD adventure
    
    Args:
        prompt (str): The prompt used for generation
    """
    st.info("Copy this page URL to share your ALF & GOD golden adventure!")
    
    # Create shareable text for GOD adventures
    share_text = f"🐊🐕 Just created a golden ALF & GOD dyslexic adventure!\\n\\nPrompt: {prompt}\\n\\n#ALFandGOD #DyslexicDog #AIArt #GoldenAdventures"
    
    # Show the share text in an expandable section
    with st.expander("📋 Copy Share Text"):
        st.code(share_text)
        st.caption("Share your ALF & GOD golden adventure on social media!")

def render_god_image_history():
    """Render a sidebar or expander showing recent GOD adventures (optional feature)"""
    history = SessionManager.get_history()
    
    # Filter for GOD-related adventures (those containing "GOD" in the prompt)
    god_history = [item for item in history if "god" in item['prompt'].lower()]
    
    if god_history:
        with st.expander(f"🐕 Recent GOD Adventures ({len(god_history)})"):
            for i, item in enumerate(reversed(god_history[-5:])):  # Show last 5
                st.markdown(f"**{i+1}.** {item['prompt'][:50]}...")
                if 'timestamp' in item:
                    timestamp = time.strftime('%H:%M:%S', time.localtime(item['timestamp']))
                    st.caption(f"Adventure at: {timestamp}")
                st.markdown("---")