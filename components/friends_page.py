"""
Alf and Friends Page Component
A dedicated page for generating images of ALF with his friends
"""

import streamlit as st
from components.styles import load_alf_css, create_title, create_subtitle, create_mystical_text
from utils.session_manager import SessionManager
from config import UI_TEXT

# Friends configuration
FRIENDS = {
    "polly": {
        "name": "Polly",
        "description": "A friendly pink penguin",
        "color": "pink",
        "species": "penguin",
        "personality": "cheerful and playful",
        "emoji": "🐧"
    },
    "abster": {
        "name": "Abster",
        "description": "The Green Penguin of Abstract",
        "color": "green",
        "species": "penguin",
        "personality": "thoughtful and artistic",
        "emoji": "🐧"
    },
    "gooner": {
        "name": "GOONER",
        "description": "The bluest Penguin there is",
        "color": "blue",
        "species": "penguin",
        "personality": "energetic and blue",
        "emoji": "🐧"
    },
    "retsba": {
        "name": "Retsba",
        "description": "The villain of Abstract",
        "color": "red",
        "species": "penguin",
        "personality": "villainous and cunning",
        "emoji": "🐧"
    },
    "beary": {
        "name": "Beary",
        "description": "Number 1 prankster in abstract chain",
        "color": "brown",
        "species": "bear",
        "personality": "playful and mischievous",
        "emoji": "🐻"
    },
    "god": {
        "name": "GOD",
        "description": "The Dyslexic Dog in Abstract",
        "color": "golden",
        "species": "dog",
        "personality": "dyslexic and golden-hearted",
        "emoji": "🐕"
    },
    "pepe": {
        "name": "Pepe",
        "description": "One of the leading meme characters in Crypto",
        "color": "green",
        "species": "frog",
        "personality": "legendary and memetic",
        "emoji": "🐸"
    },
    "landwolf": {
        "name": "Landwolf",
        "description": "One of the leading meme characters in Crypto",
        "color": "hairy",
        "species": "wolf",
        "personality": "fierce and pack-minded",
        "emoji": "🐺"
    },
    "andy": {
        "name": "Andy",
        "description": "One of the leading meme characters in Crypto",
        "color": "yellow",
        "species": "guy",
        "personality": "optimistic and radiant",
        "emoji": "🟡"
    },
    "brett": {
        "name": "Brett",
        "description": "One of the leading meme characters in Crypto",
        "color": "blue",
        "species": "guy",
        "personality": "strategic and confident",
        "emoji": "🔵"
    }
}

# Friends are now handled by dedicated page flows

def render_friends_page():
    """Render the dedicated Alf and Friends page"""
    load_alf_css()
    
    # Page header
    st.markdown(
        create_title("🐊👫 ALF and Friends", "page-header"), 
        unsafe_allow_html=True
    )
    
    st.markdown(
        create_subtitle("Choose a friend to join ALF in his digital adventures"), 
        unsafe_allow_html=True
    )
    
    # Create main layout
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown(
            create_mystical_text("Select one of ALF's companions for your image generation..."), 
            unsafe_allow_html=True
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Friends selection with individual buttons
        st.markdown("### 🎭 Choose ALF's Friend:")
        
        # Create buttons for each friend
        for friend_key, friend_data in FRIENDS.items():
            col_a, col_b, col_c = st.columns([1, 2, 1])
            with col_b:
                friend_button_text = f"{friend_data['emoji']} {friend_data['name']} - {friend_data['description']}"
                if st.button(friend_button_text, key=f"select_{friend_key}"):
                    # Navigate directly to the friend's dedicated page flow
                    if friend_key == "polly":
                        SessionManager.navigate_to_polly_prompt()
                        st.rerun()
                    elif friend_key == "abster":
                        SessionManager.navigate_to_abster_prompt()
                        st.rerun()
                    elif friend_key == "gooner":
                        SessionManager.navigate_to_gooner_prompt()
                        st.rerun()
                    elif friend_key == "retsba":
                        SessionManager.navigate_to_retsba_prompt()
                        st.rerun()
                    elif friend_key == "beary":
                        SessionManager.navigate_to_beary_prompt()
                        st.rerun()
                    elif friend_key == "god":
                        SessionManager.navigate_to_god_prompt()
                        st.rerun()
                    elif friend_key == "pepe":
                        SessionManager.navigate_to_pepe_prompt()
                        st.rerun()
                    elif friend_key == "landwolf":
                        SessionManager.navigate_to_landwolf_prompt()
                        st.rerun()
                    elif friend_key == "andy":
                        SessionManager.navigate_to_andy_prompt()
                        st.rerun()
                    elif friend_key == "brett":
                        SessionManager.navigate_to_brett_prompt()
                        st.rerun()
        
        st.info("👆 Click on a friend above to start creating adventures together!")
        
        # Navigation buttons
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
        
        col_nav1, col_nav2, col_nav3 = st.columns(3)
        
        with col_nav1:
            if st.button("🔙 Back to Landing", key="back_to_landing"):
                SessionManager.set_page("landing")
                st.rerun()
        
        with col_nav2:
            if st.button("🌀 Solo ALF Images", key="go_to_prompt"):
                SessionManager.navigate_to_prompt()
                st.rerun()
        
        with col_nav3:
            # Empty column for spacing
            pass