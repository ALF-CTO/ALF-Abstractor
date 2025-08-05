"""
Retsba Result Page Component for ALF Abstractor
Where the summoned ALF and Retsba the Red Penguin villain adventure images are revealed and shared
"""

import streamlit as st
import time
from components.styles import load_alf_css, create_title, create_quote
from services.image_generator import ALFImageGenerator
from utils.helpers import create_share_text
from utils.session_manager import SessionManager
from config import UI_TEXT

# Retsba-specific completion quotes (villainous themes)
RETSBA_QUOTES = [
    "ALF and Retsba's confrontation echoes through the abstract realms.",
    "In the crimson chaos, their eternal struggle continues.",
    "Two forces, one light, one dark, infinite possibilities.",
    "Where heroism meets villainy, epic adventures unfold.",
    "Their dramatic clash ripples through digital dimensions.",
    "Green scales and red feathers, perfect opposition.",
    "Every villainous encounter with Retsba tests ALF's resolve.",
    "Together they dance the eternal dance of good versus evil.",
    "In opposition, they create the most compelling stories.",
    "The digital cosmos trembles at ALF and Retsba's epic battles."
]

def render_retsba_result_page():
    """Render the result page showing the generated ALF and Retsba image"""
    load_alf_css()
    
    st.markdown(
        create_title("🎭 A Villainous Adventure Has Emerged...", "page-header"), 
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
                prompt_display = f"Villainous adventure created with: {current_prompt}"
                st.markdown(create_quote(prompt_display), unsafe_allow_html=True)
            
            # Add a Retsba-specific completion quote
            import random
            completion_quote = random.choice(RETSBA_QUOTES)
            st.markdown(create_quote(completion_quote), unsafe_allow_html=True)
            
            # Action buttons
            _render_retsba_action_buttons(image, current_prompt)
            
        else:
            # No image found
            st.error("No villainous adventure found in the digital realm...")
            if st.button("🔙 Return to Friends"):
                SessionManager.navigate_to_friends()
                st.rerun()

def _render_retsba_action_buttons(image, prompt: str):
    """
    Render the action buttons for the Retsba result page
    
    Args:
        image: The generated PIL image
        prompt (str): The prompt used for generation
    """
    col_a, col_b, col_c, col_d = st.columns(4)
    
    with col_a:
        # Download button
        if image:
            image_bytes = ALFImageGenerator.image_to_bytes(image)
            filename = f"alf_retsba_adventure_{int(time.time())}.png"
            
            st.download_button(
                label="📥 Download Adventure",
                data=image_bytes,
                file_name=filename,
                mime="image/png"
            )
    
    with col_b:
        # Make another button
        if st.button("🔄 New Adventure"):
            SessionManager.navigate_to_retsba_prompt()
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
            _show_retsba_share_options(prompt)

def _show_retsba_share_options(prompt: str):
    """
    Show sharing options for the generated ALF and Retsba adventure
    
    Args:
        prompt (str): The prompt used for generation
    """
    st.info("Copy this page URL to share your ALF & Retsba villainous adventure!")
    
    # Create shareable text for Retsba adventures
    share_text = f"🐊🐧 Just created an epic ALF & Retsba villainous adventure!\n\nPrompt: {prompt}\n\n#ALFandRetsba #VillainousAdventures #AIArt #AbstractVillain"
    
    # Show the share text in an expandable section
    with st.expander("📋 Copy Share Text"):
        st.code(share_text)
        st.caption("Share your ALF & Retsba villainous adventure on social media!")

def render_retsba_image_history():
    """Render a sidebar or expander showing recent Retsba adventures (optional feature)"""
    history = SessionManager.get_history()
    
    # Filter for Retsba-related adventures (those containing "Retsba" in the prompt)
    retsba_history = [item for item in history if "retsba" in item['prompt'].lower()]
    
    if retsba_history:
        with st.expander(f"🐧 Recent Retsba Adventures ({len(retsba_history)})"):
            for i, item in enumerate(reversed(retsba_history[-5:])):  # Show last 5
                st.markdown(f"**{i+1}.** {item['prompt'][:50]}...")
                if 'timestamp' in item:
                    timestamp = time.strftime('%H:%M:%S', time.localtime(item['timestamp']))
                    st.caption(f"Adventure at: {timestamp}")
                st.markdown("---")