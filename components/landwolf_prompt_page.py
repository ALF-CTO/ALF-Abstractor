"""
Landwolf Prompt Page Component for ALF Abstractor
Where users craft prompts for ALF and Landwolf the Hairy Wolf crypto meme adventures
"""

import streamlit as st
from components.styles import load_alf_css, create_title, create_mystical_text
from utils.helpers import validate_prompt_length
from utils.session_manager import SessionManager
from config import UI_TEXT

# Landwolf-specific prompt components (crypto pack/wolf themes)
LANDWOLF_PROMPT_OBJECTS = [
    "ALF and Landwolf howling at the crypto moon together",
    "ALF and Landwolf pack-hunting for legendary altcoins",
    "ALF and Landwolf leading the wolf pack to financial freedom",
    "ALF and Landwolf guarding their crypto treasure in forest vaults",
    "ALF and Landwolf teaching pack strategies for DeFi protocols",
    "ALF and Landwolf prowling through blockchain wilderness",
    "ALF and Landwolf forming an unstoppable crypto alliance",
    "ALF and Landwolf building hairy wolf NFT empires",
    "ALF and Landwolf diamond-paw hodling through market storms",
    "ALF and Landwolf creating legendary pack memes",
    "ALF and Landwolf establishing crypto territories in the metaverse",
    "ALF and Landwolf unleashing wild forest wisdom on trading floors",
    "ALF and Landwolf forming the ultimate predator-prey crypto team",
    "ALF and Landwolf defending their pack's digital assets"
]

LANDWOLF_PROMPT_SETTINGS = [
    "in a moonlit crypto forest",
    "among howling pack celebrations",
    "in a wild blockchain wilderness", 
    "within ancient forest trading posts",
    "surrounded by loyal wolf pack members",
    "in a legendary crypto den",
    "among moonbeam-powered mining rigs",
    "in a pack-hunting DeFi paradise",
    "within wild forest NFT galleries",
    "in a hairy wolf meme sanctuary",
    "surrounded by legendary pack energy",
    "in a moon-howling crypto realm"
]

LANDWOLF_PROMPT_EMOTIONS = [
    "fiercely pack-minded and loyal",
    "wildly confident and legendary",
    "pack-leader strong and determined",
    "hairy-wolf proud and crypto-wise",
    "legendarily fierce and diamond-pawed",
    "pack-hunting focused and strategic",
    "wildly crypto-native and moon-bound",
    "forest-wise and blockchain-savvy",
    "fierce-howling and community-driven",
    "legendarily hairy and crypto-alpha"
]

def generate_random_landwolf_prompt():
    """Generate a random prompt for ALF and Landwolf"""
    import random
    
    obj = random.choice(LANDWOLF_PROMPT_OBJECTS)
    setting = random.choice(LANDWOLF_PROMPT_SETTINGS)
    emotion = random.choice(LANDWOLF_PROMPT_EMOTIONS)
    
    return f"{obj} {setting}, both characters are {emotion}"

def mix_landwolf_prompt_components():
    """Mix different Landwolf prompt components"""
    import random
    
    # Take random components
    obj1 = random.choice(LANDWOLF_PROMPT_OBJECTS)
    obj2 = random.choice(LANDWOLF_PROMPT_OBJECTS)
    setting = random.choice(LANDWOLF_PROMPT_SETTINGS)
    emotion = random.choice(LANDWOLF_PROMPT_EMOTIONS)
    
    # Create mixed prompt
    base = obj1.split(" together")[0] if " together" in obj1 else obj1
    return f"{base} and creating legendary pack crypto magic {setting}, both {emotion}"

def render_landwolf_prompt_page():
    """Render the Landwolf prompt input page"""
    load_alf_css()
    
    st.markdown(
        create_title("🐊🐺 ALF & Landwolf Pack Adventures", "page-header"), 
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        # Description text
        st.markdown(
            create_mystical_text("Describe the hairy wolf crypto adventure ALF and Landwolf will create..."), 
            unsafe_allow_html=True
        )
        
        # Show Landwolf info
        st.success("🐺 **Landwolf** is one of the leading meme characters in Crypto - a legendary hairy wolf who brings wild pack energy to blockchain adventures!")
        
        # Main prompt input
        current_prompt = SessionManager.get_current_prompt()
        prompt = st.text_area(
            "ALF & Landwolf Pack Adventure Prompt",
            value=current_prompt,
            placeholder="e.g., ALF and Landwolf howling at the crypto moon together in a moonlit crypto forest, both fiercely pack-minded and loyal",
            height=100,
            key="landwolf_prompt",
            label_visibility="collapsed"
        )
        
        # Update session state with current prompt
        if prompt != current_prompt:
            SessionManager.set_current_prompt(prompt)
        
        # Button row for prompt generation
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            if st.button("🎲 Random Pack Adventure"):
                random_prompt = generate_random_landwolf_prompt()
                SessionManager.set_current_prompt(random_prompt)
                st.rerun()
        
        with col_b:
            if st.button("🌀 Mix Wolf Adventure"):
                mixed_prompt = mix_landwolf_prompt_components()
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
        
        # Reference images section - show both ALF and Landwolf references
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
            st.markdown("### 🐺 Landwolf Reference Images")
            
            landwolf_ref_info = SessionManager.get_landwolf_reference_images_info()
            landwolf_ref_images = SessionManager.get_landwolf_reference_images()
            
            if landwolf_ref_info["image_count"] > 0:
                st.markdown(f"📁 **{landwolf_ref_info['image_count']} Landwolf images loaded**")
                
                # Display Landwolf reference images
                if landwolf_ref_images:
                    for i, img in enumerate(landwolf_ref_images[:2]):  # Show first 2 Landwolf images
                        st.image(img, caption=f"Landwolf Ref {i+1}", use_column_width=True)
                    
                    if len(landwolf_ref_images) > 2:
                        st.caption(f"+ {len(landwolf_ref_images) - 2} more Landwolf images")
                
                # Reload Landwolf button
                if st.button("🔄 Reload Landwolf References", key="reload_landwolf"):
                    SessionManager.load_landwolf_reference_images_from_folder()
                    st.rerun()
            else:
                st.info("📂 No Landwolf reference images found.")
                st.caption(f"Add Landwolf images to: `{landwolf_ref_info['folder_path']}`")
                
                if st.button("🔄 Check for Landwolf Images", key="check_landwolf"):
                    SessionManager.load_landwolf_reference_images_from_folder()
                    st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Generate button
        if st.button("🌟 Generate ALF & Landwolf Adventure", key="generate_landwolf_btn"):
            current_prompt = SessionManager.get_current_prompt()
            if current_prompt.strip():
                is_valid, error_msg = validate_prompt_length(current_prompt)
                if is_valid:
                    SessionManager.navigate_to_landwolf_generating()
                    st.rerun()
                else:
                    st.error(error_msg)
            else:
                st.warning("You must describe the hairy wolf crypto adventure to summon ALF and Landwolf...")