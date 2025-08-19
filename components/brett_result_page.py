"""
Brett Result Page Component for ALF Abstractor
Where the summoned ALF and Brett the Blue Guy crypto ocean adventure images are revealed and shared
"""

import streamlit as st
import time
from components.styles import load_alf_css, create_title, create_quote
from services.image_generator import ALFImageGenerator
from utils.helpers import create_share_text
from utils.session_manager import SessionManager
from config import UI_TEXT

# Brett-specific completion quotes (crypto ocean/strategic themes)
BRETT_QUOTES = [
    "ALF and Brett's ocean wisdom flows through the blockchain forever.",
    "In the crypto depths, their blue strategy creates legendary gains.",
    "Two friends, one strategic vision, unlimited wave-powered adventures.",
    "Where deep confidence meets blockchain technology, legends are born.",
    "Their ocean adventures flow through digital realms eternally.",
    "Green scales and electric blue spirit, the ultimate crypto strategic duo.",
    "Every strategic moment with Brett makes ALF's portfolio more analytical.",
    "Together they create the most confidently strategic adventures.",
    "In friendship, even bear markets become bull market ocean celebrations.",
    "The blockchain celebrates ALF and Brett's electric blue crypto magic."
]

def render_brett_result_page():
    """Render the result page showing the generated ALF and Brett image"""
    load_alf_css()
    
    st.markdown(
        create_title("🎭 A Strategic Ocean Adventure Has Emerged...", "page-header"), 
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
                prompt_display = f"Strategic ocean adventure created with: {current_prompt}"
                st.markdown(create_quote(prompt_display), unsafe_allow_html=True)
            
            # Add a Brett-specific completion quote
            import random
            completion_quote = random.choice(BRETT_QUOTES)
            st.markdown(create_quote(completion_quote), unsafe_allow_html=True)
            
            # Action buttons
            _render_brett_action_buttons(image, current_prompt)
            
        else:
            # No image found
            st.error("No strategic ocean adventure found in the digital realm...")
            if st.button("🔙 Return to Friends"):
                SessionManager.navigate_to_friends()
                st.rerun()

def _render_brett_action_buttons(image, prompt: str):
    """
    Render the action buttons for the Brett result page
    
    Args:
        image: The generated PIL image
        prompt (str): The prompt used for generation
    """
    col_a, col_b, col_c, col_d = st.columns(4)
    
    with col_a:
        # Download button
        if image:
            image_bytes = ALFImageGenerator.image_to_bytes(image)
            filename = f"alf_brett_adventure_{int(time.time())}.png"
            
            st.download_button(
                label="📥 Download Adventure",
                data=image_bytes,
                file_name=filename,
                mime="image/png"
            )
    
    with col_b:
        # Make another button
        if st.button("🔄 New Adventure"):
            SessionManager.navigate_to_brett_prompt()
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
            _show_brett_share_options(prompt)

def _show_brett_share_options(prompt: str):
    """
    Show sharing options for the generated ALF and Brett adventure
    
    Args:
        prompt (str): The prompt used for generation
    """
    st.info("Copy this page URL to share your ALF & Brett strategic ocean adventure!")
    
    # Create shareable text for Brett adventures
    share_text = f"🐊🔵 Just created a strategic ALF & Brett crypto ocean adventure!\n\nPrompt: {prompt}\n\n#ALFandBrett #OceanVibes #BlueCrypto #AIArt #StrategicCrypto"
    
    # Show the share text in an expandable section
    with st.expander("📋 Copy Share Text"):
        st.code(share_text)
        st.caption("Share your ALF & Brett strategic ocean adventure on social media!")

def render_brett_image_history():
    """Render a sidebar or expander showing recent Brett adventures (optional feature)"""
    history = SessionManager.get_history()
    
    # Filter for Brett-related adventures (those containing "Brett" in the prompt)
    brett_history = [item for item in history if "brett" in item['prompt'].lower()]
    
    if brett_history:
        with st.expander(f"🔵 Recent Brett Adventures ({len(brett_history)})"):
            for i, item in enumerate(reversed(brett_history[-5:])):  # Show last 5
                st.markdown(f"**{i+1}.** {item['prompt'][:50]}...")
                if 'timestamp' in item:
                    timestamp = time.strftime('%H:%M:%S', time.localtime(item['timestamp']))
                    st.caption(f"Adventure at: {timestamp}")
                st.markdown("---")