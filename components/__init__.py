"""
ALF Abstractor Components Package
Contains all UI components for the application
"""

from .landing_page import render_landing_page
from .prompt_page import render_prompt_page
from .generation_page import render_generation_page
from .result_page import render_result_page, render_image_history
from .styles import load_alf_css, create_title, create_subtitle, create_quote, create_mystical_text

__all__ = [
    'render_landing_page',
    'render_prompt_page', 
    'render_generation_page',
    'render_result_page',
    'render_image_history',
    'load_alf_css',
    'create_title',
    'create_subtitle', 
    'create_quote',
    'create_mystical_text'
]