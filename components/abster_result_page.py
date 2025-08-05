"""
Abster Result Page Component for ALF Abstractor
Where the summoned ALF and Abster the Green Penguin of Abstract adventure images are revealed and shared
"""

import streamlit as st
import time
from components.styles import load_alf_css, create_title, create_quote
from services.image_generator import ALFImageGenerator
from utils.helpers import create_share_text
from utils.session_manager import SessionManager
from config import UI_TEXT

# Abster-specific completion quotes
ABSTER_QUOTES = [
    "ALF and Abster's creativity transcends dimensional boundaries.",
    "In the geometric patterns, their abstract vision becomes reality.",
    "Two minds, one artistic vision, infinite abstractions.",
    "Where technology meets abstraction, true art emerges.",
    "Their collaborative genius echoes through digital dimensions.",
    "Green scales and geometric thoughts, perfect harmony.",
    "Every abstract adventure with Abster expands ALF's perspective.",
    "Together they build bridges between logic and creativity.",
    "In collaboration, even opposites create masterpieces.",
    "The digital cosmos celebrates ALF and Abster's artistry."
]

def render_abster_result_page():
    """Render the result page showing the generated ALF and Abster image"""
    load_alf_css()
    
    st.markdown(
        create_title("🎭 An Abstract Adventure Has Emerged...", "page-header"), 
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
                prompt_display = f"Abstract adventure created with: {current_prompt}"
                st.markdown(create_quote(prompt_display), unsafe_allow_html=True)
            
            # Add an Abster-specific completion quote
            import random
            completion_quote = random.choice(ABSTER_QUOTES)
            st.markdown(create_quote(completion_quote), unsafe_allow_html=True)
            
            # Action buttons
            _render_abster_action_buttons(image, current_prompt)
            
        else:
            # No image found
            st.error("No abstract adventure found in the digital realm...")
            if st.button("🔙 Return to Friends"):
                SessionManager.navigate_to_friends()
                st.rerun()

def _render_abster_action_buttons(image, prompt: str):
    """
    Render the action buttons for the Abster result page
    
    Args:
        image: The generated PIL image
        prompt (str): The prompt used for generation
    """
    col_a, col_b, col_c, col_d = st.columns(4)
    
    with col_a:
        # Download button
        if image:
            image_bytes = ALFImageGenerator.image_to_bytes(image)
            filename = f"alf_abster_adventure_{int(time.time())}.png"
            
            st.download_button(
                label="📥 Download Adventure",
                data=image_bytes,
                file_name=filename,
                mime="image/png"
            )
    
    with col_b:
        # Make another button
        if st.button("🔄 New Adventure"):
            SessionManager.navigate_to_abster_prompt()
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
            _show_abster_share_options(prompt)

def _show_abster_share_options(prompt: str):
    """
    Show sharing options for the generated ALF and Abster adventure
    
    Args:
        prompt (str): The prompt used for generation
    """
    st.info("Copy this page URL to share your ALF & Abster abstract adventure!")
    
    # Create shareable text for Abster adventures
    share_text = f"🐊🐧 Just created an amazing ALF & Abster abstract adventure!\n\nPrompt: {prompt}\n\n#ALFandAbster #AbstractAdventures #AIArt #GeometricArt"
    
    # Show the share text in an expandable section
    with st.expander("📋 Copy Share Text"):
        st.code(share_text)
        st.caption("Share your ALF & Abster abstract adventure on social media!")

def render_abster_image_history():
    """Render a sidebar or expander showing recent Abster adventures (optional feature)"""
    history = SessionManager.get_history()
    
    # Filter for Abster-related adventures (those containing "Abster" in the prompt)
    abster_history = [item for item in history if "abster" in item['prompt'].lower()]
    
    if abster_history:
        with st.expander(f"🐧 Recent Abster Adventures ({len(abster_history)})"):
            for i, item in enumerate(reversed(abster_history[-5:])):  # Show last 5
                st.markdown(f"**{i+1}.** {item['prompt'][:50]}...")
                if 'timestamp' in item:
                    timestamp = time.strftime('%H:%M:%S', time.localtime(item['timestamp']))
                    st.caption(f"Adventure at: {timestamp}")
                st.markdown("---")