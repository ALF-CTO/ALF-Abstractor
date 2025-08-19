"""
Andy Generation Page Component for ALF Abstractor
Where the mystical ALF and Andy the Yellow Guy crypto meme image generation happens
"""

import streamlit as st
import time
from components.styles import load_alf_css, create_title
from services.image_generator import ALFImageGenerator, ImageGenerationError
from utils.helpers import get_random_loading_message, format_error_message
from utils.session_manager import SessionManager
from config import UI_TEXT

def render_andy_generation_page():
    """Render the ALF and Andy image generation page"""
    load_alf_css()
    
    st.markdown(
        create_title("🌀 ALF & Andy are Glowing...", "page-header"), 
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
            st.info(f"**Yellow guy crypto adventure prompt:** {current_prompt}")
        
        # Show reference images if available
        alf_ref_images = SessionManager.get_reference_images()
        andy_ref_images = SessionManager.get_andy_reference_images()
        
        if alf_ref_images or andy_ref_images:
            st.markdown("**🖼️ Using Reference Images:**")
            
            col_gen_ref1, col_gen_ref2 = st.columns(2)
            
            with col_gen_ref1:
                if alf_ref_images:
                    st.markdown("**🐊 ALF References:**")
                    for i, img in enumerate(alf_ref_images[-2:]):  # Show last 2 ALF
                        st.image(img, caption=f"ALF Ref {i+1}", use_column_width=True)
            
            with col_gen_ref2:
                if andy_ref_images:
                    st.markdown("**🟡 Andy References:**")
                    for i, img in enumerate(andy_ref_images[-2:]):  # Show last 2 Andy
                        st.image(img, caption=f"Andy Ref {i+1}", use_column_width=True)
        
        # Generation button
        if api_key and current_prompt:
            if st.button("Generate ALF & Andy Adventure"):
                _generate_andy_image(api_key, current_prompt)
        
        # Navigation buttons
        col_nav1, col_nav2 = st.columns(2)
        
        with col_nav1:
            if st.button("🔙 Back to Prompt"):
                SessionManager.navigate_to_andy_prompt()
                st.rerun()
        
        with col_nav2:
            # Show result button if image exists
            if SessionManager.has_generated_image():
                if st.button("🎭 View Adventure"):
                    SessionManager.navigate_to_andy_result()
                    st.rerun()

def _generate_andy_image(api_key: str, prompt: str):
    """
    Generate ALF and Andy image using the provided API key and prompt
    
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
            "🐊🟡 ALF and Andy are radiating bright yellow crypto energy...",
            "☀️ Creating the most luminous yellow meme adventures...", 
            "💛 Painting bright yellow optimism with blockchain gold...",
            "🌟 Building sunshine-powered crypto realms...",
            "✨ Weaving golden yellow wisdom with meme magic...",
            "⚡ Mixing crocodile green with radiant yellow vibes..."
        ]
        
        import random
        loading_message = random.choice(loading_messages)
        
        with st.spinner(loading_message):
            # Add some mystical delay for effect
            time.sleep(1)
            
            # Enhance prompt specifically for ALF and Andy
            andy_enhanced_prompt = _enhance_andy_prompt(prompt)
            
            # Get both ALF and Andy reference images
            alf_reference_images = SessionManager.get_reference_images()
            andy_reference_images = SessionManager.get_andy_reference_images()
            
            # Combine both reference sets for generation
            all_reference_images = []
            if alf_reference_images:
                all_reference_images.extend(alf_reference_images)
            if andy_reference_images:
                all_reference_images.extend(andy_reference_images)
            
            if all_reference_images:
                # Use the edit endpoint with combined reference images for better fidelity
                image, enhanced_prompt = generator.generate_image_with_reference_files(andy_enhanced_prompt, all_reference_images)
            else:
                # Use regular generation without references
                image, enhanced_prompt = generator.generate_image(andy_enhanced_prompt, False)
            
            # Store in session state
            SessionManager.set_generated_image(image)
            SessionManager.add_to_history(prompt, image)
            
            # Store generation timestamp
            st.session_state["generation_timestamp"] = time.time()
            
            # Navigate to result page
            SessionManager.navigate_to_andy_result()
            st.rerun()
            
    except ImageGenerationError as e:
        st.error(str(e))
    except Exception as e:
        error_msg = format_error_message(e)
        st.error(error_msg)

def _enhance_andy_prompt(user_prompt: str) -> str:
    """
    Enhance user prompt with Andy-specific styling and context
    
    Args:
        user_prompt (str): User's original prompt
        
    Returns:
        str: Enhanced prompt with Andy styling
    """
    
    andy_context = (
    "Andy is a cartoon yellow dog-like meme character with floppy ears, smooth bright yellow skin, "
    "large meme-style eyes, and a wide open mouth showing a pink tongue. "
    "He has a humorous, carefree, and optimistic expression that radiates positive meme energy. "
    "Andy is known in crypto culture as a sunny, radiant figure—always bright, uplifting, and playful. "
    "His appearance should exactly match the reference image provided, including his floppy ears, big eyes, "
    "wide mouth with visible tongue, and vibrant yellow coloring. "
    )

    alf_context = (
    "ALF is a friendly cartoon crocodile with green scales, white tech goggles, and a green digital vest. "
    "He has a warm, adventurous expression and appears clever and fun-loving. "
    )

    combined_reference_instruction = (
    "Use both Andy and ALF's reference images to accurately represent their appearance, proportions, and colors. "
    "Ensure Andy and ALF appear together in the scene described below, with Andy expressing his radiant crypto optimism. "
    )

    user_scene = user_prompt  # e.g., "spreading sunshine vibes while trading crypto"

    enhanced_prompt = (
    f"{andy_context}{alf_context}{combined_reference_instruction} "
    f"The scene shows Andy and ALF {user_scene}. "
    "Andy retains his goofy, bright yellow cartoon dog style, "
    "and ALF maintains his tech-themed, adventurous appearance. "
    "Render both characters clearly visible, side by side or in action, fully engaged."
    )
    
    return enhanced_prompt