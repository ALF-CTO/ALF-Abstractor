"""
Brett Generation Page Component for ALF Abstractor
Where the mystical ALF and Brett the Blue Guy crypto meme image generation happens
"""

import streamlit as st
import time
from components.styles import load_alf_css, create_title
from services.image_generator import ALFImageGenerator, ImageGenerationError
from utils.helpers import get_random_loading_message, format_error_message
from utils.session_manager import SessionManager
from config import UI_TEXT

def render_brett_generation_page():
    """Render the ALF and Brett image generation page"""
    load_alf_css()
    
    st.markdown(
        create_title("🌀 ALF & Brett are Vibing...", "page-header"), 
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
            st.info(f"**Blue guy crypto adventure prompt:** {current_prompt}")
        
        # Show reference images if available
        alf_ref_images = SessionManager.get_reference_images()
        brett_ref_images = SessionManager.get_brett_reference_images()
        
        if alf_ref_images or brett_ref_images:
            st.markdown("**🖼️ Using Reference Images:**")
            
            col_gen_ref1, col_gen_ref2 = st.columns(2)
            
            with col_gen_ref1:
                if alf_ref_images:
                    st.markdown("**🐊 ALF References:**")
                    for i, img in enumerate(alf_ref_images[-2:]):  # Show last 2 ALF
                        st.image(img, caption=f"ALF Ref {i+1}", use_column_width=True)
            
            with col_gen_ref2:
                if brett_ref_images:
                    st.markdown("**🔵 Brett References:**")
                    for i, img in enumerate(brett_ref_images[-2:]):  # Show last 2 Brett
                        st.image(img, caption=f"Brett Ref {i+1}", use_column_width=True)
        
        # Generation button
        if api_key and current_prompt:
            if st.button("Generate ALF & Brett Adventure"):
                _generate_brett_image(api_key, current_prompt)
        
        # Navigation buttons
        col_nav1, col_nav2 = st.columns(2)
        
        with col_nav1:
            if st.button("🔙 Back to Prompt"):
                SessionManager.navigate_to_brett_prompt()
                st.rerun()
        
        with col_nav2:
            # Show result button if image exists
            if SessionManager.has_generated_image():
                if st.button("🎭 View Adventure"):
                    SessionManager.navigate_to_brett_result()
                    st.rerun()

def _generate_brett_image(api_key: str, prompt: str):
    """
    Generate ALF and Brett image using the provided API key and prompt
    
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
            "🐊🔵 ALF and Brett are radiating cool blue crypto energy...",
            "🌊 Creating the most vibrant blue meme adventures...", 
            "💙 Painting deep blue wisdom with blockchain coolness...",
            "🔷 Building ocean-powered crypto realms...",
            "✨ Weaving deep blue knowledge with meme magic...",
            "⚡ Mixing crocodile green with electric blue vibes..."
        ]
        
        import random
        loading_message = random.choice(loading_messages)
        
        with st.spinner(loading_message):
            # Add some mystical delay for effect
            time.sleep(1)
            
            # Enhance prompt specifically for ALF and Brett
            brett_enhanced_prompt = _enhance_brett_prompt(prompt)
            
            # Get both ALF and Brett reference images
            alf_reference_images = SessionManager.get_reference_images()
            brett_reference_images = SessionManager.get_brett_reference_images()
            
            # Combine both reference sets for generation
            all_reference_images = []
            if alf_reference_images:
                all_reference_images.extend(alf_reference_images)
            if brett_reference_images:
                all_reference_images.extend(brett_reference_images)
            
            if all_reference_images:
                # Use the edit endpoint with combined reference images for better fidelity
                image, enhanced_prompt = generator.generate_image_with_reference_files(brett_enhanced_prompt, all_reference_images)
            else:
                # Use regular generation without references
                image, enhanced_prompt = generator.generate_image(brett_enhanced_prompt, False)
            
            # Store in session state
            SessionManager.set_generated_image(image)
            SessionManager.add_to_history(prompt, image)
            
            # Store generation timestamp
            st.session_state["generation_timestamp"] = time.time()
            
            # Navigate to result page
            SessionManager.navigate_to_brett_result()
            st.rerun()
            
    except ImageGenerationError as e:
        st.error(str(e))
    except Exception as e:
        error_msg = format_error_message(e)
        st.error(error_msg)

def _enhance_brett_prompt(user_prompt: str) -> str:
    """
    Enhance user prompt with Brett-specific styling and context
    
    Args:
        user_prompt (str): User's original prompt
        
    Returns:
        str: Enhanced prompt with Brett styling
    """
    
    brett_context = (
    "Brett is a cartoon blue meme character with a blocky frog-like head, smooth blue skin, "
    "large round bulging eyes, and a wide pink mouth with a visible tongue. "
    "He has a goofy, expressive meme-style face that is instantly recognizable in crypto culture. "
    "Brett is known for his cool, laid-back meme confidence—representing iconic internet energy in crypto spaces. "
    "His appearance should exactly match the reference image provided, including his rounded head shape, big eyes, "
    "pink mouth, and vibrant blue coloring. "
    )

    alf_context = (
    "ALF is a friendly cartoon crocodile with green scales, white tech goggles, and a green digital vest. "
    "He has a warm, adventurous expression and appears clever and fun-loving. "
    "His appearance should also match the reference image exactly. "
    )

    combined_reference_instruction = (
    "Use both Brett and ALF's reference images to accurately represent their appearance, colors, and proportions. "
    "Ensure Brett and ALF appear together in the scene described below, with Brett showing his laid-back meme energy. "
    )

    user_scene = user_prompt  # e.g., "analyzing crypto charts on giant floating blue candlesticks"

    enhanced_prompt = (
    f"{brett_context}{alf_context}{combined_reference_instruction} "
    f"The scene shows Brett and ALF {user_scene}. "
    "Brett retains his frog-like, meme-style blue design while radiating cool meme confidence, "
    "and ALF maintains his tech-themed, adventurous appearance. "
    "Render both characters clearly visible, side by side or in action, fully engaged in the described crypto meme scene."
    )
    
    return enhanced_prompt