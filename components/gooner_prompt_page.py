"""
GOONER Prompt Page Component for ALF Abstractor
Where users craft prompts for ALF and GOONER the Blue Penguin adventures
"""

import streamlit as st
from components.styles import load_alf_css, create_title, create_mystical_text
from utils.helpers import validate_prompt_length
from utils.session_manager import SessionManager
from config import UI_TEXT

# GOONER-specific prompt components
GOONER_PROMPT_OBJECTS = [
    "ALF and GOONER swimming in crystal blue waters",
    "ALF and GOONER sliding down sapphire ice slides",
    "ALF and GOONER building blue ice castles together",
    "ALF and GOONER dancing under azure skies",
    "ALF and GOONER exploring cobalt caves",
    "ALF and GOONER playing in turquoise pools",
    "ALF and GOONER painting with blue pigments",
    "ALF and GOONER watching blue whales migrate",
    "ALF and GOONER collecting blue crystals",
    "ALF and GOONER surfing on blue waves",
    "ALF and GOONER in a navy blue submarine",
    "ALF and GOONER stargazing under midnight blue skies",
    "ALF and GOONER making blue snow angels",
    "ALF and GOONER racing through cerulean fields"
]

GOONER_PROMPT_SETTINGS = [
    "in an endless blue ocean",
    "surrounded by floating blue bubbles",
    "in a sapphire ice palace",
    "on a brilliant blue glacier",
    "in a cerulean wonderland",
    "among azure crystal formations",
    "in a cobalt digital realm",
    "on a turquoise rainbow bridge",
    "in an enchanted blue forest",
    "within electric blue light patterns",
    "on a navy blue mountain peak",
    "in a peaceful blue lagoon"
]

GOONER_PROMPT_EMOTIONS = [
    "energetically blue and joyful",
    "brilliantly happy and vibrant", 
    "enthusiastically excited",
    "peacefully blue and serene",
    "curiously exploring blue wonders",
    "cheerfully laughing together",
    "calmly floating in blue bliss",
    "magically blue and wondering",
    "radiantly happy and blue",
    "harmoniously blue and content"
]

def generate_random_gooner_prompt():
    """Generate a random prompt for ALF and GOONER"""
    import random
    
    obj = random.choice(GOONER_PROMPT_OBJECTS)
    setting = random.choice(GOONER_PROMPT_SETTINGS)
    emotion = random.choice(GOONER_PROMPT_EMOTIONS)
    
    return f"{obj} {setting}, both characters are {emotion}"

def mix_gooner_prompt_components():
    """Mix different GOONER prompt components"""
    import random
    
    # Take random components
    obj1 = random.choice(GOONER_PROMPT_OBJECTS)
    obj2 = random.choice(GOONER_PROMPT_OBJECTS)
    setting = random.choice(GOONER_PROMPT_SETTINGS)
    emotion = random.choice(GOONER_PROMPT_EMOTIONS)
    
    # Create mixed prompt
    base = obj1.split(" together")[0] if " together" in obj1 else obj1
    return f"{base} and having blue fun {setting}, both {emotion}"

