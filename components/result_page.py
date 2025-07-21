"""
Result Page Component for ALF Abstractor
Where the summoned ALF images are revealed and shared
"""

import streamlit as st
import time
from components.styles import load_alf_css, create_title, create_quote
from services.image_generator import ALFImageGenerator
from utils.helpers import create_share_text, get_random_alf_quote
from utils.session_manager import SessionManager
from config import UI_TEXT

def render_result_page():
    """Render the result page showing the generated ALF image"""
    load_alf_css()
    
    st.markdown(
        create_title(UI_TEXT["RESULT"]["title"], "page-header"), 
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
                prompt_display = f"Summoned with: {current_prompt}"
                st.markdown(create_quote(prompt_display), unsafe_allow_html=True)
            
            # Add a mystical completion quote
            completion_quote = get_random_alf_quote()
            st.markdown(create_quote(completion_quote), unsafe_allow_html=True)
            
            # Action buttons
            _render_action_buttons(image, current_prompt)
            
        else:
            # No image found
            st.error(UI_TEXT["RESULT"]["no_image_error"])
            if st.button(UI_TEXT["RESULT"]["return_button"]):
                SessionManager.reset_to_landing()
                st.rerun()

def _render_action_buttons(image, prompt: str):
    """
    Render the action buttons for the result page
    
    Args:
        image: The generated PIL image
        prompt (str): The prompt used for generation
    """
    col_a, col_b, col_c, col_d = st.columns(4)
    
    with col_a:
        # Download button
        if image:
            image_bytes = ALFImageGenerator.image_to_bytes(image)
            filename = ALFImageGenerator.generate_filename(prompt)
            
            st.download_button(
                label=UI_TEXT["RESULT"]["download_button"],
                data=image_bytes,
                file_name=filename,
                mime="image/png"
            )
    
    with col_b:
        # Make another button
        if st.button(UI_TEXT["RESULT"]["make_another_button"]):
            SessionManager.navigate_to_prompt()
            SessionManager.set_current_prompt("")  # Clear previous prompt
            st.rerun()
    
    with col_c:
        # New session button
        if st.button(UI_TEXT["RESULT"]["new_session_button"]):
            SessionManager.reset_to_landing()
            st.rerun()
    
    with col_d:
        # Share button
        if st.button(UI_TEXT["RESULT"]["share_button"]):
            _show_share_options(prompt)

def _show_share_options(prompt: str):
    """
    Show sharing options for the generated ALF
    
    Args:
        prompt (str): The prompt used for generation
    """
    st.info(UI_TEXT["RESULT"]["share_message"])
    
    # Create shareable text
    share_text = create_share_text(prompt)
    
    # Show the share text in an expandable section
    with st.expander("📋 Copy Share Text"):
        st.code(share_text)
        st.caption("Copy this text to share your ALF creation on social media!")

def render_image_history():
    """Render a sidebar or expander showing recent generations (optional feature)"""
    history = SessionManager.get_history()
    
    if history:
        with st.expander(f"🌌 Recent ALF Manifestations ({len(history)})"):
            for i, item in enumerate(reversed(history[-5:])):  # Show last 5
                st.markdown(f"**{i+1}.** {item['prompt'][:50]}...")
                if 'timestamp' in item:
                    timestamp = time.strftime('%H:%M:%S', time.localtime(item['timestamp']))
                    st.caption(f"Summoned at: {timestamp}")
                st.markdown("---")