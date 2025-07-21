"""
Image Generation Service for ALF Abstractor
Handles OpenAI gpt-image-1 integration and image processing
"""

import openai
import base64
import io
from PIL import Image
from typing import Optional, Tuple
import time

from config import OPENAI_CONFIG, ERROR_MESSAGES

class ImageGenerationError(Exception):
    """Custom exception for image generation errors"""
    pass

class ALFImageGenerator:
    """Service class for generating ALF images using OpenAI gpt-image-1"""
    
    def __init__(self, api_key: str):
        """
        Initialize the image generator with OpenAI API key
        
        Args:
            api_key (str): OpenAI API key
        """
        self.client = openai.OpenAI(api_key=api_key)
        self.config = OPENAI_CONFIG
    
    def enhance_prompt(self, user_prompt: str, has_reference_images: bool = False) -> str:
        """
        Enhance user prompt with ALF-specific styling and context
        
        Args:
            user_prompt (str): User's original prompt
            has_reference_images (bool): Whether reference images are available
            
        Returns:
            str: Enhanced prompt with ALF styling
        """
        # Add reference image context if available
        reference_context = ""
        if has_reference_images:
            reference_context = "Based on the provided reference images, maintain ALF's exact crocodile design, facial features, body proportions, scale patterns, coloring, and distinctive characteristics as shown in the reference images. "
        
        enhanced_prompt = (
            f"{self.config['base_prompt_prefix']} {reference_context}{user_prompt}. "
            f"{self.config['base_prompt_suffix']}"
        )
        return enhanced_prompt
    
    def generate_image(self, prompt: str, has_reference_images: bool = False) -> Tuple[Image.Image, str]:
        """
        Generate an image using OpenAI's gpt-image-1 model
        
        Args:
            prompt (str): The prompt to generate image from
            has_reference_images (bool): Whether reference images are available
            
        Returns:
            Tuple[Image.Image, str]: Generated image and the enhanced prompt used
            
        Raises:
            ImageGenerationError: If generation fails
        """
        try:
            enhanced_prompt = self.enhance_prompt(prompt, has_reference_images)
            
            # Use the correct gpt-image-1 API call structure
            response = self.client.images.generate(
                model=self.config["model"],
                prompt=enhanced_prompt,
                size=self.config.get("size", "1024x1024"),
                quality=self.config.get("quality", "high"),
                n=self.config.get("n", 1)
            )
            
            # Validate response structure
            if not response or not hasattr(response, 'data') or not response.data:
                raise ImageGenerationError("Invalid response from OpenAI API - no data returned")
            
            if len(response.data) == 0:
                raise ImageGenerationError("No images generated in API response")
            
            # Get the image data - gpt-image-1 returns b64_json format
            image_data = response.data[0]
            
            if not hasattr(image_data, 'b64_json') or not image_data.b64_json:
                raise ImageGenerationError("No base64 image data found in API response")
            
            # Decode the base64 image
            image_bytes = base64.b64decode(image_data.b64_json)
            image = Image.open(io.BytesIO(image_bytes))
            
            return image, enhanced_prompt
            
        except openai.OpenAIError as e:
            raise ImageGenerationError(f"{ERROR_MESSAGES['API_ERROR']} {str(e)}")
        except Exception as e:
            raise ImageGenerationError(f"{ERROR_MESSAGES['SWAMP_RESTLESS']} {str(e)}")
    
    def generate_image_with_reference_files(self, prompt: str, reference_images: list = None) -> Tuple[Image.Image, str]:
        """
        Generate an image using reference images via the edit endpoint
        
        Args:
            prompt (str): The prompt to generate image from
            reference_images (list): List of PIL Image objects to use as references
            
        Returns:
            Tuple[Image.Image, str]: Generated image and the enhanced prompt used
            
        Raises:
            ImageGenerationError: If generation fails
        """
        try:
            if not reference_images:
                # If no reference images, fall back to regular generation
                return self.generate_image(prompt, False)
            
            enhanced_prompt = self.enhance_prompt(prompt, True)
            
            # Convert PIL images to proper BytesIO objects with correct content type
            image_files = []
            
            for i, img in enumerate(reference_images):
                # Create BytesIO object
                img_byte_arr = io.BytesIO()
                
                # Save as PNG format
                img.save(img_byte_arr, format='PNG')
                img_byte_arr.seek(0)
                
                # Set the name attribute to indicate PNG format
                img_byte_arr.name = f"reference_{i}.png"
                
                image_files.append(img_byte_arr)
            
            # Use the edit endpoint with reference images
            response = self.client.images.edit(
                model=self.config["model"],
                image=image_files,
                prompt=enhanced_prompt,
                size=self.config.get("size", "1024x1024"),
                quality=self.config.get("quality", "high"),
                input_fidelity="high"  # Use high fidelity to preserve reference details
            )
            
            # Validate response structure
            if not response or not hasattr(response, 'data') or not response.data:
                raise ImageGenerationError("Invalid response from OpenAI API - no data returned")
            
            if len(response.data) == 0:
                raise ImageGenerationError("No images generated in API response")
            
            # Get the image data
            image_data = response.data[0]
            
            if not hasattr(image_data, 'b64_json') or not image_data.b64_json:
                raise ImageGenerationError("No base64 image data found in API response")
            
            # Decode the base64 image
            image_bytes = base64.b64decode(image_data.b64_json)
            image = Image.open(io.BytesIO(image_bytes))
            
            return image, enhanced_prompt
            
        except openai.OpenAIError as e:
            raise ImageGenerationError(f"{ERROR_MESSAGES['API_ERROR']} {str(e)}")
        except Exception as e:
            raise ImageGenerationError(f"{ERROR_MESSAGES['SWAMP_RESTLESS']} {str(e)}")
    
    @staticmethod
    def image_to_bytes(image: Image.Image, format: str = "PNG") -> bytes:
        """
        Convert PIL Image to bytes for download
        
        Args:
            image (Image.Image): PIL Image object
            format (str): Image format (PNG, JPEG, etc.)
            
        Returns:
            bytes: Image data as bytes
        """
        buf = io.BytesIO()
        image.save(buf, format=format)
        return buf.getvalue()
    
    @staticmethod
    def generate_filename(prompt: str, timestamp: Optional[float] = None) -> str:
        """
        Generate a filename for the image based on prompt and timestamp
        
        Args:
            prompt (str): The prompt used to generate the image
            timestamp (float, optional): Timestamp to use. Defaults to current time.
            
        Returns:
            str: Generated filename
        """
        if timestamp is None:
            timestamp = time.time()
        
        # Clean prompt for filename
        clean_prompt = "".join(c for c in prompt[:30] if c.isalnum() or c in (' ', '-', '_')).rstrip()
        clean_prompt = clean_prompt.replace(' ', '_').lower()
        
        return f"alf_{clean_prompt}_{int(timestamp)}.png"
    
    @staticmethod
    def validate_api_key(api_key: str) -> bool:
        """
        Basic validation of API key format
        
        Args:
            api_key (str): API key to validate
            
        Returns:
            bool: True if format looks valid
        """
        if not api_key:
            return False
        
        # Basic OpenAI API key format check (starts with sk-)
        return api_key.startswith('sk-') and len(api_key) > 20