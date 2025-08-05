"""
Retsba Generation Page Component for ALF Abstractor
Where the mystical ALF and Retsba the Red Penguin villain image generation happens
"""

import streamlit as st
import time
from components.styles import load_alf_css, create_title
from services.image_generator import ALFImageGenerator, ImageGenerationError
from utils.helpers import get_random_loading_message, format_error_message
from utils.session_manager import SessionManager
from config import UI_TEXT

def render_retsba_generation_page():
    """Render the ALF and Retsba image generation page"""
    load_alf_css()
    
    st.markdown(
        create_title("🌀 ALF & Retsba are Scheming...", "page-header"), 
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # API key input - using widget key to manage state directly
        api_key = st.text_input(
            "Enter your OpenAI API Key:", 
            type="password", 
            key="api_key"
        )
        
        current_prompt = SessionManager.get_current_prompt()
        
        # Show current prompt
        if current_prompt:
            st.info(f"**Villainous adventure prompt:** {current_prompt}")
        
        # Show reference images if available
        alf_ref_images = SessionManager.get_reference_images()
        retsba_ref_images = SessionManager.get_retsba_reference_images()
        
        if alf_ref_images or retsba_ref_images:
            st.markdown("**🖼️ Using Reference Images:**")
            
            col_gen_ref1, col_gen_ref2 = st.columns(2)
            
            with col_gen_ref1:
                if alf_ref_images:
                    st.markdown("**🐊 ALF References:**")
                    for i, img in enumerate(alf_ref_images[-2:]):  # Show last 2 ALF
                        st.image(img, caption=f"ALF Ref {i+1}", use_column_width=True)
            
            with col_gen_ref2:
                if retsba_ref_images:
                    st.markdown("**🐧 Retsba References:**")
                    for i, img in enumerate(retsba_ref_images[-2:]):  # Show last 2 Retsba
                        st.image(img, caption=f"Retsba Ref {i+1}", use_column_width=True)
        
        # Generation button
        if api_key and current_prompt:
            if st.button("Generate ALF & Retsba Adventure"):
                _generate_retsba_image(api_key, current_prompt)
        
        # Navigation buttons
        col_nav1, col_nav2 = st.columns(2)
        
        with col_nav1:
            if st.button("🔙 Back to Prompt"):
                SessionManager.navigate_to_retsba_prompt()
                st.rerun()
        
        with col_nav2:
            # Show result button if image exists
            if SessionManager.has_generated_image():
                if st.button("🎭 View Adventure"):
                    SessionManager.navigate_to_retsba_result()
                    st.rerun()

def _generate_retsba_image(api_key: str, prompt: str):
    """
    Generate ALF and Retsba image using the provided API key and prompt
    
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
        loading_messages = [
            "🐊🐧 ALF and Retsba are plotting their villainous adventure...",
            "🔴 Creating sinister red abstractions...", 
            "🌋 Painting the most villainous red feathers...",
            "⚡ Building chaotic red dimensions...",
            "✨ Weaving dark abstract magic...",
            "🎨 Mixing crocodile green with villainous red..."
        ]
        
        import random
        loading_message = random.choice(loading_messages)
        
        with st.spinner(loading_message):
            # Add some mystical delay for effect
            time.sleep(1)
            
            # Enhance prompt specifically for ALF and Retsba
            retsba_enhanced_prompt = _enhance_retsba_prompt(prompt)
            
            # Get both ALF and Retsba reference images
            alf_reference_images = SessionManager.get_reference_images()
            retsba_reference_images = SessionManager.get_retsba_reference_images()
            
            # Combine both reference sets for generation
            all_reference_images = []
            if alf_reference_images:
                all_reference_images.extend(alf_reference_images)
            if retsba_reference_images:
                all_reference_images.extend(retsba_reference_images)
            
            if all_reference_images:
                # Use the edit endpoint with combined reference images for better fidelity
                image, enhanced_prompt = generator.generate_image_with_reference_files(retsba_enhanced_prompt, all_reference_images)
            else:
                # Use regular generation without references
                image, enhanced_prompt = generator.generate_image(retsba_enhanced_prompt, False)
            
            # Store in session state
            SessionManager.set_generated_image(image)
            SessionManager.add_to_history(prompt, image)
            
            # Store generation timestamp
            st.session_state["generation_timestamp"] = time.time()
            
            # Navigate to result page
            SessionManager.navigate_to_retsba_result()
            st.rerun()
            
    except ImageGenerationError as e:
        st.error(str(e))
    except Exception as e:
        error_msg = format_error_message(e)
        st.error(error_msg)

def _enhance_retsba_prompt(user_prompt: str) -> str:
    """
    Enhance user prompt with Retsba-specific styling and context
    
    Args:
        user_prompt (str): User's original prompt
        
    Returns:
        str: Enhanced prompt with Retsba styling
    """
    
    retsba_context = (
    "Retsba is a bold red cartoon penguin with crimson feathers, a white belly, a blue beak, and thick black eyebrows. "
    "He has an intense, determined expression with a serious and competitive attitude. "
    "His appearance is clean, strong, and striking, with sharp contrast and a powerful stance. "
    "Retsba’s look should match the reference image exactly, with bright red coloring and cartoon proportions. "
    )

    alf_context = (
    "ALF is a friendly cartoon crocodile with green scales, white tech goggles, and a green digital vest. "
    "He has a warm, adventurous expression and appears clever and fun-loving. "
    )

    combined_reference_instruction = (
    "Use both Retsba and ALF's reference images to accurately represent their appearance. "
    "Ensure Retsba and ALF appear together in the scene described below, with Retsba showing his villainous nature. "
    )

    user_scene = user_prompt  # Example: "battling through chaotic red abstract dimensions"

    enhanced_prompt = (
    f"{retsba_context}{alf_context}{combined_reference_instruction} "
    f"The scene shows Retsba and ALF {user_scene}. "
    "Retsba maintains his bold, serious cartoon style with vivid red coloring, and ALF retains his tech-themed friendly appearance. "
    "High-quality digital illustration with dramatic lighting, rich colors, and stylized cartoon shading. "
    "Energetic, competitive atmosphere that emphasizes the contrast between Retsba’s intensity and ALF’s friendly confidence. "
    "Render both characters clearly visible, side by side or in active conflict, fully engaged in the described scene."
    )
    
    return enhanced_prompt