def render_gooner_prompt_page():
    """Render the GOONER prompt input page"""
    load_alf_css()
    
    st.markdown(
        create_title("🐊🐧 ALF & GOONER Blue Adventures", "page-header"), 
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        # Description text
        st.markdown(
            create_mystical_text("Describe the blue adventure ALF and GOONER will experience..."), 
            unsafe_allow_html=True
        )
        
        # Show GOONER info
        st.info("🐧 **GOONER** is the bluest penguin there is - full of energy and blue enthusiasm for adventures with ALF!")
        
        # Main prompt input
        current_prompt = SessionManager.get_current_prompt()
        prompt = st.text_area(
            "ALF & GOONER Blue Adventure Prompt",
            value=current_prompt,
            placeholder="e.g., ALF and GOONER swimming through crystal blue waters in an endless blue ocean, both energetically blue and joyful",
            height=100,
            key="gooner_prompt",
            label_visibility="collapsed"
        )
        
        # Update session state with current prompt
        if prompt != current_prompt:
            SessionManager.set_current_prompt(prompt)
        
        # Button row for prompt generation
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            if st.button("🎲 Random Blue Adventure"):
                random_prompt = generate_random_gooner_prompt()
                SessionManager.set_current_prompt(random_prompt)
                st.rerun()
        
        with col_b:
            if st.button("🌀 Mix Blue Adventure"):
                mixed_prompt = mix_gooner_prompt_components()
                SessionManager.set_current_prompt(mixed_prompt)
                st.rerun()
        
        with col_c:
            if st.button("🔙 Back to Friends"):
                SessionManager.navigate_to_friends()
                st.rerun()
        
        # Show validation feedback
        if prompt:
            is_valid, error_msg = validate_prompt_length(prompt)
            if not is_valid:
                st.warning(error_msg)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Reference images section - show both ALF and GOONER references
        col_ref1, col_ref2 = st.columns(2)
        
        with col_ref1:
            st.markdown("### 🐊 ALF Reference Images")
            
            ref_info = SessionManager.get_reference_images_info()
            ref_images = SessionManager.get_reference_images()
            
            if ref_info["image_count"] > 0:
                st.markdown(f"📁 **{ref_info['image_count']} ALF images loaded**")
                
                # Display ALF reference images
                if ref_images:
                    for i, img in enumerate(ref_images[:2]):  # Show first 2 ALF images
                        st.image(img, caption=f"ALF Ref {i+1}", use_column_width=True)
                    
                    if len(ref_images) > 2:
                        st.caption(f"+ {len(ref_images) - 2} more ALF images")
                
                # Reload ALF button
                if st.button("🔄 Reload ALF References", key="reload_alf"):
                    SessionManager.load_reference_images_from_folder()
                    st.rerun()
            else:
                st.info("📂 No ALF reference images found.")
                st.caption(f"Add ALF images to: `{ref_info['folder_path']}`")
                
                if st.button("🔄 Check for ALF Images", key="check_alf"):
                    SessionManager.load_reference_images_from_folder()
                    st.rerun()
        
        with col_ref2:
            st.markdown("### 🐧 GOONER Reference Images")
            
            gooner_ref_info = SessionManager.get_gooner_reference_images_info()
            gooner_ref_images = SessionManager.get_gooner_reference_images()
            
            if gooner_ref_info["image_count"] > 0:
                st.markdown(f"📁 **{gooner_ref_info['image_count']} GOONER images loaded**")
                
                # Display GOONER reference images
                if gooner_ref_images:
                    for i, img in enumerate(gooner_ref_images[:2]):  # Show first 2 GOONER images
                        st.image(img, caption=f"GOONER Ref {i+1}", use_column_width=True)
                    
                    if len(gooner_ref_images) > 2:
                        st.caption(f"+ {len(gooner_ref_images) - 2} more GOONER images")
                
                # Reload GOONER button
                if st.button("🔄 Reload GOONER References", key="reload_gooner"):
                    SessionManager.load_gooner_reference_images_from_folder()
                    st.rerun()
            else:
                st.info("📂 No GOONER reference images found.")
                st.caption(f"Add GOONER images to: `{gooner_ref_info['folder_path']}`")
                
                if st.button("🔄 Check for GOONER Images", key="check_gooner"):
                    SessionManager.load_gooner_reference_images_from_folder()
                    st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Generate button
        if st.button("🌟 Generate ALF & GOONER Adventure", key="generate_gooner_btn"):
            current_prompt = SessionManager.get_current_prompt()
            if current_prompt.strip():
                is_valid, error_msg = validate_prompt_length(current_prompt)
                if is_valid:
                    SessionManager.navigate_to_gooner_generating()
                    st.rerun()
                else:
                    st.error(error_msg)
            else:
                st.warning("You must describe the blue adventure to summon ALF and GOONER...")