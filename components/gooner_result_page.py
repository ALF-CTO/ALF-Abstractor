"""
GOONER Result Page Component for ALF Abstractor
Where the summoned ALF and GOONER the Blue Penguin adventure images are revealed and shared
"""

import streamlit as st
import time
from components.styles import load_alf_css, create_title, create_quote
from services.image_generator import ALFImageGenerator
from utils.helpers import create_share_text
from utils.session_manager import SessionManager
from config import UI_TEXT

# GOONER-specific completion quotes
GOONER_QUOTES = [
    "ALF and GOONER's friendship flows like the deepest blue ocean.",
    "In the azure waves, their adventure becomes eternal.",
    "Two friends, one blue vision, infinite possibilities.",
    "Where technology meets the bluest penguin, magic flows.",
    "Their blue laughter ripples through digital waters.",
    "Green scales and blue feathers, perfect harmony.",
    "Every blue adventure with GOONER makes ALF's world brighter.",
    "Together they paint the sky in shades of friendship.",
    "In collaboration, even different colors create beauty.",
    "The digital ocean celebrates ALF and GOONER's blue bond."
]

def render_gooner_result_page():
    """Render the result page showing the generated ALF and GOONER image"""
    load_alf_css()
    
    st.markdown(
        create_title("🎭 A Blue Adventure Has Emerged...", "page-header"), 
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
                prompt_display = f"Blue adventure created with: {current_prompt}"
                st.markdown(create_quote(prompt_display), unsafe_allow_html=True)
            
            # Add a GOONER-specific completion quote
            import random
            completion_quote = random.choice(GOONER_QUOTES)
            st.markdown(create_quote(completion_quote), unsafe_allow_html=True)
            
            # Action buttons
            _render_gooner_action_buttons(image, current_prompt)
            
        else:
            # No image found
            st.error("No blue adventure found in the digital realm...")
            if st.button("🔙 Return to Friends"):
                SessionManager.navigate_to_friends()
                st.rerun()

def _render_gooner_action_buttons(image, prompt: str):
    """
    Render the action buttons for the GOONER result page
    
    Args:
        image: The generated PIL image
        prompt (str): The prompt used for generation
    """
    col_a, col_b, col_c, col_d = st.columns(4)
    
    with col_a:
        # Download button
        if image:
            image_bytes = ALFImageGenerator.image_to_bytes(image)
            filename = f"alf_gooner_adventure_{int(time.time())}.png"
            
            st.download_button(
                label="📥 Download Adventure",
                data=image_bytes,
                file_name=filename,
                mime="image/png"
            )
    
    with col_b:
        # Make another button
        if st.button("🔄 New Adventure"):
            SessionManager.navigate_to_gooner_prompt()
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
            _show_gooner_share_options(prompt)

def _show_gooner_share_options(prompt: str):
    """
    Show sharing options for the generated ALF and GOONER adventure
    
    Args:
        prompt (str): The prompt used for generation
    """
    st.info("Copy this page URL to share your ALF & GOONER blue adventure!")
    
    # Create shareable text for GOONER adventures
    share_text = f"🐊🐧 Just created an amazing ALF & GOONER blue adventure!\n\nPrompt: {prompt}\n\n#ALFandGOONER #BlueAdventures #AIArt #BluePenguin"
    
    # Show the share text in an expandable section
    with st.expander("📋 Copy Share Text"):
        st.code(share_text)
        st.caption("Share your ALF & GOONER blue adventure on social media!")

def render_gooner_image_history():
    """Render a sidebar or expander showing recent GOONER adventures (optional feature)"""
    history = SessionManager.get_history()
    
    # Filter for GOONER-related adventures (those containing "GOONER" in the prompt)
    gooner_history = [item for item in history if "gooner" in item['prompt'].lower()]
    
    if gooner_history:
        with st.expander(f"🐧 Recent GOONER Adventures ({len(gooner_history)})"):
            for i, item in enumerate(reversed(gooner_history[-5:])):  # Show last 5
                st.markdown(f"**{i+1}.** {item['prompt'][:50]}...")
                if 'timestamp' in item:
                    timestamp = time.strftime('%H:%M:%S', time.localtime(item['timestamp']))
                    st.caption(f"Adventure at: {timestamp}")
                st.markdown("---")