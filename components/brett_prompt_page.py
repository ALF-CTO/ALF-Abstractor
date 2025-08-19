"""
Brett Prompt Page Component for ALF Abstractor
Where users craft prompts for ALF and Brett the Blue Guy crypto meme adventures
"""

import streamlit as st
from components.styles import load_alf_css, create_title, create_mystical_text
from utils.helpers import validate_prompt_length
from utils.session_manager import SessionManager
from config import UI_TEXT

# Brett-specific prompt components (blue/ocean/strategic crypto themes)
BRETT_PROMPT_OBJECTS = [
    "ALF and Brett radiating deep blue crypto energy together",
    "ALF and Brett analyzing market trends with crypto precision",
    "ALF and Brett building oceanic crypto empires with strategy",
    "ALF and Brett painting the blockchain with cool blue wisdom",
    "ALF and Brett creating wave-powered DeFi protocols",
    "ALF and Brett illuminating volatile crypto markets with blue light",
    "ALF and Brett forming the most strategic crypto partnership",
    "ALF and Brett building electric blue NFT galleries",
    "ALF and Brett diamond-hand hodling with cool confidence",
    "ALF and Brett creating the deepest crypto analysis",
    "ALF and Brett establishing blue territories in the metaverse",
    "ALF and Brett unleashing ocean wisdom on trading floors",
    "ALF and Brett forming the ultimate strategic crypto duo",
    "ALF and Brett defending their cool digital assets"
]

BRETT_PROMPT_SETTINGS = [
    "in a deep blue crypto ocean",
    "among electric wave celebrations",
    "in a cool blue blockchain realm", 
    "within strategic ocean trading posts",
    "surrounded by flowing blue energy",
    "in a legendary deep crypto haven",
    "among wave-powered mining rigs",
    "in a blue-filled DeFi analysis center",
    "within electric blue NFT galleries",
    "in a flowing blue meme sanctuary",
    "surrounded by strategic ocean vibes",
    "in a wave-kissed crypto kingdom"
]

BRETT_PROMPT_EMOTIONS = [
    "strategically confident and cool",
    "deeply analytical and blue",
    "ocean-hearted and determined",
    "blue-bright and crypto-wise",
    "electrically strategic and diamond-handed",
    "wave-focused and analytical",
    "brilliantly crypto-native and flowing",
    "ocean-wise and blockchain-savvy",
    "deep-flowing and community-minded",
    "radiantly blue and crypto-strategic"
]

def generate_random_brett_prompt():
    """Generate a random prompt for ALF and Brett"""
    import random
    
    obj = random.choice(BRETT_PROMPT_OBJECTS)
    setting = random.choice(BRETT_PROMPT_SETTINGS)
    emotion = random.choice(BRETT_PROMPT_EMOTIONS)
    
    return f"{obj} {setting}, both characters are {emotion}"

def mix_brett_prompt_components():
    """Mix different Brett prompt components"""
    import random
    
    # Take random components
    obj1 = random.choice(BRETT_PROMPT_OBJECTS)
    obj2 = random.choice(BRETT_PROMPT_OBJECTS)
    setting = random.choice(BRETT_PROMPT_SETTINGS)
    emotion = random.choice(BRETT_PROMPT_EMOTIONS)
    
    # Create mixed prompt
    base = obj1.split(" together")[0] if " together" in obj1 else obj1
    return f"{base} and creating electric blue crypto magic {setting}, both {emotion}"

def render_brett_prompt_page():
    """Render the Brett prompt input page"""
    load_alf_css()
    
    st.markdown(
        create_title("🐊🔵 ALF & Brett Ocean Adventures", "page-header"), 
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        # Description text
        st.markdown(
            create_mystical_text("Describe the deep blue crypto adventure ALF and Brett will create..."), 
            unsafe_allow_html=True
        )
        
        # Show Brett info
        st.success("🔵 **Brett** is one of the leading meme characters in Crypto - a strategic blue guy who brings cool confidence to blockchain adventures!")
        
        # Main prompt input
        current_prompt = SessionManager.get_current_prompt()
        prompt = st.text_area(
            "ALF & Brett Ocean Adventure Prompt",
            value=current_prompt,
            placeholder="e.g., ALF and Brett radiating deep blue crypto energy together in a deep blue crypto ocean, both strategically confident and cool",
            height=100,
            key="brett_prompt",
            label_visibility="collapsed"
        )
        
        # Update session state with current prompt
        if prompt != current_prompt:
            SessionManager.set_current_prompt(prompt)
        
        # Button row for prompt generation
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            if st.button("🎲 Random Ocean Adventure"):
                random_prompt = generate_random_brett_prompt()
                SessionManager.set_current_prompt(random_prompt)
                st.rerun()
        
        with col_b:
            if st.button("🌀 Mix Blue Adventure"):
                mixed_prompt = mix_brett_prompt_components()
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
        
        # Reference images section - show both ALF and Brett references
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
            st.markdown("### 🔵 Brett Reference Images")
            
            brett_ref_info = SessionManager.get_brett_reference_images_info()
            brett_ref_images = SessionManager.get_brett_reference_images()
            
            if brett_ref_info["image_count"] > 0:
                st.markdown(f"📁 **{brett_ref_info['image_count']} Brett images loaded**")
                
                # Display Brett reference images
                if brett_ref_images:
                    for i, img in enumerate(brett_ref_images[:2]):  # Show first 2 Brett images
                        st.image(img, caption=f"Brett Ref {i+1}", use_column_width=True)
                    
                    if len(brett_ref_images) > 2:
                        st.caption(f"+ {len(brett_ref_images) - 2} more Brett images")
                
                # Reload Brett button
                if st.button("🔄 Reload Brett References", key="reload_brett"):
                    SessionManager.load_brett_reference_images_from_folder()
                    st.rerun()
            else:
                st.info("📂 No Brett reference images found.")
                st.caption(f"Add Brett images to: `{brett_ref_info['folder_path']}`")
                
                if st.button("🔄 Check for Brett Images", key="check_brett"):
                    SessionManager.load_brett_reference_images_from_folder()
                    st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Generate button
        if st.button("🌟 Generate ALF & Brett Adventure", key="generate_brett_btn"):
            current_prompt = SessionManager.get_current_prompt()
            if current_prompt.strip():
                is_valid, error_msg = validate_prompt_length(current_prompt)
                if is_valid:
                    SessionManager.navigate_to_brett_generating()
                    st.rerun()
                else:
                    st.error(error_msg)
            else:
                st.warning("You must describe the deep blue crypto adventure to summon ALF and Brett...")