"""
Reference Image Loader for ALF Abstractor
Handles loading ALF reference images from the references folder
"""

import os
from PIL import Image
from typing import List, Tuple
import streamlit as st

class ReferenceImageLoader:
    """Loads and manages reference images from the references folder"""
    
    SUPPORTED_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.bmp'}
    
    @staticmethod
    def get_references_folder_path() -> str:
        """
        Get the path to the references folder
        
        Returns:
            str: Path to the references folder
        """
        # Get the directory where the current script is located
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(current_dir, 'references')
    
    @staticmethod
    def get_polly_references_folder_path() -> str:
        """
        Get the path to the Polly references folder
        
        Returns:
            str: Path to the Polly references folder
        """
        # Get the directory where the current script is located
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(current_dir, 'references', 'polly')
    
    @staticmethod
    def load_reference_images() -> List[Tuple[Image.Image, str]]:
        """
        Load all reference images from the references folder
        
        Returns:
            List[Tuple[Image.Image, str]]: List of (image, filename) tuples
        """
        references_path = ReferenceImageLoader.get_references_folder_path()
        loaded_images = []
        
        if not os.path.exists(references_path):
            st.warning(f"References folder not found at: {references_path}")
            return loaded_images
        
        try:
            # Get all files in the references folder
            files = os.listdir(references_path)
            image_files = [
                f for f in files 
                if os.path.splitext(f.lower())[1] in ReferenceImageLoader.SUPPORTED_EXTENSIONS
            ]
            
            for filename in image_files:
                try:
                    file_path = os.path.join(references_path, filename)
                    image = Image.open(file_path)
                    
                    # Convert to RGB if necessary
                    if image.mode != 'RGB':
                        image = image.convert('RGB')
                    
                    loaded_images.append((image, filename))
                    
                except Exception as e:
                    st.warning(f"Could not load reference image {filename}: {str(e)}")
                    continue
            
            if loaded_images:
                st.success(f"✅ Loaded {len(loaded_images)} ALF reference images")
            else:
                st.info("ℹ️ No reference images found. Add ALF images to the 'references' folder to use them for generation.")
                
        except Exception as e:
            st.error(f"Error accessing references folder: {str(e)}")
        
        return loaded_images
    
    @staticmethod
    def load_polly_reference_images() -> List[Tuple[Image.Image, str]]:
        """
        Load all Polly reference images from the references/polly folder
        
        Returns:
            List[Tuple[Image.Image, str]]: List of (image, filename) tuples
        """
        polly_references_path = ReferenceImageLoader.get_polly_references_folder_path()
        loaded_images = []
        
        if not os.path.exists(polly_references_path):
            st.info(f"Polly references folder not found at: {polly_references_path}")
            return loaded_images
        
        try:
            # Get all files in the polly references folder
            files = os.listdir(polly_references_path)
            image_files = [
                f for f in files 
                if os.path.splitext(f.lower())[1] in ReferenceImageLoader.SUPPORTED_EXTENSIONS
            ]
            
            for filename in image_files:
                try:
                    file_path = os.path.join(polly_references_path, filename)
                    image = Image.open(file_path)
                    
                    # Convert to RGB if necessary
                    if image.mode != 'RGB':
                        image = image.convert('RGB')
                    
                    loaded_images.append((image, filename))
                    
                except Exception as e:
                    st.warning(f"Could not load Polly reference image {filename}: {str(e)}")
                    continue
            
            if loaded_images:
                st.success(f"✅ Loaded {len(loaded_images)} Polly reference images")
            else:
                st.info("ℹ️ No Polly reference images found. Add Polly images to the 'references/polly' folder to use them for generation.")
                
        except Exception as e:
            st.error(f"Error accessing Polly references folder: {str(e)}")
        
        return loaded_images
    
    @staticmethod
    def get_reference_images_info() -> dict:
        """
        Get information about available reference images
        
        Returns:
            dict: Information about reference images
        """
        references_path = ReferenceImageLoader.get_references_folder_path()
        
        if not os.path.exists(references_path):
            return {
                "folder_exists": False,
                "folder_path": references_path,
                "image_count": 0,
                "image_files": []
            }
        
        try:
            files = os.listdir(references_path)
            image_files = [
                f for f in files 
                if os.path.splitext(f.lower())[1] in ReferenceImageLoader.SUPPORTED_EXTENSIONS
            ]
            
            return {
                "folder_exists": True,
                "folder_path": references_path,
                "image_count": len(image_files),
                "image_files": image_files
            }
            
        except Exception as e:
            return {
                "folder_exists": True,
                "folder_path": references_path,
                "image_count": 0,
                "image_files": [],
                "error": str(e)
            }
    
    @staticmethod
    def get_polly_reference_images_info() -> dict:
        """
        Get information about available Polly reference images
        
        Returns:
            dict: Information about Polly reference images
        """
        polly_references_path = ReferenceImageLoader.get_polly_references_folder_path()
        
        if not os.path.exists(polly_references_path):
            return {
                "folder_exists": False,
                "folder_path": polly_references_path,
                "image_count": 0,
                "image_files": []
            }
        
        try:
            files = os.listdir(polly_references_path)
            image_files = [
                f for f in files 
                if os.path.splitext(f.lower())[1] in ReferenceImageLoader.SUPPORTED_EXTENSIONS
            ]
            
            return {
                "folder_exists": True,
                "folder_path": polly_references_path,
                "image_count": len(image_files),
                "image_files": image_files
            }
            
        except Exception as e:
            return {
                "folder_exists": True,
                "folder_path": polly_references_path,
                "image_count": 0,
                "image_files": [],
                "error": str(e)
            }
    
    @staticmethod
    def validate_references_folder() -> bool:
        """
        Validate that the references folder exists and is accessible
        
        Returns:
            bool: True if folder is valid and accessible
        """
        references_path = ReferenceImageLoader.get_references_folder_path()
        return os.path.exists(references_path) and os.path.isdir(references_path)