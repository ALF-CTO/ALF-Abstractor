"""
ALF Abstractor - Main Application
The Surreal Image Generator for the Abstract Blockchain

Modular Streamlit application using clean architecture principles
"""

import streamlit as st

# Import configuration
from config import APP_CONFIG, PAGES

# Import utilities
from utils.session_manager import SessionManager

# Import page components
from components.landing_page import render_landing_page
from components.friends_page import render_friends_page
from components.prompt_page import render_prompt_page
from components.generation_page import render_generation_page
from components.result_page import render_result_page, render_image_history
from components.polly_prompt_page import render_polly_prompt_page
from components.polly_generation_page import render_polly_generation_page
from components.polly_result_page import render_polly_result_page, render_polly_image_history

def configure_app():
    """Configure the Streamlit application"""
    st.set_page_config(
        page_title=APP_CONFIG["page_title"],
        page_icon=APP_CONFIG["page_icon"],
        layout=APP_CONFIG["layout"],
        initial_sidebar_state=APP_CONFIG["initial_sidebar_state"]
    )

def main():
    """Main application entry point"""
    # Configure the app
    configure_app()
    
    # Initialize session state
    SessionManager.initialize_session()
    
    # Load reference images on first run
    if "references_loaded" not in st.session_state:
        with st.spinner("🐊 Loading ALF reference images..."):
            num_alf_loaded = SessionManager.load_reference_images_from_folder()
        with st.spinner("🐧 Loading Polly reference images..."):
            num_polly_loaded = SessionManager.load_polly_reference_images_from_folder()
        st.session_state["references_loaded"] = True
    
    # Get current page from session
    current_page = SessionManager.get_current_page()
    
    # Route to appropriate page component
    if current_page == PAGES["LANDING"]:
        render_landing_page()
    elif current_page == PAGES["FRIENDS"]:
        render_friends_page()
    elif current_page == PAGES["PROMPT"]:
        render_prompt_page()
    elif current_page == PAGES["GENERATING"]:
        render_generation_page()
    elif current_page == PAGES["RESULT"]:
        render_result_page()
        # Optionally show image history in sidebar or expandable section
        render_image_history()
    elif current_page == PAGES["POLLY_PROMPT"]:
        render_polly_prompt_page()
    elif current_page == PAGES["POLLY_GENERATING"]:
        render_polly_generation_page()
    elif current_page == PAGES["POLLY_RESULT"]:
        render_polly_result_page()
        # Optionally show Polly image history in sidebar or expandable section
        render_polly_image_history()
    else:
        # Fallback to landing page if invalid page
        SessionManager.set_page(PAGES["LANDING"])
        st.rerun()

if __name__ == "__main__":
    main()