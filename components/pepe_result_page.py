"""
Pepe Result Page Component for ALF Abstractor
Where the summoned ALF and Pepe the Green Frog crypto meme adventure images are revealed and shared
"""

import streamlit as st
import time
from components.styles import load_alf_css, create_title, create_quote
from services.image_generator import ALFImageGenerator
from utils.helpers import create_share_text
from utils.session_manager import SessionManager
from config import UI_TEXT

# Pepe-specific completion quotes (crypto meme themes)
PEPE_QUOTES = [
    "ALF and Pepe's legendary memes echo through the blockchain forever.",
    "In the crypto dimensions, their diamond hands create infinite gains.",
    "Two friends, one memetic vision, unlimited moon potential.",
    "Where technology meets rare Pepe energy, legends are born.",
    "Their crypto adventures pump through digital realms eternally.",
    "Green scales and green frog skin, the ultimate hodling duo.",
    "Every meme with Pepe makes ALF's portfolio more legendary.",
    "Together they create the most diamond-handed adventures.",
    "In friendship, even bear markets become bull runs.",
    "The blockchain celebrates ALF and Pepe's iconic meme magic."
]

def render_pepe_result_page():
    """Render the result page showing the generated ALF and Pepe image"""
    load_alf_css()
    
    st.markdown(
        create_title("🎭 A Legendary Meme Adventure Has Emerged...", "page-header"), 
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
                prompt_display = f"Legendary meme adventure created with: {current_prompt}"
                st.markdown(create_quote(prompt_display), unsafe_allow_html=True)
            
            # Add a Pepe-specific completion quote
            import random
            completion_quote = random.choice(PEPE_QUOTES)
            st.markdown(create_quote(completion_quote), unsafe_allow_html=True)
            
            # Action buttons
            _render_pepe_action_buttons(image, current_prompt)
            
        else:
            # No image found
            st.error("No legendary meme adventure found in the digital realm...")
            if st.button("🔙 Return to Friends"):
                SessionManager.navigate_to_friends()
                st.rerun()

def _render_pepe_action_buttons(image, prompt: str):
    """
    Render the action buttons for the Pepe result page
    
    Args:
        image: The generated PIL image
        prompt (str): The prompt used for generation
    """
    col_a, col_b, col_c, col_d = st.columns(4)
    
    with col_a:
        # Download button
        if image:
            image_bytes = ALFImageGenerator.image_to_bytes(image)
            filename = f"alf_pepe_adventure_{int(time.time())}.png"
            
            st.download_button(
                label="📥 Download Adventure",
                data=image_bytes,
                file_name=filename,
                mime="image/png"
            )
    
    with col_b:
        # Make another button
        if st.button("🔄 New Adventure"):
            SessionManager.navigate_to_pepe_prompt()
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
            _show_pepe_share_options(prompt)

def _show_pepe_share_options(prompt: str):
    """
    Show sharing options for the generated ALF and Pepe adventure
    
    Args:
        prompt (str): The prompt used for generation
    """
    st.info("Copy this page URL to share your ALF & Pepe legendary meme adventure!")
    
    # Create shareable text for Pepe adventures
    share_text = f"🐊🐸 Just created a legendary ALF & Pepe crypto meme adventure!\n\nPrompt: {prompt}\n\n#ALFandPepe #RarePepe #CryptoMemes #AIArt #ToTheMoon"
    
    # Show the share text in an expandable section
    with st.expander("📋 Copy Share Text"):
        st.code(share_text)
        st.caption("Share your ALF & Pepe legendary meme adventure on social media!")

def render_pepe_image_history():
    """Render a sidebar or expander showing recent Pepe adventures (optional feature)"""
    history = SessionManager.get_history()
    
    # Filter for Pepe-related adventures (those containing "Pepe" in the prompt)
    pepe_history = [item for item in history if "pepe" in item['prompt'].lower()]
    
    if pepe_history:
        with st.expander(f"🐸 Recent Pepe Adventures ({len(pepe_history)})"):
            for i, item in enumerate(reversed(pepe_history[-5:])):  # Show last 5
                st.markdown(f"**{i+1}.** {item['prompt'][:50]}...")
                if 'timestamp' in item:
                    timestamp = time.strftime('%H:%M:%S', time.localtime(item['timestamp']))
                    st.caption(f"Adventure at: {timestamp}")
                st.markdown("---")