"""
Utility functions for ALF Abstractor
Contains helper functions used across the application
"""

import random
from typing import List, Dict, Any
from config import PROMPT_OBJECTS, PROMPT_EMOTIONS, PROMPT_SETTINGS, ALF_QUOTES

def generate_random_prompt() -> str:
    """
    Generate a random mystical prompt for ALF image generation
    
    Returns:
        str: A randomly generated prompt combining object, emotion, and setting
    """
    obj = random.choice(PROMPT_OBJECTS)
    emotion = random.choice(PROMPT_EMOTIONS)
    setting = random.choice(PROMPT_SETTINGS)
    return f"{obj}, {emotion}, {setting}"

def get_random_alf_quote() -> str:
    """
    Get a random ALF quote for mystical atmosphere
    
    Returns:
        str: A random ALF quote
    """
    return random.choice(ALF_QUOTES)

def mix_prompt_components() -> str:
    """
    Create a mixed prompt by randomly combining different elements
    
    Returns:
        str: A mixed prompt with creative combinations
    """
    # Randomly decide if we want to use multiple objects or emotions
    use_multiple = random.choice([True, False])
    
    if use_multiple:
        obj1 = random.choice(PROMPT_OBJECTS)
        obj2 = random.choice(PROMPT_OBJECTS)
        emotion = random.choice(PROMPT_EMOTIONS)
        setting = random.choice(PROMPT_SETTINGS)
        return f"{obj1} and {obj2}, {emotion}, {setting}"
    else:
        obj = random.choice(PROMPT_OBJECTS)
        emotion1 = random.choice(PROMPT_EMOTIONS)
        emotion2 = random.choice(PROMPT_EMOTIONS)
        setting = random.choice(PROMPT_SETTINGS)
        return f"{obj}, {emotion1} and {emotion2}, {setting}"

def sanitize_filename(filename: str) -> str:
    """
    Sanitize a filename by removing invalid characters
    
    Args:
        filename (str): Original filename
        
    Returns:
        str: Sanitized filename safe for all operating systems
    """
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

def truncate_text(text: str, max_length: int = 100) -> str:
    """
    Truncate text to a maximum length with ellipsis
    
    Args:
        text (str): Text to truncate
        max_length (int): Maximum length before truncation
        
    Returns:
        str: Truncated text with ellipsis if needed
    """
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."

def format_prompt_display(prompt: str) -> str:
    """
    Format a prompt for display with proper capitalization and punctuation
    
    Args:
        prompt (str): Raw prompt text
        
    Returns:
        str: Formatted prompt text
    """
    # Capitalize first letter and ensure it ends with proper punctuation
    formatted = prompt.strip()
    if formatted:
        formatted = formatted[0].upper() + formatted[1:]
        if not formatted.endswith(('.', '!', '?')):
            formatted += '.'
    return formatted

def validate_prompt_length(prompt: str, min_length: int = 5, max_length: int = 500) -> tuple[bool, str]:
    """
    Validate prompt length and provide feedback
    
    Args:
        prompt (str): Prompt to validate
        min_length (int): Minimum allowed length
        max_length (int): Maximum allowed length
        
    Returns:
        tuple[bool, str]: (is_valid, error_message)
    """
    prompt_length = len(prompt.strip())
    
    if prompt_length < min_length:
        return False, f"Prompt too short. Need at least {min_length} characters."
    
    if prompt_length > max_length:
        return False, f"Prompt too long. Maximum {max_length} characters allowed."
    
    return True, ""

def create_mystical_loading_messages() -> List[str]:
    """
    Generate mystical loading messages for the generation process
    
    Returns:
        List[str]: List of mystical loading messages
    """
    return [
        "ALF is stirring in the digital depths...",
        "The blockchain spirits are consulted...",
        "Mystical algorithms are aligning...",
        "The digital swamp bubbles with creativity...",
        "ALF's essence is being channeled...",
        "The DAO whispers ancient secrets...",
        "Pixels are being blessed by the frog prophet...",
        "The abstract realm opens its gates..."
    ]

def get_random_loading_message() -> str:
    """
    Get a random mystical loading message
    
    Returns:
        str: A random loading message
    """
    messages = create_mystical_loading_messages()
    return random.choice(messages)

def format_error_message(error: Exception) -> str:
    """
    Format error messages in the ALF mystical style
    
    Args:
        error (Exception): The exception that occurred
        
    Returns:
        str: Formatted error message with mystical flavor
    """
    error_str = str(error)
    mystical_prefix = "The digital spirits report: "
    return f"{mystical_prefix}{error_str}"

def create_share_text(prompt: str) -> str:
    """
    Create shareable text for ALF creations
    
    Args:
        prompt (str): The prompt used to generate the image
        
    Returns:
        str: Formatted share text
    """
    quote = get_random_alf_quote()
    return f'🌌 I summoned an ALF with: "{prompt}"\n\n"{quote}"\n\n#ALFAbstractor #DigitalSwamp'