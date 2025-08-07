"""
GOD Generation Page Component for ALF Abstractor
Where the mystical ALF and GOD the Golden Dog dyslexic image generation happens
"""

import streamlit as st
import time
from components.styles import load_alf_css, create_title
from services.image_generator import ALFImageGenerator, ImageGenerationError
from utils.helpers import get_random_loading_message, format_error_message
from utils.session_manager import SessionManager
from config import UI_TEXT

def render_god_generation_page():
    """Render the ALF and GOD image generation page"""
    load_alf_css()
    
    st.markdown(
        create_title("🌀 ALF & GOD are Dyslexically Creating...", "page-header"), 
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
            st.info(f"**Dyslexic adventure prompt:** {current_prompt}")
        
        # Show reference images if available
        alf_ref_images = SessionManager.get_reference_images()
        god_ref_images = SessionManager.get_god_reference_images()
        
        if alf_ref_images or god_ref_images:
            st.markdown("**🖼️ Using Reference Images:**")
            
            col_gen_ref1, col_gen_ref2 = st.columns(2)
            
            with col_gen_ref1:
                if alf_ref_images:
                    st.markdown("**🐊 ALF References:**")
                    for i, img in enumerate(alf_ref_images[-2:]):  # Show last 2 ALF
                        st.image(img, caption=f"ALF Ref {i+1}", use_column_width=True)
            
            with col_gen_ref2:
                if god_ref_images:
                    st.markdown("**🐕 GOD References:**")
                    for i, img in enumerate(god_ref_images[-2:]):  # Show last 2 GOD
                        st.image(img, caption=f"GOD Ref {i+1}", use_column_width=True)
        
        # Generation button
        if api_key and current_prompt:
            if st.button("Generate ALF & GOD Adventure"):
                _generate_god_image(api_key, current_prompt)
        
        # Navigation buttons
        col_nav1, col_nav2 = st.columns(2)
        
        with col_nav1:
            if st.button("🔙 Back to Prompt"):
                SessionManager.navigate_to_god_prompt()
                st.rerun()
        
        with col_nav2:
            # Show result button if image exists
            if SessionManager.has_generated_image():
                if st.button("🎭 View Adventure"):
                    SessionManager.navigate_to_god_result()
                    st.rerun()

def _generate_god_image(api_key: str, prompt: str):
    """
    Generate ALF and GOD image using the provided API key and prompt
    
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
            "🐊🐕 ALF and GOD are mixing up letters in golden dimensions...",
            "✨ Creating the most brilliant dyslexic art...", 
            "🌟 Painting golden retriever fur with floating letters...",
            "📝 Building beautifully confused golden realms...",
            "🎨 Weaving dyslexic magic...",
            "💫 Mixing crocodile green with golden dog wisdom..."
        ]
        
        import random
        loading_message = random.choice(loading_messages)
        
        with st.spinner(loading_message):
            # Add some mystical delay for effect
            time.sleep(1)
            
            # Enhance prompt specifically for ALF and GOD
            god_enhanced_prompt = _enhance_god_prompt(prompt)
            
            # Get both ALF and GOD reference images
            alf_reference_images = SessionManager.get_reference_images()
            god_reference_images = SessionManager.get_god_reference_images()
            
            # Combine both reference sets for generation
            all_reference_images = []
            if alf_reference_images:
                all_reference_images.extend(alf_reference_images)
            if god_reference_images:
                all_reference_images.extend(god_reference_images)
            
            if all_reference_images:
                # Use the edit endpoint with combined reference images for better fidelity
                image, enhanced_prompt = generator.generate_image_with_reference_files(god_enhanced_prompt, all_reference_images)
            else:
                # Use regular generation without references
                image, enhanced_prompt = generator.generate_image(god_enhanced_prompt, False)
            
            # Store in session state
            SessionManager.set_generated_image(image)
            SessionManager.add_to_history(prompt, image)
            
            # Store generation timestamp
            st.session_state["generation_timestamp"] = time.time()
            
            # Navigate to result page
            SessionManager.navigate_to_god_result()
            st.rerun()
            
    except ImageGenerationError as e:
        st.error(str(e))
    except Exception as e:
        error_msg = format_error_message(e)
        st.error(error_msg)

def _enhance_god_prompt(user_prompt: str) -> str:
    """
    Enhance user prompt with GOD-specific styling and context
    
    Args:
        user_prompt (str): User's original prompt
        
    Returns:
        str: Enhanced prompt with GOD styling
    """
    
    god_context = (
    "GOD is a small cartoon golden dog with an orange-yellow coat, large round eyes behind glasses, "
    "and a slightly puzzled but innocent expression. He wears a green collar with a gold tag labeled 'G'. "
    "GOD is gentle and curious. "
    "He often appears to be lost in thought or trying to understand something important. "
    "His appearance should exactly match the reference image provided, including his proportions, glasses, and collar. "
    )

    alf_context = (
    "ALF is a friendly cartoon crocodile with green scales, white tech goggles, and a green digital vest. "
    "He has a warm, adventurous expression and appears clever and fun-loving. "
    )

    combined_reference_instruction = (
    "Use both GOD and ALF's reference images to accurately represent their appearance. "
    "Ensure GOD and ALF appear together in the scene described below, with GOD showing his dyslexic golden magic. "
    )

    user_scene = user_prompt  # Example: "playing with backwards letters in a golden field"

    enhanced_prompt = (
    f"{god_context}{alf_context}{combined_reference_instruction} "
    f"The scene shows GOD and ALF {user_scene}. "
    "GOD retains his small, curious cartoon style and puzzled expression, "
    "and ALF maintains his tech-savvy, cheerful appearance. "
    "High-quality digital illustration with soft, warm lighting and glowing golden tones. "
    "The setting should emphasize creativity, kindness, and the joy of imperfection. "
    "Render both characters clearly visible, side by side or actively engaged, within the charming, golden scene."
    )
    
    return enhanced_prompt