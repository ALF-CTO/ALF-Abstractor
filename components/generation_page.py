"""
Generation Page Component for ALF Abstractor
Where the mystical image generation happens
"""

import streamlit as st
import time
from components.styles import load_alf_css, create_title
from services.image_generator import ALFImageGenerator, ImageGenerationError
from utils.helpers import get_random_loading_message, format_error_message
from utils.session_manager import SessionManager
from config import UI_TEXT

def render_generation_page():
    """Render the image generation page"""
    load_alf_css()
    
    st.markdown(
        create_title(UI_TEXT["GENERATING"]["title"], "page-header"), 
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # API key input - using widget key to manage state directly
        api_key = st.text_input(
            UI_TEXT["GENERATING"]["api_key_label"], 
            type="password", 
            key="api_key"
        )
        
        current_prompt = SessionManager.get_current_prompt()
        
        # Show current prompt
        if current_prompt:
            st.info(f"**Summoning prompt:** {current_prompt}")
        
        # Show reference images if available
        ref_images = SessionManager.get_reference_images()
        if ref_images:
            st.markdown("**🖼️ Using Reference Images:**")
            cols = st.columns(min(len(ref_images), 3))
            for i, img in enumerate(ref_images[-3:]):  # Show last 3
                with cols[i % 3]:
                    st.image(img, caption=f"Reference {i+1}", use_column_width=True)
        
        # Generation button
        if api_key and current_prompt:
            if st.button(UI_TEXT["GENERATING"]["generate_button"]):
                _generate_alf_image(api_key, current_prompt)
        
        # Navigation buttons
        col_nav1, col_nav2 = st.columns(2)
        
        with col_nav1:
            if st.button(UI_TEXT["GENERATING"]["back_button"]):
                SessionManager.navigate_to_prompt()
                st.rerun()
        
        with col_nav2:
            # Show result button if image exists
            if SessionManager.has_generated_image():
                if st.button("🎭 View Result"):
                    SessionManager.navigate_to_result()
                    st.rerun()

def _generate_alf_image(api_key: str, prompt: str):
    """
    Generate ALF image using the provided API key and prompt
    
    Args:
        api_key (str): OpenAI API key
        prompt (str): User prompt for generation
    """
    try:
        # Validate API key format
        if not ALFImageGenerator.validate_api_key(api_key):
            st.error("Invalid API key format. Please check your OpenAI API key.")
            return
        
        # Initialize the image generator
        generator = ALFImageGenerator(api_key)
        
        # Show mystical loading message
        loading_message = get_random_loading_message()
        
        with st.spinner(loading_message):
            # Add some mystical delay for effect
            time.sleep(1)
            
            # Check if we have reference images and use appropriate method
            reference_images = SessionManager.get_reference_images()
            
            if reference_images:
                # Use the edit endpoint with reference images for better fidelity
                image, enhanced_prompt = generator.generate_image_with_reference_files(prompt, reference_images)
            else:
                # Use regular generation without references
                image, enhanced_prompt = generator.generate_image(prompt, False)
            
            # Store in session state
            SessionManager.set_generated_image(image)
            SessionManager.add_to_history(prompt, image)
            
            # Store generation timestamp
            st.session_state["generation_timestamp"] = time.time()
            
            # Navigate to result page
            SessionManager.navigate_to_result()
            st.rerun()
            
    except ImageGenerationError as e:
        st.error(str(e))
    except Exception as e:
        error_msg = format_error_message(e)
        st.error(error_msg)