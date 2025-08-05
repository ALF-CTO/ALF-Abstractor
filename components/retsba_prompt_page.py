"""
Retsba Prompt Page Component for ALF Abstractor
Where users craft prompts for ALF and Retsba the Red Penguin villain adventures
"""

import streamlit as st
from components.styles import load_alf_css, create_title, create_mystical_text
from utils.helpers import validate_prompt_length
from utils.session_manager import SessionManager
from config import UI_TEXT

# Retsba-specific prompt components (villainous themes)
RETSBA_PROMPT_OBJECTS = [
    "ALF and Retsba clashing in abstract battlegrounds",
    "ALF and Retsba navigating crimson chaos dimensions",
    "ALF and Retsba confronting twisted red geometries",
    "ALF and Retsba in a villainous abstract showdown",
    "ALF and Retsba exploring dark red labyrinths",
    "ALF and Retsba battling through scarlet storms",
    "ALF and Retsba in menacing ruby crystal caves",
    "ALF and Retsba facing chaotic red vortexes",
    "ALF and Retsba amid sinister abstract patterns",
    "ALF and Retsba in a dramatic red abstract duel",
    "ALF and Retsba traversing dangerous crimson mazes",
    "ALF and Retsba confronting evil red illusions",
    "ALF and Retsba in a tense villainous encounter",
    "ALF and Retsba amid swirling red abstract energy"
]

RETSBA_PROMPT_SETTINGS = [
    "in a chaotic red dimension",
    "surrounded by menacing crimson abstractions",
    "in a villainous scarlet fortress",
    "on a platform of dark red energy",
    "in a sinister abstract realm",
    "among twisted ruby formations",
    "in a realm of pure red chaos",
    "on a bridge of villainous abstractions",
    "in an enchanted crimson battleground",
    "within malevolent red light patterns",
    "on a mountain of dark red crystals",
    "in a treacherous abstract void"
]

RETSBA_PROMPT_EMOTIONS = [
    "dramatically tense and confrontational",
    "villainously scheming and cunning", 
    "intensely focused on the conflict",
    "darkly determined and menacing",
    "mysteriously plotting together",
    "dramatically opposed yet intrigued",
    "suspensefully cautious around each other",
    "chaotically engaging in abstract warfare",
    "dangerously curious about each other",
    "tensely balancing good versus evil"
]

def generate_random_retsba_prompt():
    """Generate a random prompt for ALF and Retsba"""
    import random
    
    obj = random.choice(RETSBA_PROMPT_OBJECTS)
    setting = random.choice(RETSBA_PROMPT_SETTINGS)
    emotion = random.choice(RETSBA_PROMPT_EMOTIONS)
    
    return f"{obj} {setting}, both characters are {emotion}"

def mix_retsba_prompt_components():
    """Mix different Retsba prompt components"""
    import random
    
    # Take random components
    obj1 = random.choice(RETSBA_PROMPT_OBJECTS)
    obj2 = random.choice(RETSBA_PROMPT_OBJECTS)
    setting = random.choice(RETSBA_PROMPT_SETTINGS)
    emotion = random.choice(RETSBA_PROMPT_EMOTIONS)
    
    # Create mixed prompt
    base = obj1.split(" confronting")[0] if " confronting" in obj1 else obj1
    return f"{base} and engaging villainously {setting}, both {emotion}"

def render_retsba_prompt_page():
    """Render the Retsba prompt input page"""
    load_alf_css()
    
    st.markdown(
        create_title("🐊🐧 ALF & Retsba Villainous Adventures", "page-header"), 
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        # Description text
        st.markdown(
            create_mystical_text("Describe the villainous adventure ALF and Retsba will encounter..."), 
            unsafe_allow_html=True
        )
        
        # Show Retsba info
        st.warning("🐧 **Retsba** is The villain of Abstract - a cunning red penguin who brings chaos to adventures with ALF!")
        
        # Main prompt input
        current_prompt = SessionManager.get_current_prompt()
        prompt = st.text_area(
            "ALF & Retsba Villainous Adventure Prompt",
            value=current_prompt,
            placeholder="e.g., ALF and Retsba clashing in abstract battlegrounds in a chaotic red dimension, both dramatically tense and confrontational",
            height=100,
            key="retsba_prompt",
            label_visibility="collapsed"
        )
        
        # Update session state with current prompt
        if prompt != current_prompt:
            SessionManager.set_current_prompt(prompt)
        
        # Button row for prompt generation
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            if st.button("🎲 Random Villainous Adventure"):
                random_prompt = generate_random_retsba_prompt()
                SessionManager.set_current_prompt(random_prompt)
                st.rerun()
        
        with col_b:
            if st.button("🌀 Mix Villainous Adventure"):
                mixed_prompt = mix_retsba_prompt_components()
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
        
        # Reference images section - show both ALF and Retsba references
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
            st.markdown("### 🐧 Retsba Reference Images")
            
            retsba_ref_info = SessionManager.get_retsba_reference_images_info()
            retsba_ref_images = SessionManager.get_retsba_reference_images()
            
            if retsba_ref_info["image_count"] > 0:
                st.markdown(f"📁 **{retsba_ref_info['image_count']} Retsba images loaded**")
                
                # Display Retsba reference images
                if retsba_ref_images:
                    for i, img in enumerate(retsba_ref_images[:2]):  # Show first 2 Retsba images
                        st.image(img, caption=f"Retsba Ref {i+1}", use_column_width=True)
                    
                    if len(retsba_ref_images) > 2:
                        st.caption(f"+ {len(retsba_ref_images) - 2} more Retsba images")
                
                # Reload Retsba button
                if st.button("🔄 Reload Retsba References", key="reload_retsba"):
                    SessionManager.load_retsba_reference_images_from_folder()
                    st.rerun()
            else:
                st.info("📂 No Retsba reference images found.")
                st.caption(f"Add Retsba images to: `{retsba_ref_info['folder_path']}`")
                
                if st.button("🔄 Check for Retsba Images", key="check_retsba"):
                    SessionManager.load_retsba_reference_images_from_folder()
                    st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Generate button
        if st.button("🌟 Generate ALF & Retsba Adventure", key="generate_retsba_btn"):
            current_prompt = SessionManager.get_current_prompt()
            if current_prompt.strip():
                is_valid, error_msg = validate_prompt_length(current_prompt)
                if is_valid:
                    SessionManager.navigate_to_retsba_generating()
                    st.rerun()
                else:
                    st.error(error_msg)
            else:
                st.warning("You must describe the villainous adventure to summon ALF and Retsba...")