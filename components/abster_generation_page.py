"""
Abster Generation Page Component for ALF Abstractor
Where the mystical ALF and Abster the Green Penguin of Abstract image generation happens
"""

import streamlit as st
import time
from components.styles import load_alf_css, create_title
from services.image_generator import ALFImageGenerator, ImageGenerationError
from utils.helpers import get_random_loading_message, format_error_message
from utils.session_manager import SessionManager
from config import UI_TEXT

def render_abster_generation_page():
    """Render the ALF and Abster image generation page"""
    load_alf_css()
    
    st.markdown(
        create_title("🌀 ALF & Abster are Manifesting...", "page-header"), 
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
            st.info(f"**Abstract adventure prompt:** {current_prompt}")
        
        # Show reference images if available
        alf_ref_images = SessionManager.get_reference_images()
        abster_ref_images = SessionManager.get_abster_reference_images()
        
        if alf_ref_images or abster_ref_images:
            st.markdown("**🖼️ Using Reference Images:**")
            
            col_gen_ref1, col_gen_ref2 = st.columns(2)
            
            with col_gen_ref1:
                if alf_ref_images:
                    st.markdown("**🐊 ALF References:**")
                    for i, img in enumerate(alf_ref_images[-2:]):  # Show last 2 ALF
                        st.image(img, caption=f"ALF Ref {i+1}", use_column_width=True)
            
            with col_gen_ref2:
                if abster_ref_images:
                    st.markdown("**🐧 Abster References:**")
                    for i, img in enumerate(abster_ref_images[-2:]):  # Show last 2 Abster
                        st.image(img, caption=f"Abster Ref {i+1}", use_column_width=True)
        
        # Generation button
        if api_key and current_prompt:
            if st.button("Generate ALF & Abster Adventure"):
                _generate_abster_image(api_key, current_prompt)
        
        # Navigation buttons
        col_nav1, col_nav2 = st.columns(2)
        
        with col_nav1:
            if st.button("🔙 Back to Prompt"):
                SessionManager.navigate_to_abster_prompt()
                st.rerun()
        
        with col_nav2:
            # Show result button if image exists
            if SessionManager.has_generated_image():
                if st.button("🎭 View Adventure"):
                    SessionManager.navigate_to_abster_result()
                    st.rerun()

def _generate_abster_image(api_key: str, prompt: str):
    """
    Generate ALF and Abster image using the provided API key and prompt
    
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
            "🐊🐧 ALF and Abster are preparing their abstract adventure...",
            "🌌 Creating mystical abstract patterns...", 
            "💚 Painting green penguin feathers...",
            "🎨 Building geometric realms...",
            "✨ Weaving abstract magic...",
            "🔮 Mixing crocodile green with abstract geometry..."
        ]
        
        import random
        loading_message = random.choice(loading_messages)
        
        with st.spinner(loading_message):
            # Add some mystical delay for effect
            time.sleep(1)
            
            # Enhance prompt specifically for ALF and Abster
            abster_enhanced_prompt = _enhance_abster_prompt(prompt)
            
            # Get both ALF and Abster reference images
            alf_reference_images = SessionManager.get_reference_images()
            abster_reference_images = SessionManager.get_abster_reference_images()
            
            # Combine both reference sets for generation
            all_reference_images = []
            if alf_reference_images:
                all_reference_images.extend(alf_reference_images)
            if abster_reference_images:
                all_reference_images.extend(abster_reference_images)
            
            if all_reference_images:
                # Use the edit endpoint with combined reference images for better fidelity
                image, enhanced_prompt = generator.generate_image_with_reference_files(abster_enhanced_prompt, all_reference_images)
            else:
                # Use regular generation without references
                image, enhanced_prompt = generator.generate_image(abster_enhanced_prompt, False)
            
            # Store in session state
            SessionManager.set_generated_image(image)
            SessionManager.add_to_history(prompt, image)
            
            # Store generation timestamp
            st.session_state["generation_timestamp"] = time.time()
            
            # Navigate to result page
            SessionManager.navigate_to_abster_result()
            st.rerun()
            
    except ImageGenerationError as e:
        st.error(str(e))
    except Exception as e:
        error_msg = format_error_message(e)
        st.error(error_msg)

def _enhance_abster_prompt(user_prompt: str) -> str:
    """
    Enhance user prompt with Abster-specific styling and context
    
    Args:
        user_prompt (str): User's original prompt
        
    Returns:
        str: Enhanced prompt with Abster styling
    """
    
    abster_context = (
    "Abster is a cheerful green and white cartoon penguin with smooth, rounded features, "
    "a small orange beak, and expressive black eyes. His design is simple, cute, and clean, "
    "with a friendly, thoughtful expression. His green color is distinct and should match the reference image exactly. "
    )

    alf_context = (
    "ALF is a friendly cartoon crocodile with green scales, white tech goggles, and a green digital vest. "
    "He has a warm, adventurous expression and appears clever and fun-loving. "
    )

    combined_reference_instruction = (
    "Use both Abster and ALF's reference images to accurately represent their appearance. "
    "Ensure Abster and ALF appear together in the scene described below, interacting naturally. "
    )

    user_scene = user_prompt  # Example: "exploring geometric landscapes with floating abstract shapes"


    enhanced_prompt = (
    f"{abster_context}{alf_context}{combined_reference_instruction} "
    f"The scene shows Abster and ALF {user_scene}. "
    "Abster retains his smooth, cute cartoon style, while ALF maintains his tech-themed appearance. "
    "High-quality digital illustration with soft shading and creative lighting. "
    "The scene should have a whimsical, imaginative atmosphere that highlights their friendship and shared adventure. "
    "Render both characters side by side, clearly visible, and actively engaged in the described scene. "
)
    
    return enhanced_prompt