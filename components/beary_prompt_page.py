"""
Beary Prompt Page Component for ALF Abstractor
Where users craft prompts for ALF and Beary the Brown Bear prankster adventures
"""

import streamlit as st
from components.styles import load_alf_css, create_title, create_mystical_text
from utils.helpers import validate_prompt_length
from utils.session_manager import SessionManager
from config import UI_TEXT

# Beary-specific prompt components (prankster themes)
BEARY_PROMPT_OBJECTS = [
    "ALF and Beary setting up elaborate pranks together",
    "ALF and Beary planning hilarious comedy schemes",
    "ALF and Beary building funny trap mechanisms",
    "ALF and Beary orchestrating brown bear comedy shows",
    "ALF and Beary creating mischievous abstract patterns",
    "ALF and Beary designing joke-filled environments",
    "ALF and Beary constructing prank obstacle courses",
    "ALF and Beary preparing surprise comedy acts",
    "ALF and Beary crafting humorous digital illusions",
    "ALF and Beary inventing new comedy techniques",
    "ALF and Beary staging elaborate joke performances",
    "ALF and Beary building whimsical prank contraptions",
    "ALF and Beary creating comedic abstract sculptures",
    "ALF and Beary designing laughter-filled adventures"
]

BEARY_PROMPT_SETTINGS = [
    "in a comedy-filled dimension",
    "surrounded by floating joke bubbles",
    "in a whimsical brown bear circus",
    "on a platform of pure laughter",
    "in a mischievous playground",
    "among giggling geometric shapes",
    "in a realm of pure comedy",
    "on a bridge of banana peels",
    "in an enchanted prank workshop",
    "within swirling comedy energy",
    "on a mountain of whoopee cushions",
    "in a hilarious abstract funhouse"
]

BEARY_PROMPT_EMOTIONS = [
    "playfully mischievous and giggling",
    "hilariously scheming and clever", 
    "joyfully planning the next prank",
    "comedically focused on fun",
    "mischievously collaborating together",
    "laughingly creative with tricks",
    "playfully competitive in pranks",
    "cheerfully causing harmless chaos",
    "humorously inventive and silly",
    "delightfully planning comedy magic"
]

def generate_random_beary_prompt():
    """Generate a random prompt for ALF and Beary"""
    import random
    
    obj = random.choice(BEARY_PROMPT_OBJECTS)
    setting = random.choice(BEARY_PROMPT_SETTINGS)
    emotion = random.choice(BEARY_PROMPT_EMOTIONS)
    
    return f"{obj} {setting}, both characters are {emotion}"

def mix_beary_prompt_components():
    """Mix different Beary prompt components"""
    import random
    
    # Take random components
    obj1 = random.choice(BEARY_PROMPT_OBJECTS)
    obj2 = random.choice(BEARY_PROMPT_OBJECTS)
    setting = random.choice(BEARY_PROMPT_SETTINGS)
    emotion = random.choice(BEARY_PROMPT_EMOTIONS)
    
    # Create mixed prompt
    base = obj1.split(" together")[0] if " together" in obj1 else obj1
    return f"{base} and having comedic fun {setting}, both {emotion}"

def render_beary_prompt_page():
    """Render the Beary prompt input page"""
    load_alf_css()
    
    st.markdown(
        create_title("🐊🐻 ALF & Beary Prankster Adventures", "page-header"), 
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        # Description text
        st.markdown(
            create_mystical_text("Describe the prankster adventure ALF and Beary will create..."), 
            unsafe_allow_html=True
        )
        
        # Show Beary info
        st.success("🐻 **Beary** is number 1 prankster in abstract chain - a hilarious brown bear who loves comedy adventures with ALF!")
        
        # Main prompt input
        current_prompt = SessionManager.get_current_prompt()
        prompt = st.text_area(
            "ALF & Beary Prankster Adventure Prompt",
            value=current_prompt,
            placeholder="e.g., ALF and Beary setting up elaborate pranks together in a comedy-filled dimension, both playfully mischievous and giggling",
            height=100,
            key="beary_prompt",
            label_visibility="collapsed"
        )
        
        # Update session state with current prompt
        if prompt != current_prompt:
            SessionManager.set_current_prompt(prompt)
        
        # Button row for prompt generation
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            if st.button("🎲 Random Comedy Adventure"):
                random_prompt = generate_random_beary_prompt()
                SessionManager.set_current_prompt(random_prompt)
                st.rerun()
        
        with col_b:
            if st.button("🌀 Mix Comedy Adventure"):
                mixed_prompt = mix_beary_prompt_components()
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
        
        # Reference images section - show both ALF and Beary references
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
            st.markdown("### 🐻 Beary Reference Images")
            
            beary_ref_info = SessionManager.get_beary_reference_images_info()
            beary_ref_images = SessionManager.get_beary_reference_images()
            
            if beary_ref_info["image_count"] > 0:
                st.markdown(f"📁 **{beary_ref_info['image_count']} Beary images loaded**")
                
                # Display Beary reference images
                if beary_ref_images:
                    for i, img in enumerate(beary_ref_images[:2]):  # Show first 2 Beary images
                        st.image(img, caption=f"Beary Ref {i+1}", use_column_width=True)
                    
                    if len(beary_ref_images) > 2:
                        st.caption(f"+ {len(beary_ref_images) - 2} more Beary images")
                
                # Reload Beary button
                if st.button("🔄 Reload Beary References", key="reload_beary"):
                    SessionManager.load_beary_reference_images_from_folder()
                    st.rerun()
            else:
                st.info("📂 No Beary reference images found.")
                st.caption(f"Add Beary images to: `{beary_ref_info['folder_path']}`")
                
                if st.button("🔄 Check for Beary Images", key="check_beary"):
                    SessionManager.load_beary_reference_images_from_folder()
                    st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Generate button
        if st.button("🌟 Generate ALF & Beary Adventure", key="generate_beary_btn"):
            current_prompt = SessionManager.get_current_prompt()
            if current_prompt.strip():
                is_valid, error_msg = validate_prompt_length(current_prompt)
                if is_valid:
                    SessionManager.navigate_to_beary_generating()
                    st.rerun()
                else:
                    st.error(error_msg)
            else:
                st.warning("You must describe the prankster adventure to summon ALF and Beary...")