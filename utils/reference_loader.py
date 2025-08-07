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
    def get_abster_references_folder_path() -> str:
        """
        Get the path to the Abster references folder
        
        Returns:
            str: Path to the Abster references folder
        """
        # Get the directory where the current script is located
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(current_dir, 'references', 'abster')
    
    @staticmethod
    def get_gooner_references_folder_path() -> str:
        """
        Get the path to the GOONER references folder
        
        Returns:
            str: Path to the GOONER references folder
        """
        # Get the directory where the current script is located
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(current_dir, 'references', 'gooner')
    
    @staticmethod
    def get_retsba_references_folder_path() -> str:
        """
        Get the path to the Retsba references folder
        
        Returns:
            str: Path to the Retsba references folder
        """
        # Get the directory where the current script is located
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(current_dir, 'references', 'retsba')
    
    @staticmethod
    def get_beary_references_folder_path() -> str:
        """
        Get the path to the Beary references folder
        
        Returns:
            str: Path to the Beary references folder
        """
        # Get the directory where the current script is located
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(current_dir, 'references', 'beary')
    
    @staticmethod
    def get_god_references_folder_path() -> str:
        """
        Get the path to the GOD references folder
        
        Returns:
            str: Path to the GOD references folder
        """
        # Get the directory where the current script is located
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(current_dir, 'references', 'god')
    
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
    def load_abster_reference_images() -> List[Tuple[Image.Image, str]]:
        """
        Load all Abster reference images from the references/abster folder
        
        Returns:
            List[Tuple[Image.Image, str]]: List of (image, filename) tuples
        """
        abster_references_path = ReferenceImageLoader.get_abster_references_folder_path()
        loaded_images = []
        
        if not os.path.exists(abster_references_path):
            st.info(f"Abster references folder not found at: {abster_references_path}")
            return loaded_images
        
        try:
            # Get all files in the abster references folder
            files = os.listdir(abster_references_path)
            image_files = [
                f for f in files 
                if os.path.splitext(f.lower())[1] in ReferenceImageLoader.SUPPORTED_EXTENSIONS
            ]
            
            for filename in image_files:
                try:
                    file_path = os.path.join(abster_references_path, filename)
                    image = Image.open(file_path)
                    
                    # Convert to RGB if necessary
                    if image.mode != 'RGB':
                        image = image.convert('RGB')
                    
                    loaded_images.append((image, filename))
                    
                except Exception as e:
                    st.warning(f"Could not load Abster reference image {filename}: {str(e)}")
                    continue
            
            if loaded_images:
                st.success(f"✅ Loaded {len(loaded_images)} Abster reference images")
            else:
                st.info("ℹ️ No Abster reference images found. Add Abster images to the 'references/abster' folder to use them for generation.")
                
        except Exception as e:
            st.error(f"Error accessing Abster references folder: {str(e)}")
        
        return loaded_images
    
    @staticmethod
    def load_gooner_reference_images() -> List[Tuple[Image.Image, str]]:
        """
        Load all GOONER reference images from the references/gooner folder
        
        Returns:
            List[Tuple[Image.Image, str]]: List of (image, filename) tuples
        """
        gooner_references_path = ReferenceImageLoader.get_gooner_references_folder_path()
        loaded_images = []
        
        if not os.path.exists(gooner_references_path):
            st.info(f"GOONER references folder not found at: {gooner_references_path}")
            return loaded_images
        
        try:
            # Get all files in the gooner references folder
            files = os.listdir(gooner_references_path)
            image_files = [
                f for f in files 
                if os.path.splitext(f.lower())[1] in ReferenceImageLoader.SUPPORTED_EXTENSIONS
            ]
            
            for filename in image_files:
                try:
                    file_path = os.path.join(gooner_references_path, filename)
                    image = Image.open(file_path)
                    
                    # Convert to RGB if necessary
                    if image.mode != 'RGB':
                        image = image.convert('RGB')
                    
                    loaded_images.append((image, filename))
                    
                except Exception as e:
                    st.warning(f"Could not load GOONER reference image {filename}: {str(e)}")
                    continue
            
            if loaded_images:
                st.success(f"✅ Loaded {len(loaded_images)} GOONER reference images")
            else:
                st.info("ℹ️ No GOONER reference images found. Add GOONER images to the 'references/gooner' folder to use them for generation.")
                
        except Exception as e:
            st.error(f"Error accessing GOONER references folder: {str(e)}")
        
        return loaded_images
    
    @staticmethod
    def load_retsba_reference_images() -> List[Tuple[Image.Image, str]]:
        """
        Load all Retsba reference images from the references/retsba folder
        
        Returns:
            List[Tuple[Image.Image, str]]: List of (image, filename) tuples
        """
        retsba_references_path = ReferenceImageLoader.get_retsba_references_folder_path()
        loaded_images = []
        
        if not os.path.exists(retsba_references_path):
            st.info(f"Retsba references folder not found at: {retsba_references_path}")
            return loaded_images
        
        try:
            # Get all files in the retsba references folder
            files = os.listdir(retsba_references_path)
            image_files = [
                f for f in files 
                if os.path.splitext(f.lower())[1] in ReferenceImageLoader.SUPPORTED_EXTENSIONS
            ]
            
            for filename in image_files:
                try:
                    file_path = os.path.join(retsba_references_path, filename)
                    image = Image.open(file_path)
                    
                    # Convert to RGB if necessary
                    if image.mode != 'RGB':
                        image = image.convert('RGB')
                    
                    loaded_images.append((image, filename))
                    
                except Exception as e:
                    st.warning(f"Could not load Retsba reference image {filename}: {str(e)}")
                    continue
            
            if loaded_images:
                st.success(f"✅ Loaded {len(loaded_images)} Retsba reference images")
            else:
                st.info("ℹ️ No Retsba reference images found. Add Retsba images to the 'references/retsba' folder to use them for generation.")
                
        except Exception as e:
            st.error(f"Error accessing Retsba references folder: {str(e)}")
        
        return loaded_images
    
    @staticmethod
    def load_beary_reference_images() -> List[Tuple[Image.Image, str]]:
        """
        Load all Beary reference images from the references/beary folder
        
        Returns:
            List[Tuple[Image.Image, str]]: List of (image, filename) tuples
        """
        beary_references_path = ReferenceImageLoader.get_beary_references_folder_path()
        loaded_images = []
        
        if not os.path.exists(beary_references_path):
            st.info(f"Beary references folder not found at: {beary_references_path}")
            return loaded_images
        
        try:
            # Get all files in the beary references folder
            files = os.listdir(beary_references_path)
            image_files = [
                f for f in files 
                if os.path.splitext(f.lower())[1] in ReferenceImageLoader.SUPPORTED_EXTENSIONS
            ]
            
            for filename in image_files:
                try:
                    file_path = os.path.join(beary_references_path, filename)
                    image = Image.open(file_path)
                    
                    # Convert to RGB if necessary
                    if image.mode != 'RGB':
                        image = image.convert('RGB')
                    
                    loaded_images.append((image, filename))
                    
                except Exception as e:
                    st.warning(f"Could not load Beary reference image {filename}: {str(e)}")
                    continue
            
            if loaded_images:
                st.success(f"✅ Loaded {len(loaded_images)} Beary reference images")
            else:
                st.info("ℹ️ No Beary reference images found. Add Beary images to the 'references/beary' folder to use them for generation.")
                
        except Exception as e:
            st.error(f"Error accessing Beary references folder: {str(e)}")
        
        return loaded_images
    
    @staticmethod
    def load_god_reference_images() -> List[Tuple[Image.Image, str]]:
        """
        Load all GOD reference images from the references/god folder
        
        Returns:
            List[Tuple[Image.Image, str]]: List of (image, filename) tuples
        """
        god_references_path = ReferenceImageLoader.get_god_references_folder_path()
        loaded_images = []
        
        if not os.path.exists(god_references_path):
            st.info(f"GOD references folder not found at: {god_references_path}")
            return loaded_images
        
        try:
            # Get all files in the god references folder
            files = os.listdir(god_references_path)
            image_files = [
                f for f in files 
                if os.path.splitext(f.lower())[1] in ReferenceImageLoader.SUPPORTED_EXTENSIONS
            ]
            
            for filename in image_files:
                try:
                    file_path = os.path.join(god_references_path, filename)
                    image = Image.open(file_path)
                    
                    # Convert to RGB if necessary
                    if image.mode != 'RGB':
                        image = image.convert('RGB')
                    
                    loaded_images.append((image, filename))
                    
                except Exception as e:
                    st.warning(f"Could not load GOD reference image {filename}: {str(e)}")
                    continue
            
            if loaded_images:
                st.success(f"✅ Loaded {len(loaded_images)} GOD reference images")
            else:
                st.info("ℹ️ No GOD reference images found. Add GOD images to the 'references/god' folder to use them for generation.")
                
        except Exception as e:
            st.error(f"Error accessing GOD references folder: {str(e)}")
        
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
    def get_abster_reference_images_info() -> dict:
        """
        Get information about available Abster reference images
        
        Returns:
            dict: Information about Abster reference images
        """
        abster_references_path = ReferenceImageLoader.get_abster_references_folder_path()
        
        if not os.path.exists(abster_references_path):
            return {
                "folder_exists": False,
                "folder_path": abster_references_path,
                "image_count": 0,
                "image_files": []
            }
        
        try:
            files = os.listdir(abster_references_path)
            image_files = [
                f for f in files 
                if os.path.splitext(f.lower())[1] in ReferenceImageLoader.SUPPORTED_EXTENSIONS
            ]
            
            return {
                "folder_exists": True,
                "folder_path": abster_references_path,
                "image_count": len(image_files),
                "image_files": image_files
            }
            
        except Exception as e:
            return {
                "folder_exists": True,
                "folder_path": abster_references_path,
                "image_count": 0,
                "image_files": [],
                "error": str(e)
            }
    
    @staticmethod
    def get_gooner_reference_images_info() -> dict:
        """
        Get information about available GOONER reference images
        
        Returns:
            dict: Information about GOONER reference images
        """
        gooner_references_path = ReferenceImageLoader.get_gooner_references_folder_path()
        
        if not os.path.exists(gooner_references_path):
            return {
                "folder_exists": False,
                "folder_path": gooner_references_path,
                "image_count": 0,
                "image_files": []
            }
        
        try:
            files = os.listdir(gooner_references_path)
            image_files = [
                f for f in files 
                if os.path.splitext(f.lower())[1] in ReferenceImageLoader.SUPPORTED_EXTENSIONS
            ]
            
            return {
                "folder_exists": True,
                "folder_path": gooner_references_path,
                "image_count": len(image_files),
                "image_files": image_files
            }
            
        except Exception as e:
            return {
                "folder_exists": True,
                "folder_path": gooner_references_path,
                "image_count": 0,
                "image_files": [],
                "error": str(e)
            }
    
    @staticmethod
    def get_retsba_reference_images_info() -> dict:
        """
        Get information about available Retsba reference images
        
        Returns:
            dict: Information about Retsba reference images
        """
        retsba_references_path = ReferenceImageLoader.get_retsba_references_folder_path()
        
        if not os.path.exists(retsba_references_path):
            return {
                "folder_exists": False,
                "folder_path": retsba_references_path,
                "image_count": 0,
                "image_files": []
            }
        
        try:
            files = os.listdir(retsba_references_path)
            image_files = [
                f for f in files 
                if os.path.splitext(f.lower())[1] in ReferenceImageLoader.SUPPORTED_EXTENSIONS
            ]
            
            return {
                "folder_exists": True,
                "folder_path": retsba_references_path,
                "image_count": len(image_files),
                "image_files": image_files
            }
            
        except Exception as e:
            return {
                "folder_exists": True,
                "folder_path": retsba_references_path,
                "image_count": 0,
                "image_files": [],
                "error": str(e)
            }
    
    @staticmethod
    def get_beary_reference_images_info() -> dict:
        """
        Get information about available Beary reference images
        
        Returns:
            dict: Information about Beary reference images
        """
        beary_references_path = ReferenceImageLoader.get_beary_references_folder_path()
        
        if not os.path.exists(beary_references_path):
            return {
                "folder_exists": False,
                "folder_path": beary_references_path,
                "image_count": 0,
                "image_files": []
            }
        
        try:
            files = os.listdir(beary_references_path)
            image_files = [
                f for f in files 
                if os.path.splitext(f.lower())[1] in ReferenceImageLoader.SUPPORTED_EXTENSIONS
            ]
            
            return {
                "folder_exists": True,
                "folder_path": beary_references_path,
                "image_count": len(image_files),
                "image_files": image_files
            }
            
        except Exception as e:
            return {
                "folder_exists": True,
                "folder_path": beary_references_path,
                "image_count": 0,
                "image_files": [],
                "error": str(e)
            }
    
    @staticmethod
    def get_god_reference_images_info() -> dict:
        """
        Get information about available GOD reference images
        
        Returns:
            dict: Information about GOD reference images
        """
        god_references_path = ReferenceImageLoader.get_god_references_folder_path()
        
        if not os.path.exists(god_references_path):
            return {
                "folder_exists": False,
                "folder_path": god_references_path,
                "image_count": 0,
                "image_files": []
            }
        
        try:
            files = os.listdir(god_references_path)
            image_files = [
                f for f in files 
                if os.path.splitext(f.lower())[1] in ReferenceImageLoader.SUPPORTED_EXTENSIONS
            ]
            
            return {
                "folder_exists": True,
                "folder_path": god_references_path,
                "image_count": len(image_files),
                "image_files": image_files
            }
            
        except Exception as e:
            return {
                "folder_exists": True,
                "folder_path": god_references_path,
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