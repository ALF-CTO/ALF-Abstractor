"""
GOD Generation Page Component for ALF Abstractor
The mystical generation interface for ALF and GOD the Golden Dog dyslexic adventures
"""

import streamlit as st
import time
import random
from openai import OpenAI
from components.styles import load_alf_css, create_title, create_quote, create_mystical_text
from services.image_generator import ALFImageGenerator
from utils.session_manager import SessionManager
from config import OPENAI_CONFIG

# GOD-specific loading messages (dyslexic/golden themes)
GOD_LOADING_MESSAGES = [
    "Mixing up letters in golden dimensions...",
    "Creating the most brilliant dyslexic art...", 
    "Scrambling words into golden poetry...",
    "Building mixed-up magical realms...",
    "Dyslexically organizing digital adventures...",
    "Golden paws typing backwards messages...",
    "Creating beautifully confused golden scenes...",
    "Mixing letters with golden sparkles..."
]

def render_god_generation_page():
    """Render the generation page for ALF and GOD adventures"""
    load_alf_css()
    
    st.markdown(
        create_title("🌀 ALF & GOD Are Manifesting...", "page-header"), 
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Get the current prompt
        prompt = SessionManager.get_current_prompt()
        
        if not prompt:
            st.error("No adventure prompt found!")
            if st.button("🔙 Back to GOD Prompt"):
                SessionManager.navigate_to_god_prompt()
                st.rerun()
            return
        
        # Show the prompt being used
        st.markdown(
            create_mystical_text(f"Golden adventure brewing: {prompt}"), 
            unsafe_allow_html=True
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # API Key input
        api_key = st.text_input(
            "🔑 Enter your OpenAI API Key:",
            type="password",
            placeholder="sk-...",
            key="god_api_key"
        )
        
        # Generate button
        if st.button("🌟 Generate ALF & GOD Adventure", key="generate_god", type="primary"):
            if not api_key.strip():
                st.error("Please enter your OpenAI API key to generate the adventure.")
                return
                
            _generate_god_adventure(api_key, prompt)
        
        # Back button
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔙 Back to GOD Prompt"):
            SessionManager.navigate_to_god_prompt()
            st.rerun()

def _generate_god_adventure(api_key: str, prompt: str):
    """
    Generate ALF and GOD adventure using OpenAI API
    
    Args:
        api_key (str): OpenAI API key
        prompt (str): User's adventure prompt
    """
    try:
        # Create the enhanced prompt for ALF and GOD
        enhanced_prompt = _create_god_prompt(prompt)
        
        # Show progress with GOD-specific loading messages
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        loading_message = random.choice(GOD_LOADING_MESSAGES)
        status_text.text(loading_message)
        
        # Initialize progress
        for i in range(30):
            progress_bar.progress(i + 1)
            time.sleep(0.1)
        
        # Initialize OpenAI client
        client = OpenAI(api_key=api_key)
        
        status_text.text("🐕 GOD is dyslexically arranging the scene...")
        
        # Get reference images for context
        reference_images = SessionManager.get_reference_images()
        god_reference_images = SessionManager.get_god_reference_images()
        
        # Update progress
        for i in range(30, 60):
            progress_bar.progress(i + 1)
            time.sleep(0.05)
        
        status_text.text("✨ Golden letters swirling into beautiful chaos...")
        
        # Generate the image
        response = client.images.generate(
            model=OPENAI_CONFIG["model"],
            prompt=enhanced_prompt,
            size=OPENAI_CONFIG["size"],
            quality=OPENAI_CONFIG["quality"],
            n=OPENAI_CONFIG["n"]
        )
        
        # Complete progress
        for i in range(60, 100):
            progress_bar.progress(i + 1)
            time.sleep(0.02)
        
        progress_bar.progress(100)
        status_text.text("🎭 Golden adventure complete!")
        
        # Process the generated image
        image_url = response.data[0].url
        image = ALFImageGenerator.download_image(image_url)
        
        if image:
            # Store the image and prompt in session
            SessionManager.set_generated_image(image)
            SessionManager.set_current_prompt(prompt)
            
            # Add to history
            SessionManager.add_to_history(prompt, image)
            
            # Navigate to result page
            SessionManager.navigate_to_god_result()
            st.rerun()
        else:
            st.error("Failed to process the generated adventure. Please try again.")
            
    except Exception as e:
        st.error(f"Error creating ALF & GOD adventure: {str(e)}")
        st.info("Please check your API key and try again.")

def _create_god_prompt(user_prompt: str) -> str:
    """
    Create an enhanced prompt for GOD (dyslexic dog) adventures
    
    Args:
        user_prompt (str): Original user prompt
        
    Returns:
        str: Enhanced prompt for image generation
    """
    # GOD character context with dyslexic themes
    god_context = (
        "A friendly cartoon golden retriever character named GOD with bright golden fur, "
        "playful expression, and slightly confused but happy demeanor. GOD is the dyslexic dog "
        "who mixes up letters and words in charming ways. Whimsical, golden color palette, "
        "same friendly facial features and golden coat as reference image."
    )
    
    # Combine ALF's base prompt with GOD context
    base_context = OPENAI_CONFIG["base_prompt_prefix"]
    
    enhanced_prompt = f"{base_context} Together with {god_context}, they are {user_prompt}. " \
                     f"The scene shows both ALF and GOD in a golden, slightly mixed-up world where " \
                     f"letters float around playfully and words get scrambled in beautiful ways. " \
                     f"{OPENAI_CONFIG['base_prompt_suffix']} Include golden sparkles and floating letters."
    
    return enhanced_prompt

def _show_god_generation_status():
    """Show generation status with GOD-specific theming"""
    with st.spinner("🐕 GOD is dyslexically organizing the adventure..."):
        time.sleep(1)
    
    # Show a GOD quote while generating
    god_quotes = [
        "Wodrs get mxied up, but herat stays true! - GOD",
        "Soeitems the bset advnetures are misspelled! - GOD", 
        "Gloden leters flaot in beutiful chaos! - GOD",
        "I mgiht mix up leters, but I nver mix up frinedship! - GOD"
    ]
    
    quote = random.choice(god_quotes)
    st.markdown(create_quote(quote), unsafe_allow_html=True)