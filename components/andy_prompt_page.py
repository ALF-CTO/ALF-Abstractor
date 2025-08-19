"""
Andy Prompt Page Component for ALF Abstractor
Where users craft prompts for ALF and Andy the Yellow Guy crypto meme adventures
"""

import streamlit as st
from components.styles import load_alf_css, create_title, create_mystical_text
from utils.helpers import validate_prompt_length
from utils.session_manager import SessionManager
from config import UI_TEXT

# Andy-specific prompt components (yellow/sunshine/optimistic crypto themes)
ANDY_PROMPT_OBJECTS = [
    "ALF and Andy radiating bright yellow crypto energy together",
    "ALF and Andy spreading sunshine vibes while trading crypto",
    "ALF and Andy building golden crypto empires with optimism",
    "ALF and Andy painting the blockchain with bright yellow wisdom",
    "ALF and Andy creating sunshine-powered DeFi protocols",
    "ALF and Andy illuminating dark crypto markets with yellow light",
    "ALF and Andy forming the most optimistic crypto partnership",
    "ALF and Andy building radiant yellow NFT galleries",
    "ALF and Andy diamond-hand hodling with sunny confidence",
    "ALF and Andy creating the brightest crypto memes",
    "ALF and Andy establishing golden territories in the metaverse",
    "ALF and Andy unleashing yellow wisdom on trading floors",
    "ALF and Andy forming the ultimate optimistic crypto duo",
    "ALF and Andy defending their sunny digital assets"
]

ANDY_PROMPT_SETTINGS = [
    "in a sunlit crypto paradise",
    "among golden ray celebrations",
    "in a bright yellow blockchain realm", 
    "within luminous sunshine trading posts",
    "surrounded by radiant yellow energy",
    "in a legendary sunny crypto haven",
    "among sunbeam-powered mining rigs",
    "in a sunshine-filled DeFi wonderland",
    "within bright yellow NFT galleries",
    "in a glowing yellow meme sanctuary",
    "surrounded by optimistic golden vibes",
    "in a sun-kissed crypto kingdom"
]

ANDY_PROMPT_EMOTIONS = [
    "radiantly optimistic and cheerful",
    "brightly confident and sunny",
    "golden-hearted and determined",
    "sunshine-bright and crypto-wise",
    "luminously positive and diamond-handed",
    "sunshine-focused and strategic",
    "brilliantly crypto-native and uplifting",
    "golden-wise and blockchain-savvy",
    "bright-glowing and community-minded",
    "radiantly yellow and crypto-optimistic"
]

def generate_random_andy_prompt():
    """Generate a random prompt for ALF and Andy"""
    import random
    
    obj = random.choice(ANDY_PROMPT_OBJECTS)
    setting = random.choice(ANDY_PROMPT_SETTINGS)
    emotion = random.choice(ANDY_PROMPT_EMOTIONS)
    
    return f"{obj} {setting}, both characters are {emotion}"

def mix_andy_prompt_components():
    """Mix different Andy prompt components"""
    import random
    
    # Take random components
    obj1 = random.choice(ANDY_PROMPT_OBJECTS)
    obj2 = random.choice(ANDY_PROMPT_OBJECTS)
    setting = random.choice(ANDY_PROMPT_SETTINGS)
    emotion = random.choice(ANDY_PROMPT_EMOTIONS)
    
    # Create mixed prompt
    base = obj1.split(" together")[0] if " together" in obj1 else obj1
    return f"{base} and creating radiant yellow crypto magic {setting}, both {emotion}"

def render_andy_prompt_page():
    """Render the Andy prompt input page"""
    load_alf_css()
    
    st.markdown(
        create_title("🐊🟡 ALF & Andy Sunshine Adventures", "page-header"), 
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        # Description text
        st.markdown(
            create_mystical_text("Describe the bright yellow crypto adventure ALF and Andy will create..."), 
            unsafe_allow_html=True
        )
        
        # Show Andy info
        st.success("🟡 **Andy** is one of the leading meme characters in Crypto - a radiant yellow guy who brings sunshine optimism to blockchain adventures!")
        
        # Main prompt input
        current_prompt = SessionManager.get_current_prompt()
        prompt = st.text_area(
            "ALF & Andy Sunshine Adventure Prompt",
            value=current_prompt,
            placeholder="e.g., ALF and Andy radiating bright yellow crypto energy together in a sunlit crypto paradise, both radiantly optimistic and cheerful",
            height=100,
            key="andy_prompt",
            label_visibility="collapsed"
        )
        
        # Update session state with current prompt
        if prompt != current_prompt:
            SessionManager.set_current_prompt(prompt)
        
        # Button row for prompt generation
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            if st.button("🎲 Random Sunshine Adventure"):
                random_prompt = generate_random_andy_prompt()
                SessionManager.set_current_prompt(random_prompt)
                st.rerun()
        
        with col_b:
            if st.button("🌀 Mix Yellow Adventure"):
                mixed_prompt = mix_andy_prompt_components()
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
        
        # Reference images section - show both ALF and Andy references
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
            st.markdown("### 🟡 Andy Reference Images")
            
            andy_ref_info = SessionManager.get_andy_reference_images_info()
            andy_ref_images = SessionManager.get_andy_reference_images()
            
            if andy_ref_info["image_count"] > 0:
                st.markdown(f"📁 **{andy_ref_info['image_count']} Andy images loaded**")
                
                # Display Andy reference images
                if andy_ref_images:
                    for i, img in enumerate(andy_ref_images[:2]):  # Show first 2 Andy images
                        st.image(img, caption=f"Andy Ref {i+1}", use_column_width=True)
                    
                    if len(andy_ref_images) > 2:
                        st.caption(f"+ {len(andy_ref_images) - 2} more Andy images")
                
                # Reload Andy button
                if st.button("🔄 Reload Andy References", key="reload_andy"):
                    SessionManager.load_andy_reference_images_from_folder()
                    st.rerun()
            else:
                st.info("📂 No Andy reference images found.")
                st.caption(f"Add Andy images to: `{andy_ref_info['folder_path']}`")
                
                if st.button("🔄 Check for Andy Images", key="check_andy"):
                    SessionManager.load_andy_reference_images_from_folder()
                    st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Generate button
        if st.button("🌟 Generate ALF & Andy Adventure", key="generate_andy_btn"):
            current_prompt = SessionManager.get_current_prompt()
            if current_prompt.strip():
                is_valid, error_msg = validate_prompt_length(current_prompt)
                if is_valid:
                    SessionManager.navigate_to_andy_generating()
                    st.rerun()
                else:
                    st.error(error_msg)
            else:
                st.warning("You must describe the bright yellow crypto adventure to summon ALF and Andy...")