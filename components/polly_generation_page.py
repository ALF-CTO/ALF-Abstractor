"""
Polly Generation Page Component for ALF Abstractor
Where the mystical ALF and Polly image generation happens
"""

import streamlit as st
import time
from components.styles import load_alf_css, create_title
from services.image_generator import ALFImageGenerator, ImageGenerationError
from utils.helpers import get_random_loading_message, format_error_message
from utils.session_manager import SessionManager
from config import UI_TEXT

def render_polly_generation_page():
    """Render the ALF and Polly image generation page"""
    load_alf_css()
    
    st.markdown(
        create_title("🌀 ALF & Polly are Manifesting...", "page-header"), 
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
            st.info(f"**Adventure prompt:** {current_prompt}")
        
        # Show reference images if available
        alf_ref_images = SessionManager.get_reference_images()
        polly_ref_images = SessionManager.get_polly_reference_images()
        
        if alf_ref_images or polly_ref_images:
            st.markdown("**🖼️ Using Reference Images:**")
            
            col_gen_ref1, col_gen_ref2 = st.columns(2)
            
            with col_gen_ref1:
                if alf_ref_images:
                    st.markdown("**🐊 ALF References:**")
                    for i, img in enumerate(alf_ref_images[-2:]):  # Show last 2 ALF
                        st.image(img, caption=f"ALF Ref {i+1}", use_column_width=True)
            
            with col_gen_ref2:
                if polly_ref_images:
                    st.markdown("**🐧 Polly References:**")
                    for i, img in enumerate(polly_ref_images[-2:]):  # Show last 2 Polly
                        st.image(img, caption=f"Polly Ref {i+1}", use_column_width=True)
        
        # Generation button
        if api_key and current_prompt:
            if st.button("Generate ALF & Polly Adventure"):
                _generate_polly_image(api_key, current_prompt)
        
        # Navigation buttons
        col_nav1, col_nav2 = st.columns(2)
        
        with col_nav1:
            if st.button("🔙 Back to Prompt"):
                SessionManager.navigate_to_polly_prompt()
                st.rerun()
        
        with col_nav2:
            # Show result button if image exists
            if SessionManager.has_generated_image():
                if st.button("🎭 View Adventure"):
                    SessionManager.navigate_to_polly_result()
                    st.rerun()

def _generate_polly_image(api_key: str, prompt: str):
    """
    Generate ALF and Polly image using the provided API key and prompt
    
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
            "🐊🐧 ALF and Polly are preparing their adventure...",
            "❄️ Creating magical ice crystals...", 
            "🌈 Painting pink penguin feathers...",
            "🏔️ Building enchanted ice kingdoms...",
            "✨ Weaving friendship magic...",
            "🎨 Mixing crocodile green with penguin pink..."
        ]
        
        import random
        loading_message = random.choice(loading_messages)
        
        with st.spinner(loading_message):
            # Add some mystical delay for effect
            time.sleep(1)
            
            # Enhance prompt specifically for ALF and Polly
            polly_enhanced_prompt = _enhance_polly_prompt(prompt)
            
            # Get both ALF and Polly reference images
            alf_reference_images = SessionManager.get_reference_images()
            polly_reference_images = SessionManager.get_polly_reference_images()
            
            # Combine both reference sets for generation
            all_reference_images = []
            if alf_reference_images:
                all_reference_images.extend(alf_reference_images)
            if polly_reference_images:
                all_reference_images.extend(polly_reference_images)
            
            if all_reference_images:
                # Use the edit endpoint with combined reference images for better fidelity
                image, enhanced_prompt = generator.generate_image_with_reference_files(polly_enhanced_prompt, all_reference_images)
            else:
                # Use regular generation without references
                image, enhanced_prompt = generator.generate_image(polly_enhanced_prompt, False)
            
            # Store in session state
            SessionManager.set_generated_image(image)
            SessionManager.add_to_history(prompt, image)
            
            # Store generation timestamp
            st.session_state["generation_timestamp"] = time.time()
            
            # Navigate to result page
            SessionManager.navigate_to_polly_result()
            st.rerun()
            
    except ImageGenerationError as e:
        st.error(str(e))
    except Exception as e:
        error_msg = format_error_message(e)
        st.error(error_msg)

def _enhance_polly_prompt(user_prompt: str) -> str:
    """
    Enhance user prompt with Polly-specific styling and context
    
    Args:
        user_prompt (str): User's original prompt
        
    Returns:
        str: Enhanced prompt with Polly styling
    """
    
    polly_context = (
    "Polly is a cheerful pink penguin with a friendly expression, cute round features, and a distinct pink body. "
    "She is wearing a playful accessory (like a scarf or hat) as seen in her reference image. "
    )

    alf_context = (
    "ALF is a friendly cartoon crocodile with green scales, white tech goggles, and a green digital vest. "
    "He has a warm, adventurous expression and appears clever and fun-loving. "
    )

    combined_reference_instruction = (
    "Use both Polly and ALF’s reference images to accurately represent their appearance. "
    "Ensure Polly and ALF appear together in the scene described below, interacting naturally. "
    )

    user_scene = user_prompt  # Example: "exploring a glowing jungle with magical plants"

    enhanced_prompt = (
    f"{polly_context}{alf_context}{combined_reference_instruction} "
    f"The scene shows Polly and ALF {user_scene}. "
    "Both characters have whimsical, cartoon-style proportions and friendly expressions. "
    "High-quality digital illustration with soft shading and warm lighting. "
    "Colorful, magical atmosphere that emphasizes their friendship and shared adventure. "
    "Render them side by side, clearly visible, and actively engaged in the scene."
    )
    
    return enhanced_prompt