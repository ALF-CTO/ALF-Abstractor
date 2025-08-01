"""
Polly Prompt Page Component for ALF Abstractor
Where users craft prompts for ALF and Polly adventures
"""

import streamlit as st
from components.styles import load_alf_css, create_title, create_mystical_text
from utils.helpers import validate_prompt_length
from utils.session_manager import SessionManager
from config import UI_TEXT

# Polly-specific prompt components
POLLY_PROMPT_OBJECTS = [
    "nowy building a snowman together",
    "ALF and Polly sliding on ice together",
    "ALF and Polly sharing fish in the digital swamp",
    "ALF and Polly dancing on rainbow ice",
    "ALF and Polly exploring a magical ice cave",
    "ALF and Polly sitting by a frozen digital lake",
    "ALF and Polly playing in pink and green snow",
    "ALF and Polly watching aurora lights",
    "ALF and Polly on a floating ice platform",
    "ALF and Polly creating art with ice crystals",
    "ALF and Polly in a cozy igloo",
    "ALF and Polly racing through snow drifts",
    "ALF and Polly sharing warm cocoa",
    "ALF and Polly making snow angels"
]

POLLY_PROMPT_SETTINGS = [
    "in a magical ice castle",
    "surrounded by pink snow clouds",
    "in a penguin village",
    "on a floating iceberg",
    "in a winter wonderland",
    "among crystalline formations",
    "in a frosty digital realm",
    "on a frozen rainbow bridge",
    "in an enchanted arctic forest",
    "within aurora light patterns",
    "on a pink ice mountain",
    "in a cozy snow cabin"
]

POLLY_PROMPT_EMOTIONS = [
    "joyful and playful",
    "warm and friendly", 
    "excited and adventurous",
    "peaceful and content",
    "curious and exploring",
    "cheerful and laughing",
    "cozy and comfortable",
    "magical and wondering",
    "happy and carefree",
    "gentle and caring"
]

def generate_random_polly_prompt():
    """Generate a random prompt for ALF and Polly"""
    import random
    
    obj = random.choice(POLLY_PROMPT_OBJECTS)
    setting = random.choice(POLLY_PROMPT_SETTINGS)
    emotion = random.choice(POLLY_PROMPT_EMOTIONS)
    
    return f"{obj} {setting}, both characters are {emotion}"

def mix_polly_prompt_components():
    """Mix different Polly prompt components"""
    import random
    
    # Take random components
    obj1 = random.choice(POLLY_PROMPT_OBJECTS)
    obj2 = random.choice(POLLY_PROMPT_OBJECTS)
    setting = random.choice(POLLY_PROMPT_SETTINGS)
    emotion = random.choice(POLLY_PROMPT_EMOTIONS)
    
    # Create mixed prompt
    base = obj1.split(" together")[0] if " together" in obj1 else obj1
    return f"{base} and having fun {setting}, both {emotion}"

def render_polly_prompt_page():
    """Render the Polly prompt input page"""
    load_alf_css()
    
    st.markdown(
        create_title("🐊🐧 ALF & Polly Adventures", "page-header"), 
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        # Description text
        st.markdown(
            create_mystical_text("Describe the magical adventure ALF and Polly will share..."), 
            unsafe_allow_html=True
        )
        
        # Show Polly info
        st.info("🐧 **Polly** is a cheerful pink penguin who loves adventures with ALF!")
        
        # Main prompt input
        current_prompt = SessionManager.get_current_prompt()
        prompt = st.text_area(
            "ALF & Polly Adventure Prompt",
            value=current_prompt,
            placeholder="e.g., ALF and Polly building an ice castle in a magical winter forest, both joyful and creative",
            height=100,
            key="polly_prompt",
            label_visibility="collapsed"
        )
        
        # Update session state with current prompt
        if prompt != current_prompt:
            SessionManager.set_current_prompt(prompt)
        
        # Button row for prompt generation
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            if st.button("🎲 Random Adventure"):
                random_prompt = generate_random_polly_prompt()
                SessionManager.set_current_prompt(random_prompt)
                st.rerun()
        
        with col_b:
            if st.button("🌀 Mix Adventure"):
                mixed_prompt = mix_polly_prompt_components()
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
        
        # Reference images section - show both ALF and Polly references
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
            st.markdown("### 🐧 Polly Reference Images")
            
            polly_ref_info = SessionManager.get_polly_reference_images_info()
            polly_ref_images = SessionManager.get_polly_reference_images()
            
            if polly_ref_info["image_count"] > 0:
                st.markdown(f"📁 **{polly_ref_info['image_count']} Polly images loaded**")
                
                # Display Polly reference images
                if polly_ref_images:
                    for i, img in enumerate(polly_ref_images[:2]):  # Show first 2 Polly images
                        st.image(img, caption=f"Polly Ref {i+1}", use_column_width=True)
                    
                    if len(polly_ref_images) > 2:
                        st.caption(f"+ {len(polly_ref_images) - 2} more Polly images")
                
                # Reload Polly button
                if st.button("🔄 Reload Polly References", key="reload_polly"):
                    SessionManager.load_polly_reference_images_from_folder()
                    st.rerun()
            else:
                st.info("📂 No Polly reference images found.")
                st.caption(f"Add Polly images to: `{polly_ref_info['folder_path']}`")
                
                if st.button("🔄 Check for Polly Images", key="check_polly"):
                    SessionManager.load_polly_reference_images_from_folder()
                    st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Generate button
        if st.button("🌟 Generate ALF & Polly Adventure", key="generate_polly_btn"):
            current_prompt = SessionManager.get_current_prompt()
            if current_prompt.strip():
                is_valid, error_msg = validate_prompt_length(current_prompt)
                if is_valid:
                    SessionManager.navigate_to_polly_generating()
                    st.rerun()
                else:
                    st.error(error_msg)
            else:
                st.warning("You must describe the adventure to summon ALF and Polly...")