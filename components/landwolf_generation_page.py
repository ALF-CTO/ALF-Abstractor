"""
Landwolf Generation Page Component for ALF Abstractor
Where the mystical ALF and Landwolf the Hairy Wolf crypto meme image generation happens
"""

import streamlit as st
import time
from components.styles import load_alf_css, create_title
from services.image_generator import ALFImageGenerator, ImageGenerationError
from utils.helpers import get_random_loading_message, format_error_message
from utils.session_manager import SessionManager
from config import UI_TEXT

def render_landwolf_generation_page():
    """Render the ALF and Landwolf image generation page"""
    load_alf_css()
    
    st.markdown(
        create_title("🌀 ALF & Landwolf are Howling...", "page-header"), 
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
            st.info(f"**Hairy wolf crypto adventure prompt:** {current_prompt}")
        
        # Show reference images if available
        alf_ref_images = SessionManager.get_reference_images()
        landwolf_ref_images = SessionManager.get_landwolf_reference_images()
        
        if alf_ref_images or landwolf_ref_images:
            st.markdown("**🖼️ Using Reference Images:**")
            
            col_gen_ref1, col_gen_ref2 = st.columns(2)
            
            with col_gen_ref1:
                if alf_ref_images:
                    st.markdown("**🐊 ALF References:**")
                    for i, img in enumerate(alf_ref_images[-2:]):  # Show last 2 ALF
                        st.image(img, caption=f"ALF Ref {i+1}", use_column_width=True)
            
            with col_gen_ref2:
                if landwolf_ref_images:
                    st.markdown("**🐺 Landwolf References:**")
                    for i, img in enumerate(landwolf_ref_images[-2:]):  # Show last 2 Landwolf
                        st.image(img, caption=f"Landwolf Ref {i+1}", use_column_width=True)
        
        # Generation button
        if api_key and current_prompt:
            if st.button("Generate ALF & Landwolf Adventure"):
                _generate_landwolf_image(api_key, current_prompt)
        
        # Navigation buttons
        col_nav1, col_nav2 = st.columns(2)
        
        with col_nav1:
            if st.button("🔙 Back to Prompt"):
                SessionManager.navigate_to_landwolf_prompt()
                st.rerun()
        
        with col_nav2:
            # Show result button if image exists
            if SessionManager.has_generated_image():
                if st.button("🎭 View Adventure"):
                    SessionManager.navigate_to_landwolf_result()
                    st.rerun()

def _generate_landwolf_image(api_key: str, prompt: str):
    """
    Generate ALF and Landwolf image using the provided API key and prompt
    
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
            "🐊🐺 ALF and Landwolf are howling at the crypto moon...",
            "🌙 Creating the most legendary hairy wolf memes...", 
            "💎 Painting wolf fur with diamond-handed energy...",
            "🚀 Building pack-hunting crypto adventures...",
            "🌲 Weaving forest wisdom with blockchain magic...",
            "⚡ Mixing crocodile scales with wild wolf spirit..."
        ]
        
        import random
        loading_message = random.choice(loading_messages)
        
        with st.spinner(loading_message):
            # Add some mystical delay for effect
            time.sleep(1)
            
            # Enhance prompt specifically for ALF and Landwolf
            landwolf_enhanced_prompt = _enhance_landwolf_prompt(prompt)
            
            # Get both ALF and Landwolf reference images
            alf_reference_images = SessionManager.get_reference_images()
            landwolf_reference_images = SessionManager.get_landwolf_reference_images()
            
            # Combine both reference sets for generation
            all_reference_images = []
            if alf_reference_images:
                all_reference_images.extend(alf_reference_images)
            if landwolf_reference_images:
                all_reference_images.extend(landwolf_reference_images)
            
            if all_reference_images:
                # Use the edit endpoint with combined reference images for better fidelity
                image, enhanced_prompt = generator.generate_image_with_reference_files(landwolf_enhanced_prompt, all_reference_images)
            else:
                # Use regular generation without references
                image, enhanced_prompt = generator.generate_image(landwolf_enhanced_prompt, False)
            
            # Store in session state
            SessionManager.set_generated_image(image)
            SessionManager.add_to_history(prompt, image)
            
            # Store generation timestamp
            st.session_state["generation_timestamp"] = time.time()
            
            # Navigate to result page
            SessionManager.navigate_to_landwolf_result()
            st.rerun()
            
    except ImageGenerationError as e:
        st.error(str(e))
    except Exception as e:
        error_msg = format_error_message(e)
        st.error(error_msg)

def _enhance_landwolf_prompt(user_prompt: str) -> str:
    """
    Enhance user prompt with Landwolf-specific styling and context
    
    Args:
        user_prompt (str): User's original prompt
        
    Returns:
        str: Enhanced prompt with Landwolf styling
    """
    
    landwolf_context = (
    "Landwolf is a cartoon meme character resembling a hairy wolfman with a shaggy brown beard, "
    "wild hair, and a wide pink smile. He wears bright red sunglasses with reflective lenses and a light purple outfit. "
    "His hands and feet are bare, adding to his surreal, playful style. "
    "Landwolf is known in crypto culture as a legendary meme wolf, confident and pack-minded, "
    "often shown climbing green candlesticks and embracing wild crypto energy. "
    "His appearance should exactly match the reference image provided, including his beard, sunglasses, clothing, and playful expression. "
    )

    alf_context = (
    "ALF is a friendly cartoon crocodile with green scales, white tech goggles, and a green digital vest. "
    "He has a warm, adventurous expression and appears clever and fun-loving. "
    )

    combined_reference_instruction = (
    "Use both Landwolf and ALF's reference images to accurately represent their appearance. "
    "Ensure Landwolf and ALF appear together in the scene described below, with Landwolf showing his wild crypto pack energy. "
    )

    user_scene = user_prompt  # Example: "howling at the moon while diamond-handing crypto"

    enhanced_prompt = (
    f"{landwolf_context}{alf_context}{combined_reference_instruction} "
    f"The scene shows Landwolf and ALF {user_scene}. "
    "Landwolf retains his wild, hairy wolf style, and ALF maintains his tech-themed, fun-loving appearance. "
    "Render both characters clearly visible, side by side or in action, fully engaged in the described scene."
    )
    
    return enhanced_prompt 