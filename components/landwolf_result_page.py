"""
Landwolf Result Page Component for ALF Abstractor
Where the summoned ALF and Landwolf the Hairy Wolf crypto pack adventure images are revealed and shared
"""

import streamlit as st
import time
from components.styles import load_alf_css, create_title, create_quote
from services.image_generator import ALFImageGenerator
from utils.helpers import create_share_text
from utils.session_manager import SessionManager
from config import UI_TEXT

# Landwolf-specific completion quotes (crypto pack themes)
LANDWOLF_QUOTES = [
    "ALF and Landwolf's pack howl echoes through the blockchain forever.",
    "In the crypto wilderness, their hairy wolf wisdom creates legendary gains.",
    "Two friends, one pack vision, unlimited moon-bound adventures.",
    "Where wild forest meets blockchain technology, legends are born.",
    "Their pack adventures prowl through digital realms eternally.",
    "Green scales and hairy wolf fur, the ultimate crypto pack duo.",
    "Every howl with Landwolf makes ALF's portfolio more legendary.",
    "Together they create the most diamond-pawed pack adventures.",
    "In friendship, even bear markets become bull market pack hunts.",
    "The blockchain celebrates ALF and Landwolf's wild crypto magic."
]

def render_landwolf_result_page():
    """Render the result page showing the generated ALF and Landwolf image"""
    load_alf_css()
    
    st.markdown(
        create_title("🎭 A Legendary Pack Adventure Has Emerged...", "page-header"), 
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
                prompt_display = f"Legendary pack adventure created with: {current_prompt}"
                st.markdown(create_quote(prompt_display), unsafe_allow_html=True)
            
            # Add a Landwolf-specific completion quote
            import random
            completion_quote = random.choice(LANDWOLF_QUOTES)
            st.markdown(create_quote(completion_quote), unsafe_allow_html=True)
            
            # Action buttons
            _render_landwolf_action_buttons(image, current_prompt)
            
        else:
            # No image found
            st.error("No legendary pack adventure found in the digital realm...")
            if st.button("🔙 Return to Friends"):
                SessionManager.navigate_to_friends()
                st.rerun()

def _render_landwolf_action_buttons(image, prompt: str):
    """
    Render the action buttons for the Landwolf result page
    
    Args:
        image: The generated PIL image
        prompt (str): The prompt used for generation
    """
    col_a, col_b, col_c, col_d = st.columns(4)
    
    with col_a:
        # Download button
        if image:
            image_bytes = ALFImageGenerator.image_to_bytes(image)
            filename = f"alf_landwolf_adventure_{int(time.time())}.png"
            
            st.download_button(
                label="📥 Download Adventure",
                data=image_bytes,
                file_name=filename,
                mime="image/png"
            )
    
    with col_b:
        # Make another button
        if st.button("🔄 New Adventure"):
            SessionManager.navigate_to_landwolf_prompt()
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
            _show_landwolf_share_options(prompt)

def _show_landwolf_share_options(prompt: str):
    """
    Show sharing options for the generated ALF and Landwolf adventure
    
    Args:
        prompt (str): The prompt used for generation
    """
    st.info("Copy this page URL to share your ALF & Landwolf legendary pack adventure!")
    
    # Create shareable text for Landwolf adventures
    share_text = f"🐊🐺 Just created a legendary ALF & Landwolf crypto pack adventure!\n\nPrompt: {prompt}\n\n#ALFandLandwolf #PackHunting #CryptoWolf #AIArt #WildCrypto"
    
    # Show the share text in an expandable section
    with st.expander("📋 Copy Share Text"):
        st.code(share_text)
        st.caption("Share your ALF & Landwolf legendary pack adventure on social media!")

def render_landwolf_image_history():
    """Render a sidebar or expander showing recent Landwolf adventures (optional feature)"""
    history = SessionManager.get_history()
    
    # Filter for Landwolf-related adventures (those containing "Landwolf" in the prompt)
    landwolf_history = [item for item in history if "landwolf" in item['prompt'].lower()]
    
    if landwolf_history:
        with st.expander(f"🐺 Recent Landwolf Adventures ({len(landwolf_history)})"):
            for i, item in enumerate(reversed(landwolf_history[-5:])):  # Show last 5
                st.markdown(f"**{i+1}.** {item['prompt'][:50]}...")
                if 'timestamp' in item:
                    timestamp = time.strftime('%H:%M:%S', time.localtime(item['timestamp']))
                    st.caption(f"Adventure at: {timestamp}")
                st.markdown("---")