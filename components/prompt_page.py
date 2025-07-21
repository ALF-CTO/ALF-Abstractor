"""
Prompt Page Component for ALF Abstractor
Where users craft their mystical prompts to summon ALF
"""

import streamlit as st
from components.styles import load_alf_css, create_title, create_mystical_text
from utils.helpers import generate_random_prompt, mix_prompt_components, validate_prompt_length
from utils.session_manager import SessionManager
from config import UI_TEXT

def render_prompt_page():
    """Render the prompt input page"""
    load_alf_css()
    
    st.markdown(
        create_title(UI_TEXT["PROMPT"]["title"], "page-header"), 
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        # Description text
        st.markdown(
            create_mystical_text(UI_TEXT["PROMPT"]["description"]), 
            unsafe_allow_html=True
        )
        
        # Main prompt input
        current_prompt = SessionManager.get_current_prompt()
        prompt = st.text_area(
            "ALF Prompt Input",
            value=current_prompt,
            placeholder=UI_TEXT["PROMPT"]["placeholder"],
            height=100,
            key="main_prompt",
            label_visibility="collapsed"
        )
        
        # Update session state with current prompt
        if prompt != current_prompt:
            SessionManager.set_current_prompt(prompt)
        
        # Button row for prompt generation
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            if st.button(UI_TEXT["PROMPT"]["random_button"]):
                random_prompt = generate_random_prompt()
                SessionManager.set_current_prompt(random_prompt)
                st.rerun()
        
        with col_b:
            if st.button(UI_TEXT["PROMPT"]["mix_button"]):
                mixed_prompt = mix_prompt_components()
                SessionManager.set_current_prompt(mixed_prompt)
                st.rerun()
        
        with col_c:
            if st.button(UI_TEXT["PROMPT"]["back_button"]):
                SessionManager.set_page("landing")
                st.rerun()
        
        # Show validation feedback
        if prompt:
            is_valid, error_msg = validate_prompt_length(prompt)
            if not is_valid:
                st.warning(error_msg)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Reference images section
        st.markdown("### 🖼️ ALF Reference Images")
        
        ref_info = SessionManager.get_reference_images_info()
        ref_images = SessionManager.get_reference_images()
        
        if ref_info["image_count"] > 0:
            st.markdown(f"📁 **{ref_info['image_count']} reference images loaded from folder**")
            
            # Display reference images
            if ref_images:
                cols = st.columns(min(len(ref_images), 4))
                for i, img in enumerate(ref_images):
                    with cols[i % 4]:
                        st.image(img, caption=f"ALF Ref {i+1}", use_column_width=True)
                
                # Reload button
                if st.button("🔄 Reload References"):
                    SessionManager.load_reference_images_from_folder()
                    st.rerun()
        else:
            st.info("📂 No reference images found. Add ALF images to the 'references' folder to use them for generation.")
            st.markdown(f"**Folder location:** `{ref_info['folder_path']}`")
            
            if st.button("🔄 Check for Images"):
                SessionManager.load_reference_images_from_folder()
                st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Generate button
        if st.button(UI_TEXT["PROMPT"]["generate_button"], key="generate_btn"):
            current_prompt = SessionManager.get_current_prompt()
            if current_prompt.strip():
                is_valid, error_msg = validate_prompt_length(current_prompt)
                if is_valid:
                    SessionManager.navigate_to_generating()
                    st.rerun()
                else:
                    st.error(error_msg)
            else:
                st.warning(UI_TEXT["PROMPT"]["empty_prompt_warning"])