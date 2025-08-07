"""
GOD Prompt Page Component for ALF Abstractor
Where users craft prompts for ALF and GOD the Golden Dog dyslexic adventures
"""

import streamlit as st
from components.styles import load_alf_css, create_title, create_mystical_text
from utils.helpers import validate_prompt_length
from utils.session_manager import SessionManager
from config import UI_TEXT

# GOD-specific prompt components (dyslexic/golden themes)
GOD_PROMPT_OBJECTS = [
    "ALF and GOD playing with backwards letters together",
    "ALF and GOD spelling words in mixed-up but beautiful ways",
    "ALF and GOD chasing dyslexic butterflies through golden gardens",
    "ALF and GOD creating art with scrambled letter blocks",
    "ALF and GOD reading upside-down books in a golden library",
    "ALF and GOD writing poetry with letters floating in reverse",
    "ALF and GOD solving word puzzles in golden dimensions",
    "ALF and GOD teaching each other about beautiful spelling mistakes",
    "ALF and GOD dancing with backwards alphabet letters",
    "ALF and GOD painting with golden, mixed-up words",
    "ALF and GOD exploring a world where letters float freely",
    "ALF and GOD creating dyslexic masterpieces together",
    "ALF and GOD organizing golden letter storms",
    "ALF and GOD building words that spell backwards magic"
]

GOD_PROMPT_SETTINGS = [
    "in a golden library with backwards books",
    "among floating mixed-up letters",
    "in a dyslexic classroom of wonder", 
    "within a golden alphabet storm",
    "surrounded by scrambled word clouds",
    "in a spelling bee dimension",
    "among golden letter rain",
    "in a reversed-reading sanctuary",
    "within mixed-up message bubbles",
    "in a golden world of word art",
    "surrounded by beautiful spelling chaos",
    "in a dyslexic paradise realm"
]

GOD_PROMPT_EMOTIONS = [
    "happily confused but determined",
    "joyfully mixing up words",
    "golden and slightly puzzled",
    "cheerfully dyslexic and proud",
    "warmly confused but loving",
    "playfully scrambling letters",
    "golden-hearted and mixed-up",
    "beautifully backwards thinking",
    "lovingly linguistic chaos",
    "bright and dyslexically creative"
]

def generate_random_god_prompt():
    """Generate a random prompt for ALF and GOD"""
    import random
    
    obj = random.choice(GOD_PROMPT_OBJECTS)
    setting = random.choice(GOD_PROMPT_SETTINGS)
    emotion = random.choice(GOD_PROMPT_EMOTIONS)
    
    return f"{obj} {setting}, both characters are {emotion}"

def mix_god_prompt_components():
    """Mix different GOD prompt components"""
    import random
    
    # Take random components
    obj1 = random.choice(GOD_PROMPT_OBJECTS)
    obj2 = random.choice(GOD_PROMPT_OBJECTS)
    setting = random.choice(GOD_PROMPT_SETTINGS)
    emotion = random.choice(GOD_PROMPT_EMOTIONS)
    
    # Create mixed prompt
    base = obj1.split(" together")[0] if " together" in obj1 else obj1
    return f"{base} and creating golden dyslexic magic {setting}, both {emotion}"

def render_god_prompt_page():
    """Render the GOD prompt input page"""
    load_alf_css()
    
    st.markdown(
        create_title("🐊🐕 ALF & GOD Dyslexic Adventures", "page-header"), 
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        # Description text
        st.markdown(
            create_mystical_text("Describe the dyslexic adventure ALF and GOD will experience..."), 
            unsafe_allow_html=True
        )
        
        # Show GOD info
        st.success("🐕 **GOD** is the Dyslexic Dog in Abstract - a golden retriever who mixes up letters and words in charming, beautiful ways!")
        
        # Main prompt input
        current_prompt = SessionManager.get_current_prompt()
        prompt = st.text_area(
            "ALF & GOD Dyslexic Adventure Prompt",
            value=current_prompt,
            placeholder="e.g., ALF and GOD playing with backwards letters together in a golden library with backwards books, both happily confused but determined",
            height=100,
            key="god_prompt",
            label_visibility="collapsed"
        )
        
        # Update session state with current prompt
        if prompt != current_prompt:
            SessionManager.set_current_prompt(prompt)
        
        # Button row for prompt generation
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            if st.button("🎲 Random Dyslexic Adventure"):
                random_prompt = generate_random_god_prompt()
                SessionManager.set_current_prompt(random_prompt)
                st.rerun()
        
        with col_b:
            if st.button("🌀 Mix Dyslexic Adventure"):
                mixed_prompt = mix_god_prompt_components()
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
        
        # Reference images section - show both ALF and GOD references
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
            st.markdown("### 🐕 GOD Reference Images")
            
            god_ref_info = SessionManager.get_god_reference_images_info()
            god_ref_images = SessionManager.get_god_reference_images()
            
            if god_ref_info["image_count"] > 0:
                st.markdown(f"📁 **{god_ref_info['image_count']} GOD images loaded**")
                
                # Display GOD reference images
                if god_ref_images:
                    for i, img in enumerate(god_ref_images[:2]):  # Show first 2 GOD images
                        st.image(img, caption=f"GOD Ref {i+1}", use_column_width=True)
                    
                    if len(god_ref_images) > 2:
                        st.caption(f"+ {len(god_ref_images) - 2} more GOD images")
                
                # Reload GOD button
                if st.button("🔄 Reload GOD References", key="reload_god"):
                    SessionManager.load_god_reference_images_from_folder()
                    st.rerun()
            else:
                st.info("📂 No GOD reference images found.")
                st.caption(f"Add GOD images to: `{god_ref_info['folder_path']}`")
                
                if st.button("🔄 Check for GOD Images", key="check_god"):
                    SessionManager.load_god_reference_images_from_folder()
                    st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Generate button
        if st.button("🌟 Generate ALF & GOD Adventure", key="generate_god_btn"):
            current_prompt = SessionManager.get_current_prompt()
            if current_prompt.strip():
                is_valid, error_msg = validate_prompt_length(current_prompt)
                if is_valid:
                    SessionManager.navigate_to_god_generating()
                    st.rerun()
                else:
                    st.error(error_msg)
            else:
                st.warning("You must describe the dyslexic adventure to summon ALF and GOD...")