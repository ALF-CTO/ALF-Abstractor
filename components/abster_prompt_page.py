"""
Abster Prompt Page Component for ALF Abstractor
Where users craft prompts for ALF and Abster the Green Penguin of Abstract adventures
"""

import streamlit as st
from components.styles import load_alf_css, create_title, create_mystical_text
from utils.helpers import validate_prompt_length
from utils.session_manager import SessionManager
from config import UI_TEXT

# Abster-specific prompt components
ABSTER_PROMPT_OBJECTS = [
    "ALF and Abster creating geometric art together",
    "ALF and Abster exploring abstract dimensions",
    "ALF and Abster building crystalline structures",
    "ALF and Abster dancing with floating shapes",
    "ALF and Abster solving mathematical puzzles",
    "ALF and Abster painting with light patterns",
    "ALF and Abster in a gallery of living art",
    "ALF and Abster composing visual symphonies",
    "ALF and Abster crafting digital sculptures",
    "ALF and Abster weaving reality patterns",
    "ALF and Abster in a maze of mirrors",
    "ALF and Abster conducting color experiments",
    "ALF and Abster building thought constructs",
    "ALF and Abster exploring fractal gardens"
]

ABSTER_PROMPT_SETTINGS = [
    "in a geometric wonderland",
    "surrounded by floating abstractions",
    "in a crystalline art studio",
    "on a platform of pure thought",
    "in a digital museum",
    "among living mathematical equations",
    "in a realm of pure creativity",
    "on an abstract rainbow bridge",
    "in an enchanted geometry forest",
    "within kaleidoscope dimensions",
    "on a mountain of shifting patterns",
    "in a cosmic art laboratory"
]

ABSTER_PROMPT_EMOTIONS = [
    "intellectually curious and inspired",
    "thoughtful and creative", 
    "excited about discovery",
    "peaceful and contemplative",
    "amazed by abstract beauty",
    "focused and artistic",
    "mystical and philosophical",
    "enlightened and wondering",
    "harmonious and balanced",
    "visionary and innovative"
]

def generate_random_abster_prompt():
    """Generate a random prompt for ALF and Abster"""
    import random
    
    obj = random.choice(ABSTER_PROMPT_OBJECTS)
    setting = random.choice(ABSTER_PROMPT_SETTINGS)
    emotion = random.choice(ABSTER_PROMPT_EMOTIONS)
    
    return f"{obj} {setting}, both characters are {emotion}"

def mix_abster_prompt_components():
    """Mix different Abster prompt components"""
    import random
    
    # Take random components
    obj1 = random.choice(ABSTER_PROMPT_OBJECTS)
    obj2 = random.choice(ABSTER_PROMPT_OBJECTS)
    setting = random.choice(ABSTER_PROMPT_SETTINGS)
    emotion = random.choice(ABSTER_PROMPT_EMOTIONS)
    
    # Create mixed prompt
    base = obj1.split(" together")[0] if " together" in obj1 else obj1
    return f"{base} and collaborating artistically {setting}, both {emotion}"

def render_abster_prompt_page():
    """Render the Abster prompt input page"""
    load_alf_css()
    
    st.markdown(
        create_title("🐊🐧 ALF & Abster Abstract Adventures", "page-header"), 
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        # Description text
        st.markdown(
            create_mystical_text("Describe the abstract adventure ALF and Abster will create..."), 
            unsafe_allow_html=True
        )
        
        # Show Abster info
        st.info("🐧 **Abster** is the Green Penguin of Abstract - a thoughtful artist who loves geometric adventures with ALF!")
        
        # Main prompt input
        current_prompt = SessionManager.get_current_prompt()
        prompt = st.text_area(
            "ALF & Abster Abstract Adventure Prompt",
            value=current_prompt,
            placeholder="e.g., ALF and Abster creating a floating geometric sculpture in a crystalline art studio, both intellectually curious and inspired",
            height=100,
            key="abster_prompt",
            label_visibility="collapsed"
        )
        
        # Update session state with current prompt
        if prompt != current_prompt:
            SessionManager.set_current_prompt(prompt)
        
        # Button row for prompt generation
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            if st.button("🎲 Random Abstract Adventure"):
                random_prompt = generate_random_abster_prompt()
                SessionManager.set_current_prompt(random_prompt)
                st.rerun()
        
        with col_b:
            if st.button("🌀 Mix Abstract Adventure"):
                mixed_prompt = mix_abster_prompt_components()
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
        
        # Reference images section - show both ALF and Abster references
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
            st.markdown("### 🐧 Abster Reference Images")
            
            abster_ref_info = SessionManager.get_abster_reference_images_info()
            abster_ref_images = SessionManager.get_abster_reference_images()
            
            if abster_ref_info["image_count"] > 0:
                st.markdown(f"📁 **{abster_ref_info['image_count']} Abster images loaded**")
                
                # Display Abster reference images
                if abster_ref_images:
                    for i, img in enumerate(abster_ref_images[:2]):  # Show first 2 Abster images
                        st.image(img, caption=f"Abster Ref {i+1}", use_column_width=True)
                    
                    if len(abster_ref_images) > 2:
                        st.caption(f"+ {len(abster_ref_images) - 2} more Abster images")
                
                # Reload Abster button
                if st.button("🔄 Reload Abster References", key="reload_abster"):
                    SessionManager.load_abster_reference_images_from_folder()
                    st.rerun()
            else:
                st.info("📂 No Abster reference images found.")
                st.caption(f"Add Abster images to: `{abster_ref_info['folder_path']}`")
                
                if st.button("🔄 Check for Abster Images", key="check_abster"):
                    SessionManager.load_abster_reference_images_from_folder()
                    st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Generate button
        if st.button("🌟 Generate ALF & Abster Adventure", key="generate_abster_btn"):
            current_prompt = SessionManager.get_current_prompt()
            if current_prompt.strip():
                is_valid, error_msg = validate_prompt_length(current_prompt)
                if is_valid:
                    SessionManager.navigate_to_abster_generating()
                    st.rerun()
                else:
                    st.error(error_msg)
            else:
                st.warning("You must describe the abstract adventure to summon ALF and Abster...")