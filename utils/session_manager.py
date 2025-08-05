"""
Session Management for ALF Abstractor
Handles Streamlit session state management and navigation
"""

import streamlit as st
from typing import Any, Optional
from PIL import Image

from config import SESSION_KEYS, PAGES

class SessionManager:
    """Manages Streamlit session state for the ALF Abstractor application"""
    
    @staticmethod
    def initialize_session():
        """Initialize all required session state variables"""
        # Page navigation
        if SESSION_KEYS["PAGE"] not in st.session_state:
            st.session_state[SESSION_KEYS["PAGE"]] = PAGES["LANDING"]
        
        # Image data
        if SESSION_KEYS["GENERATED_IMAGE"] not in st.session_state:
            st.session_state[SESSION_KEYS["GENERATED_IMAGE"]] = None
        
        # Prompt data
        if SESSION_KEYS["CURRENT_PROMPT"] not in st.session_state:
            st.session_state[SESSION_KEYS["CURRENT_PROMPT"]] = ""
        
        # Image history for session
        if SESSION_KEYS["IMAGE_HISTORY"] not in st.session_state:
            st.session_state[SESSION_KEYS["IMAGE_HISTORY"]] = []
        
        # Reference images for ALF
        if SESSION_KEYS["REFERENCE_IMAGES"] not in st.session_state:
            st.session_state[SESSION_KEYS["REFERENCE_IMAGES"]] = []
        
        # Reference images for Polly
        if SESSION_KEYS["POLLY_REFERENCE_IMAGES"] not in st.session_state:
            st.session_state[SESSION_KEYS["POLLY_REFERENCE_IMAGES"]] = []
        
        # Reference images for Abster
        if SESSION_KEYS["ABSTER_REFERENCE_IMAGES"] not in st.session_state:
            st.session_state[SESSION_KEYS["ABSTER_REFERENCE_IMAGES"]] = []
        
        # Reference images for GOONER
        if SESSION_KEYS["GOONER_REFERENCE_IMAGES"] not in st.session_state:
            st.session_state[SESSION_KEYS["GOONER_REFERENCE_IMAGES"]] = []
        
        # Reference images for Retsba
        if SESSION_KEYS["RETSBA_REFERENCE_IMAGES"] not in st.session_state:
            st.session_state[SESSION_KEYS["RETSBA_REFERENCE_IMAGES"]] = []
    
    @staticmethod
    def get_current_page() -> str:
        """
        Get the current page from session state
        
        Returns:
            str: Current page identifier
        """
        return st.session_state.get(SESSION_KEYS["PAGE"], PAGES["LANDING"])
    
    @staticmethod
    def set_page(page: str):
        """
        Set the current page in session state
        
        Args:
            page (str): Page identifier to navigate to
        """
        if page in PAGES.values():
            st.session_state[SESSION_KEYS["PAGE"]] = page
        else:
            raise ValueError(f"Invalid page: {page}")
    
    @staticmethod
    def get_generated_image() -> Optional[Image.Image]:
        """
        Get the currently generated image from session state
        
        Returns:
            Optional[Image.Image]: Generated image or None
        """
        return st.session_state.get(SESSION_KEYS["GENERATED_IMAGE"])
    
    @staticmethod
    def set_generated_image(image: Optional[Image.Image]):
        """
        Set the generated image in session state
        
        Args:
            image (Optional[Image.Image]): Image to store
        """
        st.session_state[SESSION_KEYS["GENERATED_IMAGE"]] = image
    
    @staticmethod
    def get_current_prompt() -> str:
        """
        Get the current prompt from session state
        
        Returns:
            str: Current prompt text
        """
        return st.session_state.get(SESSION_KEYS["CURRENT_PROMPT"], "")
    
    @staticmethod
    def set_current_prompt(prompt: str):
        """
        Set the current prompt in session state
        
        Args:
            prompt (str): Prompt text to store
        """
        st.session_state[SESSION_KEYS["CURRENT_PROMPT"]] = prompt
    
    @staticmethod
    def get_api_key() -> str:
        """
        Get the API key from widget state
        
        Returns:
            str: API key from the text input widget
        """
        return st.session_state.get("api_key", "")
    
    @staticmethod
    def add_to_history(prompt: str, image: Image.Image):
        """
        Add a generated image and prompt to the session history
        
        Args:
            prompt (str): The prompt used
            image (Image.Image): The generated image
        """
        history = st.session_state.get(SESSION_KEYS["IMAGE_HISTORY"], [])
        history.append({
            "prompt": prompt,
            "image": image,
            "timestamp": st.session_state.get("generation_timestamp", 0)
        })
        
        # Keep only last 10 items to prevent memory issues
        if len(history) > 10:
            history = history[-10:]
        
        st.session_state[SESSION_KEYS["IMAGE_HISTORY"]] = history
    
    @staticmethod
    def get_history() -> list:
        """
        Get the image generation history
        
        Returns:
            list: History of generated images and prompts
        """
        return st.session_state.get(SESSION_KEYS["IMAGE_HISTORY"], [])
    
    @staticmethod
    def clear_session():
        """Clear all session data (except page navigation)"""
        current_page = SessionManager.get_current_page()
        
        # Clear all session data
        for key in SESSION_KEYS.values():
            if key in st.session_state:
                del st.session_state[key]
        
        # Reinitialize and restore page
        SessionManager.initialize_session()
        SessionManager.set_page(current_page)
    
    @staticmethod
    def reset_to_landing():
        """Reset session and return to landing page"""
        SessionManager.clear_session()
        SessionManager.set_page(PAGES["LANDING"])
    
    @staticmethod
    def navigate_to_friends():
        """Navigate to friends page"""
        SessionManager.set_page(PAGES["FRIENDS"])
    
    @staticmethod
    def navigate_to_prompt():
        """Navigate to prompt page"""
        SessionManager.set_page(PAGES["PROMPT"])
    
    @staticmethod
    def navigate_to_generating():
        """Navigate to generating page"""
        SessionManager.set_page(PAGES["GENERATING"])
    
    @staticmethod
    def navigate_to_result():
        """Navigate to result page"""
        SessionManager.set_page(PAGES["RESULT"])
    
    @staticmethod
    def navigate_to_polly_prompt():
        """Navigate to Polly prompt page"""
        SessionManager.set_page(PAGES["POLLY_PROMPT"])
    
    @staticmethod
    def navigate_to_polly_generating():
        """Navigate to Polly generating page"""
        SessionManager.set_page(PAGES["POLLY_GENERATING"])
    
    @staticmethod
    def navigate_to_polly_result():
        """Navigate to Polly result page"""
        SessionManager.set_page(PAGES["POLLY_RESULT"])
    
    @staticmethod
    def navigate_to_abster_prompt():
        """Navigate to Abster prompt page"""
        SessionManager.set_page(PAGES["ABSTER_PROMPT"])
    
    @staticmethod
    def navigate_to_abster_generating():
        """Navigate to Abster generating page"""
        SessionManager.set_page(PAGES["ABSTER_GENERATING"])
    
    @staticmethod
    def navigate_to_abster_result():
        """Navigate to Abster result page"""
        SessionManager.set_page(PAGES["ABSTER_RESULT"])
    
    @staticmethod
    def navigate_to_gooner_prompt():
        """Navigate to GOONER prompt page"""
        SessionManager.set_page(PAGES["GOONER_PROMPT"])
    
    @staticmethod
    def navigate_to_gooner_generating():
        """Navigate to GOONER generating page"""
        SessionManager.set_page(PAGES["GOONER_GENERATING"])
    
    @staticmethod
    def navigate_to_gooner_result():
        """Navigate to GOONER result page"""
        SessionManager.set_page(PAGES["GOONER_RESULT"])
    
    @staticmethod
    def navigate_to_retsba_prompt():
        """Navigate to Retsba prompt page"""
        SessionManager.set_page(PAGES["RETSBA_PROMPT"])
    
    @staticmethod
    def navigate_to_retsba_generating():
        """Navigate to Retsba generating page"""
        SessionManager.set_page(PAGES["RETSBA_GENERATING"])
    
    @staticmethod
    def navigate_to_retsba_result():
        """Navigate to Retsba result page"""
        SessionManager.set_page(PAGES["RETSBA_RESULT"])
    
    @staticmethod
    def has_generated_image() -> bool:
        """
        Check if there's a generated image in session
        
        Returns:
            bool: True if there's a generated image
        """
        return SessionManager.get_generated_image() is not None
    
    @staticmethod
    def has_prompt() -> bool:
        """
        Check if there's a current prompt in session
        
        Returns:
            bool: True if there's a current prompt
        """
        return bool(SessionManager.get_current_prompt().strip())
    
    @staticmethod
    def has_api_key() -> bool:
        """
        Check if there's an API key in the widget
        
        Returns:
            bool: True if there's an API key
        """
        return bool(SessionManager.get_api_key().strip())
    
    @staticmethod
    def get_reference_images() -> list:
        """
        Get the reference images from session state
        
        Returns:
            list: List of reference images
        """
        return st.session_state.get(SESSION_KEYS["REFERENCE_IMAGES"], [])
    
    @staticmethod
    def add_reference_image(image: Image.Image):
        """
        Add a reference image to the session
        
        Args:
            image (Image.Image): Reference image to add
        """
        ref_images = SessionManager.get_reference_images()
        ref_images.append(image)
        
        # Keep only last 5 reference images to prevent memory issues
        if len(ref_images) > 5:
            ref_images = ref_images[-5:]
            
        st.session_state[SESSION_KEYS["REFERENCE_IMAGES"]] = ref_images
    
    @staticmethod
    def clear_reference_images():
        """Clear all reference images from session"""
        st.session_state[SESSION_KEYS["REFERENCE_IMAGES"]] = []
    
    @staticmethod
    def has_reference_images() -> bool:
        """
        Check if there are reference images in session
        
        Returns:
            bool: True if there are reference images
        """
        return len(SessionManager.get_reference_images()) > 0
    
    @staticmethod
    def load_reference_images_from_folder():
        """Load reference images from the references folder into session state"""
        from utils.reference_loader import ReferenceImageLoader
        
        # Load images from the references folder
        loaded_images = ReferenceImageLoader.load_reference_images()
        
        # Extract just the images (not the filenames) for session storage
        images = [img for img, filename in loaded_images]
        
        # Store in session state
        st.session_state[SESSION_KEYS["REFERENCE_IMAGES"]] = images
        
        return len(images)
    
    @staticmethod
    def get_reference_images_info() -> dict:
        """
        Get information about reference images
        
        Returns:
            dict: Information about loaded reference images
        """
        from utils.reference_loader import ReferenceImageLoader
        return ReferenceImageLoader.get_reference_images_info()
    
    @staticmethod
    def get_polly_reference_images() -> list:
        """
        Get the Polly reference images from session state
        
        Returns:
            list: List of Polly reference images
        """
        return st.session_state.get(SESSION_KEYS["POLLY_REFERENCE_IMAGES"], [])
    
    @staticmethod
    def add_polly_reference_image(image: Image.Image):
        """
        Add a Polly reference image to the session
        
        Args:
            image (Image.Image): Polly reference image to add
        """
        ref_images = SessionManager.get_polly_reference_images()
        ref_images.append(image)
        
        # Keep only last 5 reference images to prevent memory issues
        if len(ref_images) > 5:
            ref_images = ref_images[-5:]
            
        st.session_state[SESSION_KEYS["POLLY_REFERENCE_IMAGES"]] = ref_images
    
    @staticmethod
    def clear_polly_reference_images():
        """Clear all Polly reference images from session"""
        st.session_state[SESSION_KEYS["POLLY_REFERENCE_IMAGES"]] = []
    
    @staticmethod
    def has_polly_reference_images() -> bool:
        """
        Check if there are Polly reference images in session
        
        Returns:
            bool: True if there are Polly reference images
        """
        return len(SessionManager.get_polly_reference_images()) > 0
    
    @staticmethod
    def load_polly_reference_images_from_folder():
        """Load Polly reference images from the references/polly folder into session state"""
        from utils.reference_loader import ReferenceImageLoader
        
        # Load images from the polly references folder
        loaded_images = ReferenceImageLoader.load_polly_reference_images()
        
        # Extract just the images (not the filenames) for session storage
        images = [img for img, filename in loaded_images]
        
        # Store in session state
        st.session_state[SESSION_KEYS["POLLY_REFERENCE_IMAGES"]] = images
        
        return len(images)
    
    @staticmethod
    def get_polly_reference_images_info() -> dict:
        """
        Get information about Polly reference images
        
        Returns:
            dict: Information about loaded Polly reference images
        """
        from utils.reference_loader import ReferenceImageLoader
        return ReferenceImageLoader.get_polly_reference_images_info()
    
    @staticmethod
    def get_abster_reference_images() -> list:
        """
        Get the Abster reference images from session state
        
        Returns:
            list: List of Abster reference images
        """
        return st.session_state.get(SESSION_KEYS["ABSTER_REFERENCE_IMAGES"], [])
    
    @staticmethod
    def add_abster_reference_image(image: Image.Image):
        """
        Add an Abster reference image to the session
        
        Args:
            image (Image.Image): Abster reference image to add
        """
        ref_images = SessionManager.get_abster_reference_images()
        ref_images.append(image)
        
        # Keep only last 5 reference images to prevent memory issues
        if len(ref_images) > 5:
            ref_images = ref_images[-5:]
            
        st.session_state[SESSION_KEYS["ABSTER_REFERENCE_IMAGES"]] = ref_images
    
    @staticmethod
    def clear_abster_reference_images():
        """Clear all Abster reference images from session"""
        st.session_state[SESSION_KEYS["ABSTER_REFERENCE_IMAGES"]] = []
    
    @staticmethod
    def has_abster_reference_images() -> bool:
        """
        Check if there are Abster reference images in session
        
        Returns:
            bool: True if there are Abster reference images
        """
        return len(SessionManager.get_abster_reference_images()) > 0
    
    @staticmethod
    def load_abster_reference_images_from_folder():
        """Load Abster reference images from the references/abster folder into session state"""
        from utils.reference_loader import ReferenceImageLoader
        
        # Load images from the abster references folder
        loaded_images = ReferenceImageLoader.load_abster_reference_images()
        
        # Extract just the images (not the filenames) for session storage
        images = [img for img, filename in loaded_images]
        
        # Store in session state
        st.session_state[SESSION_KEYS["ABSTER_REFERENCE_IMAGES"]] = images
        
        return len(images)
    
    @staticmethod
    def get_abster_reference_images_info() -> dict:
        """
        Get information about Abster reference images
        
        Returns:
            dict: Information about loaded Abster reference images
        """
        from utils.reference_loader import ReferenceImageLoader
        return ReferenceImageLoader.get_abster_reference_images_info()
    
    @staticmethod
    def get_gooner_reference_images() -> list:
        """
        Get the GOONER reference images from session state
        
        Returns:
            list: List of GOONER reference images
        """
        return st.session_state.get(SESSION_KEYS["GOONER_REFERENCE_IMAGES"], [])
    
    @staticmethod
    def add_gooner_reference_image(image: Image.Image):
        """
        Add a GOONER reference image to the session
        
        Args:
            image (Image.Image): GOONER reference image to add
        """
        ref_images = SessionManager.get_gooner_reference_images()
        ref_images.append(image)
        
        # Keep only last 5 reference images to prevent memory issues
        if len(ref_images) > 5:
            ref_images = ref_images[-5:]
            
        st.session_state[SESSION_KEYS["GOONER_REFERENCE_IMAGES"]] = ref_images
    
    @staticmethod
    def clear_gooner_reference_images():
        """Clear all GOONER reference images from session"""
        st.session_state[SESSION_KEYS["GOONER_REFERENCE_IMAGES"]] = []
    
    @staticmethod
    def has_gooner_reference_images() -> bool:
        """
        Check if there are GOONER reference images in session
        
        Returns:
            bool: True if there are GOONER reference images
        """
        return len(SessionManager.get_gooner_reference_images()) > 0
    
    @staticmethod
    def load_gooner_reference_images_from_folder():
        """Load GOONER reference images from the references/gooner folder into session state"""
        from utils.reference_loader import ReferenceImageLoader
        
        # Load images from the gooner references folder
        loaded_images = ReferenceImageLoader.load_gooner_reference_images()
        
        # Extract just the images (not the filenames) for session storage
        images = [img for img, filename in loaded_images]
        
        # Store in session state
        st.session_state[SESSION_KEYS["GOONER_REFERENCE_IMAGES"]] = images
        
        return len(images)
    
    @staticmethod
    def get_gooner_reference_images_info() -> dict:
        """
        Get information about GOONER reference images
        
        Returns:
            dict: Information about loaded GOONER reference images
        """
        from utils.reference_loader import ReferenceImageLoader
        return ReferenceImageLoader.get_gooner_reference_images_info()
    
    @staticmethod
    def get_retsba_reference_images() -> list:
        """
        Get the Retsba reference images from session state
        
        Returns:
            list: List of Retsba reference images
        """
        return st.session_state.get(SESSION_KEYS["RETSBA_REFERENCE_IMAGES"], [])
    
    @staticmethod
    def add_retsba_reference_image(image: Image.Image):
        """
        Add a Retsba reference image to the session
        
        Args:
            image (Image.Image): Retsba reference image to add
        """
        ref_images = SessionManager.get_retsba_reference_images()
        ref_images.append(image)
        
        # Keep only last 5 reference images to prevent memory issues
        if len(ref_images) > 5:
            ref_images = ref_images[-5:]
            
        st.session_state[SESSION_KEYS["RETSBA_REFERENCE_IMAGES"]] = ref_images
    
    @staticmethod
    def clear_retsba_reference_images():
        """Clear all Retsba reference images from session"""
        st.session_state[SESSION_KEYS["RETSBA_REFERENCE_IMAGES"]] = []
    
    @staticmethod
    def has_retsba_reference_images() -> bool:
        """
        Check if there are Retsba reference images in session
        
        Returns:
            bool: True if there are Retsba reference images
        """
        return len(SessionManager.get_retsba_reference_images()) > 0
    
    @staticmethod
    def load_retsba_reference_images_from_folder():
        """Load Retsba reference images from the references/retsba folder into session state"""
        from utils.reference_loader import ReferenceImageLoader
        
        # Load images from the retsba references folder
        loaded_images = ReferenceImageLoader.load_retsba_reference_images()
        
        # Extract just the images (not the filenames) for session storage
        images = [img for img, filename in loaded_images]
        
        # Store in session state
        st.session_state[SESSION_KEYS["RETSBA_REFERENCE_IMAGES"]] = images
        
        return len(images)
    
    @staticmethod
    def get_retsba_reference_images_info() -> dict:
        """
        Get information about Retsba reference images
        
        Returns:
            dict: Information about loaded Retsba reference images
        """
        from utils.reference_loader import ReferenceImageLoader
        return ReferenceImageLoader.get_retsba_reference_images_info()