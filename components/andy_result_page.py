"""
Andy Result Page Component for ALF Abstractor
Where the summoned ALF and Andy the Yellow Guy crypto sunshine adventure images are revealed and shared
"""

import streamlit as st
import time
from components.styles import load_alf_css, create_title, create_quote
from services.image_generator import ALFImageGenerator
from utils.helpers import create_share_text
from utils.session_manager import SessionManager
from config import UI_TEXT

# Andy-specific completion quotes (crypto sunshine/optimistic themes)
ANDY_QUOTES = [
    "ALF and Andy's sunshine vibes radiate through the blockchain forever.",
    "In the crypto realm, their yellow wisdom creates brilliant golden gains.",
    "Two friends, one radiant vision, unlimited sun-kissed adventures.",
    "Where bright optimism meets blockchain technology, legends are born.",
    "Their sunshine adventures glow through digital realms eternally.",
    "Green scales and golden yellow spirit, the ultimate crypto sunshine duo.",
    "Every golden moment with Andy makes ALF's portfolio more luminous.",
    "Together they create the most brilliantly optimistic adventures.",
    "In friendship, even bear markets become bull market sunshine celebrations.",
    "The blockchain celebrates ALF and Andy's radiant yellow crypto magic."
]

def render_andy_result_page():
    """Render the result page showing the generated ALF and Andy image"""
    load_alf_css()
    
    st.markdown(
        create_title("🎭 A Radiant Sunshine Adventure Has Emerged...", "page-header"), 
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
                prompt_display = f"Radiant sunshine adventure created with: {current_prompt}"
                st.markdown(create_quote(prompt_display), unsafe_allow_html=True)
            
            # Add an Andy-specific completion quote
            import random
            completion_quote = random.choice(ANDY_QUOTES)
            st.markdown(create_quote(completion_quote), unsafe_allow_html=True)
            
            # Action buttons
            _render_andy_action_buttons(image, current_prompt)
            
        else:
            # No image found
            st.error("No radiant sunshine adventure found in the digital realm...")
            if st.button("🔙 Return to Friends"):
                SessionManager.navigate_to_friends()
                st.rerun()

def _render_andy_action_buttons(image, prompt: str):
    """
    Render the action buttons for the Andy result page
    
    Args:
        image: The generated PIL image
        prompt (str): The prompt used for generation
    """
    col_a, col_b, col_c, col_d = st.columns(4)
    
    with col_a:
        # Download button
        if image:
            image_bytes = ALFImageGenerator.image_to_bytes(image)
            filename = f"alf_andy_adventure_{int(time.time())}.png"
            
            st.download_button(
                label="📥 Download Adventure",
                data=image_bytes,
                file_name=filename,
                mime="image/png"
            )
    
    with col_b:
        # Make another button
        if st.button("🔄 New Adventure"):
            SessionManager.navigate_to_andy_prompt()
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
            _show_andy_share_options(prompt)

def _show_andy_share_options(prompt: str):
    """
    Show sharing options for the generated ALF and Andy adventure
    
    Args:
        prompt (str): The prompt used for generation
    """
    st.info("Copy this page URL to share your ALF & Andy radiant sunshine adventure!")
    
    # Create shareable text for Andy adventures
    share_text = f"🐊🟡 Just created a radiant ALF & Andy crypto sunshine adventure!\n\nPrompt: {prompt}\n\n#ALFandAndy #SunshineVibes #YellowCrypto #AIArt #BrightCrypto"
    
    # Show the share text in an expandable section
    with st.expander("📋 Copy Share Text"):
        st.code(share_text)
        st.caption("Share your ALF & Andy radiant sunshine adventure on social media!")

def render_andy_image_history():
    """Render a sidebar or expander showing recent Andy adventures (optional feature)"""
    history = SessionManager.get_history()
    
    # Filter for Andy-related adventures (those containing "Andy" in the prompt)
    andy_history = [item for item in history if "andy" in item['prompt'].lower()]
    
    if andy_history:
        with st.expander(f"🟡 Recent Andy Adventures ({len(andy_history)})"):
            for i, item in enumerate(reversed(andy_history[-5:])):  # Show last 5
                st.markdown(f"**{i+1}.** {item['prompt'][:50]}...")
                if 'timestamp' in item:
                    timestamp = time.strftime('%H:%M:%S', time.localtime(item['timestamp']))
                    st.caption(f"Adventure at: {timestamp}")
                st.markdown("---")