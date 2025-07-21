"""
Landing Page Component for ALF Abstractor
The mystical entry point to the digital swamp
"""

import streamlit as st
from components.styles import load_alf_css, create_title, create_subtitle, create_quote, create_mystical_text
from utils.helpers import get_random_alf_quote
from utils.session_manager import SessionManager
from config import UI_TEXT

def render_landing_page():
    """Render the mystical landing page"""
    load_alf_css()
    
    # Create centered layout
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Main title with mystical styling
        st.markdown(
            create_title(UI_TEXT["LANDING"]["title"]), 
            unsafe_allow_html=True
        )
        
        # Subtitle
        st.markdown(
            create_subtitle(UI_TEXT["LANDING"]["subtitle"]), 
            unsafe_allow_html=True
        )
        
        # Rotating ALF quote for mystical atmosphere
        quote = get_random_alf_quote()
        st.markdown(create_quote(quote), unsafe_allow_html=True)
        
        # Spacing
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Enter button with mystical styling
        if st.button(UI_TEXT["LANDING"]["enter_button"], key="enter_btn"):
            SessionManager.navigate_to_prompt()
            st.rerun()
        
        # Bottom mystical text
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown(
            create_mystical_text(UI_TEXT["LANDING"]["footer"]), 
            unsafe_allow_html=True
        )