"""
Beary Result Page Component for ALF Abstractor
Where the summoned ALF and Beary the Brown Bear prankster adventure images are revealed and shared
"""

import streamlit as st
import time
from components.styles import load_alf_css, create_title, create_quote
from services.image_generator import ALFImageGenerator
from utils.helpers import create_share_text
from utils.session_manager import SessionManager
from config import UI_TEXT

# Beary-specific completion quotes (prankster themes)
BEARY_QUOTES = [
    "ALF and Beary's laughter echoes through the abstract chain.",
    "In the comedy dimensions, their pranks become legendary.",
    "Two friends, one hilarious vision, infinite giggles.",
    "Where technology meets comedy, the best pranks emerge.",
    "Their mischievous schemes ripple through digital realms.",
    "Green scales and brown fur, perfect comedy duo.",
    "Every prank with Beary makes ALF's adventures more fun.",
    "Together they create the most elaborate comedy shows.",
    "In friendship, even simple jokes become masterpieces.",
    "The digital cosmos laughs at ALF and Beary's antics."
]

def render_beary_result_page():
    """Render the result page showing the generated ALF and Beary image"""
    load_alf_css()
    
    st.markdown(
        create_title("🎭 A Comedy Adventure Has Emerged...", "page-header"), 
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        image = SessionManager.get_generated_image()
        current_prompt = SessionManager.get_current_prompt()
        
        if image:
            # Display the generated image with mystical border
            st.image(image, use_column_width=True)
            
            # Display the prompt used with mystical quote styling
            if current_prompt:
                prompt_display = f"Comedy adventure created with: {current_prompt}"
                st.markdown(create_quote(prompt_display), unsafe_allow_html=True)
            
            # Add a Beary-specific completion quote
            import random
            completion_quote = random.choice(BEARY_QUOTES)
            st.markdown(create_quote(completion_quote), unsafe_allow_html=True)
            
            # Action buttons
            _render_beary_action_buttons(image, current_prompt)
            
        else:
            # No image found
            st.error("No comedy adventure found in the digital realm...")
            if st.button("🔙 Return to Friends"):
                SessionManager.navigate_to_friends()
                st.rerun()

def _render_beary_action_buttons(image, prompt: str):
    """
    Render the action buttons for the Beary result page
    
    Args:
        image: The generated PIL image
        prompt (str): The prompt used for generation
    """
    col_a, col_b, col_c, col_d = st.columns(4)
    
    with col_a:
        # Download button
        if image:
            image_bytes = ALFImageGenerator.image_to_bytes(image)
            filename = f"alf_beary_adventure_{int(time.time())}.png"
            
            st.download_button(
                label="📥 Download Adventure",
                data=image_bytes,
                file_name=filename,
                mime="image/png"
            )
    
    with col_b:
        # Make another button
        if st.button("🔄 New Adventure"):
            SessionManager.navigate_to_beary_prompt()
            SessionManager.set_current_prompt("")  # Clear previous prompt
            st.rerun()
    
    with col_c:
        # Back to friends button
        if st.button("👫 Other Friends"):
            SessionManager.navigate_to_friends()
            st.rerun()
    
    with col_d:
        # Share button
        if st.button("🎭 Share Adventure"):
            _show_beary_share_options(prompt)

def _show_beary_share_options(prompt: str):
    """
    Show sharing options for the generated ALF and Beary adventure
    
    Args:
        prompt (str): The prompt used for generation
    """
    st.info("Copy this page URL to share your ALF & Beary comedy adventure!")
    
    # Create shareable text for Beary adventures
    share_text = f"🐊🐻 Just created a hilarious ALF & Beary prankster adventure!\n\nPrompt: {prompt}\n\n#ALFandBeary #PranksterAdventures #AIArt #ComedyBear"
    
    # Show the share text in an expandable section
    with st.expander("📋 Copy Share Text"):
        st.code(share_text)
        st.caption("Share your ALF & Beary comedy adventure on social media!")

def render_beary_image_history():
    """Render a sidebar or expander showing recent Beary adventures (optional feature)"""
    history = SessionManager.get_history()
    
    # Filter for Beary-related adventures (those containing "Beary" in the prompt)
    beary_history = [item for item in history if "beary" in item['prompt'].lower()]
    
    if beary_history:
        with st.expander(f"🐻 Recent Beary Adventures ({len(beary_history)})"):
            for i, item in enumerate(reversed(beary_history[-5:])):  # Show last 5
                st.markdown(f"**{i+1}.** {item['prompt'][:50]}...")
                if 'timestamp' in item:
                    timestamp = time.strftime('%H:%M:%S', time.localtime(item['timestamp']))
                    st.caption(f"Adventure at: {timestamp}")
                st.markdown("---")