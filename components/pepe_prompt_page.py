"""
Pepe Prompt Page Component for ALF Abstractor
Where users craft prompts for ALF and Pepe the Green Frog crypto meme adventures
"""

import streamlit as st
from components.styles import load_alf_css, create_title, create_mystical_text
from utils.helpers import validate_prompt_length
from utils.session_manager import SessionManager
from config import UI_TEXT

# Pepe-specific prompt components (crypto meme themes)
PEPE_PROMPT_OBJECTS = [
    "ALF and Pepe trading crypto on digital exchanges together",
    "ALF and Pepe hodling diamond hands through market volatility",
    "ALF and Pepe creating the most legendary meme magic",
    "ALF and Pepe surfing green crypto waves to the moon",
    "ALF and Pepe building decentralized meme empires",
    "ALF and Pepe stacking sats and rare digital artifacts",
    "ALF and Pepe launching rocket ships to crypto paradise",
    "ALF and Pepe minting NFTs in blockchain dimensions",
    "ALF and Pepe diamond-handing through bear markets",
    "ALF and Pepe creating viral memes that pump portfolios",
    "ALF and Pepe discovering hidden crypto treasures",
    "ALF and Pepe building meme-powered DeFi protocols",
    "ALF and Pepe celebrating bull runs with legendary energy",
    "ALF and Pepe turning rare pepes into digital gold"
]

PEPE_PROMPT_SETTINGS = [
    "in a digital crypto trading floor",
    "among floating Bitcoin symbols",
    "in a meme-powered blockchain dimension", 
    "within green candle chart patterns",
    "surrounded by diamond hand emojis",
    "in a DeFi yield farming paradise",
    "among rocket ship launch pads",
    "in an NFT marketplace wonderland",
    "within bull market celebration halls",
    "in a rare Pepe collection vault",
    "surrounded by legendary meme energy",
    "in a to-the-moon crypto realm"
]

PEPE_PROMPT_EMOTIONS = [
    "legendarily confident and bullish",
    "memetically powerful and iconic",
    "diamond-handed and determined",
    "crypto-wise and market-savvy",
    "legendarily meme-tier and epic",
    "bullishly optimistic about gains",
    "iconically frog-like and crypto-native",
    "moon-bound and rocket-fueled",
    "diamond-gripped and hodling strong",
    "legendarily dank and crypto-pilled"
]

def generate_random_pepe_prompt():
    """Generate a random prompt for ALF and Pepe"""
    import random
    
    obj = random.choice(PEPE_PROMPT_OBJECTS)
    setting = random.choice(PEPE_PROMPT_SETTINGS)
    emotion = random.choice(PEPE_PROMPT_EMOTIONS)
    
    return f"{obj} {setting}, both characters are {emotion}"

def mix_pepe_prompt_components():
    """Mix different Pepe prompt components"""
    import random
    
    # Take random components
    obj1 = random.choice(PEPE_PROMPT_OBJECTS)
    obj2 = random.choice(PEPE_PROMPT_OBJECTS)
    setting = random.choice(PEPE_PROMPT_SETTINGS)
    emotion = random.choice(PEPE_PROMPT_EMOTIONS)
    
    # Create mixed prompt
    base = obj1.split(" together")[0] if " together" in obj1 else obj1
    return f"{base} and creating legendary crypto memes {setting}, both {emotion}"

def render_pepe_prompt_page():
    """Render the Pepe prompt input page"""
    load_alf_css()
    
    st.markdown(
        create_title("🐊🐸 ALF & Pepe Crypto Meme Adventures", "page-header"), 
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        # Description text
        st.markdown(
            create_mystical_text("Describe the crypto meme adventure ALF and Pepe will create..."), 
            unsafe_allow_html=True
        )
        
        # Show Pepe info
        st.success("🐸 **Pepe** is one of the leading meme characters in Crypto - a legendary green frog who brings iconic meme energy to blockchain adventures!")
        
        # Main prompt input
        current_prompt = SessionManager.get_current_prompt()
        prompt = st.text_area(
            "ALF & Pepe Crypto Meme Adventure Prompt",
            value=current_prompt,
            placeholder="e.g., ALF and Pepe trading crypto on digital exchanges together in a meme-powered blockchain dimension, both legendarily confident and bullish",
            height=100,
            key="pepe_prompt",
            label_visibility="collapsed"
        )
        
        # Update session state with current prompt
        if prompt != current_prompt:
            SessionManager.set_current_prompt(prompt)
        
        # Button row for prompt generation
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            if st.button("🎲 Random Crypto Adventure"):
                random_prompt = generate_random_pepe_prompt()
                SessionManager.set_current_prompt(random_prompt)
                st.rerun()
        
        with col_b:
            if st.button("🌀 Mix Meme Adventure"):
                mixed_prompt = mix_pepe_prompt_components()
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
        
        # Reference images section - show both ALF and Pepe references
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
            st.markdown("### 🐸 Pepe Reference Images")
            
            pepe_ref_info = SessionManager.get_pepe_reference_images_info()
            pepe_ref_images = SessionManager.get_pepe_reference_images()
            
            if pepe_ref_info["image_count"] > 0:
                st.markdown(f"📁 **{pepe_ref_info['image_count']} Pepe images loaded**")
                
                # Display Pepe reference images
                if pepe_ref_images:
                    for i, img in enumerate(pepe_ref_images[:2]):  # Show first 2 Pepe images
                        st.image(img, caption=f"Pepe Ref {i+1}", use_column_width=True)
                    
                    if len(pepe_ref_images) > 2:
                        st.caption(f"+ {len(pepe_ref_images) - 2} more Pepe images")
                
                # Reload Pepe button
                if st.button("🔄 Reload Pepe References", key="reload_pepe"):
                    SessionManager.load_pepe_reference_images_from_folder()
                    st.rerun()
            else:
                st.info("📂 No Pepe reference images found.")
                st.caption(f"Add Pepe images to: `{pepe_ref_info['folder_path']}`")
                
                if st.button("🔄 Check for Pepe Images", key="check_pepe"):
                    SessionManager.load_pepe_reference_images_from_folder()
                    st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Generate button
        if st.button("🌟 Generate ALF & Pepe Adventure", key="generate_pepe_btn"):
            current_prompt = SessionManager.get_current_prompt()
            if current_prompt.strip():
                is_valid, error_msg = validate_prompt_length(current_prompt)
                if is_valid:
                    SessionManager.navigate_to_pepe_generating()
                    st.rerun()
                else:
                    st.error(error_msg)
            else:
                st.warning("You must describe the crypto meme adventure to summon ALF and Pepe...")