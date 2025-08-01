"""
Polly Result Page Component for ALF Abstractor
Where the summoned ALF and Polly adventure images are revealed and shared
"""

import streamlit as st
import time
from components.styles import load_alf_css, create_title, create_quote
from services.image_generator import ALFImageGenerator
from utils.helpers import create_share_text
from utils.session_manager import SessionManager
from config import UI_TEXT

# Polly-specific completion quotes
POLLY_QUOTES = [
    "ALF and Polly's friendship transcends the digital realm.",
    "In the ice crystals, their adventure is eternal.",
    "Two friends, one magical moment, infinite possibilities.",
    "Where crocodile meets penguin, magic happens.",
    "Their laughter echoes through the digital arctic.",
    "Pink and green, ice and swamp, perfect harmony.",
    "Every adventure with Polly makes ALF's heart warmer.",
    "Together they build bridges between worlds.",
    "In friendship, even opposites create beauty.",
    "The digital aurora dances for ALF and Polly."
]

def render_polly_result_page():
    """Render the result page showing the generated ALF and Polly image"""
    load_alf_css()
    
    st.markdown(
        create_title("🎭 An Adventure Has Emerged...", "page-header"), 
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
                prompt_display = f"Adventure created with: {current_prompt}"
                st.markdown(create_quote(prompt_display), unsafe_allow_html=True)
            
            # Add a Polly-specific completion quote
            import random
            completion_quote = random.choice(POLLY_QUOTES)
            st.markdown(create_quote(completion_quote), unsafe_allow_html=True)
            
            # Action buttons
            _render_polly_action_buttons(image, current_prompt)
            
        else:
            # No image found
            st.error("No adventure found in the digital realm...")
            if st.button("🔙 Return to Friends"):
                SessionManager.navigate_to_friends()
                st.rerun()

def _render_polly_action_buttons(image, prompt: str):
    """
    Render the action buttons for the Polly result page
    
    Args:
        image: The generated PIL image
        prompt (str): The prompt used for generation
    """
    col_a, col_b, col_c, col_d = st.columns(4)
    
    with col_a:
        # Download button
        if image:
            image_bytes = ALFImageGenerator.image_to_bytes(image)
            filename = f"alf_polly_adventure_{int(time.time())}.png"
            
            st.download_button(
                label="📥 Download Adventure",
                data=image_bytes,
                file_name=filename,
                mime="image/png"
            )
    
    with col_b:
        # Make another button
        if st.button("🔄 New Adventure"):
            SessionManager.navigate_to_polly_prompt()
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
            _show_polly_share_options(prompt)

def _show_polly_share_options(prompt: str):
    """
    Show sharing options for the generated ALF and Polly adventure
    
    Args:
        prompt (str): The prompt used for generation
    """
    st.info("Copy this page URL to share your ALF & Polly adventure!")
    
    # Create shareable text for Polly adventures
    share_text = f"🐊🐧 Just created an amazing ALF & Polly adventure!\n\nPrompt: {prompt}\n\n#ALFandPolly #DigitalAdventures #AIArt"
    
    # Show the share text in an expandable section
    with st.expander("📋 Copy Share Text"):
        st.code(share_text)
        st.caption("Share your ALF & Polly adventure on social media!")

def render_polly_image_history():
    """Render a sidebar or expander showing recent Polly adventures (optional feature)"""
    history = SessionManager.get_history()
    
    # Filter for Polly-related adventures (those containing "Polly" in the prompt)
    polly_history = [item for item in history if "polly" in item['prompt'].lower()]
    
    if polly_history:
        with st.expander(f"🐧 Recent Polly Adventures ({len(polly_history)})"):
            for i, item in enumerate(reversed(polly_history[-5:])):  # Show last 5
                st.markdown(f"**{i+1}.** {item['prompt'][:50]}...")
                if 'timestamp' in item:
                    timestamp = time.strftime('%H:%M:%S', time.localtime(item['timestamp']))
                    st.caption(f"Adventure at: {timestamp}")
                st.markdown("---")