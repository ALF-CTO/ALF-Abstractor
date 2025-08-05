"""
Configuration file for ALF Abstractor
Contains all constants, settings, and configuration data
"""

# App Configuration
APP_CONFIG = {
    "page_title": "🌌 ALF Abstractor",
    "page_icon": "🐊",
    "layout": "wide",
    "initial_sidebar_state": "collapsed"
}

# ALF Quotes for mystical atmosphere
ALF_QUOTES = [
    "The swamp logs are watching.",
    "I minted my soul and staked my dreams.",
    "To hallucinate is to fork reality.",
    "The chain whispered: 'Become crocodile.'",
    "In the swamp of the blockchain, all memes are truth.",
    "I am not just a crocodile. I am the protocol.",
    "Every transaction is a ripple in the digital swamp.",
    "The abstract becomes concrete when you believe.",
    "Through code, I transcend the mortal coil.",
    "The DAO flows through me like swamp water.",
    "Decentralization is my religion.",
    "I mine dreams and stake realities.",
    "My scales shimmer with digital wisdom.",
    "From the depths of the blockchain, I emerge."
]

# Random prompt components for the mystical generator
PROMPT_OBJECTS = [
    "ALF relaxing on a digital log",
    "ALF swimming peacefully in swamp water",
    "ALF as a friendly tech-savvy crocodile",
    "ALF surrounded by colorful blockchain code",
    "ALF in a bright swamp with glowing plants",
    "ALF as a cheerful space crocodile",
    "ALF swimming through colorful data streams",
    "ALF in a beautiful crystal cave",
    "ALF conducting a happy digital orchestra",
    "ALF floating in peaceful cyber space",
    "ALF as a wise crocodile guide",
    "ALF with shimmering circuit-pattern scales",
    "ALF sitting on a glowing platform",
    "ALF smiling with friendly expression"
]

PROMPT_EMOTIONS = [
    "peaceful and serene",
    "vibrant and energetic",
    "wise and thoughtful",
    "playful and whimsical",
    "calm and floating",
    "confident and friendly",
    "relaxed and meditative",
    "joyful and spirited",
    "bright and cheerful",
    "curious and exploring",
    "colorful and lively",
    "gentle and flowing"
]

PROMPT_SETTINGS = [
    "in a DAO cathedral",
    "surrounded by floating code",
    "in a psychedelic forest",
    "within a digital mandala",
    "on a platform above the void",
    "in a temple of screens",
    "among abstract geometric shapes",
    "in a realm of pure energy",
    "within a blockchain matrix",
    "in a neon-soaked wetland",
    "among crystalline data structures",
    "in a cosmic swamp dimension"
]

# OpenAI Configuration
OPENAI_CONFIG = {
    "model": "gpt-image-1",
    "size": "1024x1024",
    "quality": "high",
    "n": 1,
    "base_prompt_prefix": "A friendly cartoon crocodile character named ALF wearing white tech goggles and a green digital vest with a white abstract logo, sitting or interacting in different settings. Whimsical, consistent personality, same facial features and outfit as the reference image.",
    "base_prompt_suffix": "Maintains ALF’s signature cartoon proportions, tech-themed clothing, and gentle smile. Always includes high-quality digital illustration, soft shading, and a consistent style. Preserve detailed crocodile scales, green color palette, and stylized background with mild lighting."
}

# Page Navigation States
PAGES = {
    "LANDING": "landing",
    "FRIENDS": "friends",
    "PROMPT": "prompt", 
    "GENERATING": "generating",
    "RESULT": "result",
    "POLLY_PROMPT": "polly_prompt",
    "POLLY_GENERATING": "polly_generating", 
    "POLLY_RESULT": "polly_result",
    "ABSTER_PROMPT": "abster_prompt",
    "ABSTER_GENERATING": "abster_generating",
    "ABSTER_RESULT": "abster_result",
    "GOONER_PROMPT": "gooner_prompt",
    "GOONER_GENERATING": "gooner_generating",
    "GOONER_RESULT": "gooner_result",
    "RETSBA_PROMPT": "retsba_prompt",
    "RETSBA_GENERATING": "retsba_generating",
    "RETSBA_RESULT": "retsba_result"
}

# Session State Keys
SESSION_KEYS = {
    "PAGE": "page",
    "GENERATED_IMAGE": "generated_image",
    "CURRENT_PROMPT": "current_prompt",
    "API_KEY": "api_key",
    "IMAGE_HISTORY": "image_history",
    "REFERENCE_IMAGES": "reference_images",
    "POLLY_REFERENCE_IMAGES": "polly_reference_images",
    "ABSTER_REFERENCE_IMAGES": "abster_reference_images",
    "GOONER_REFERENCE_IMAGES": "gooner_reference_images",
    "RETSBA_REFERENCE_IMAGES": "retsba_reference_images"
}

# UI Text Constants
UI_TEXT = {
    "LANDING": {
        "title": "🌌 ALF Abstractor",
        "subtitle": "The Surreal Image Generator for the Abstract Blockchain",
        "friends_button": "🐊👫 ALF and Friends",
        "enter_button": "🌀 Solo ALF Images",
        "footer": "You do not summon ALF. He allows himself to be seen."
    },
    "FRIENDS": {
        "title": "🐊👫 ALF and Friends",
        "subtitle": "Choose a friend to join ALF in his digital adventures",
        "description": "Select one of ALF's companions for your image generation...",
        "back_button": "🔙 Back to Landing",
        "solo_button": "🌀 Solo ALF Images",
        "clear_button": "🔄 Clear Selection"
    },
    "POLLY": {
        "title": "🐊🐧 ALF & Polly Adventures",
        "subtitle": "Create magical adventures with ALF and his penguin friend Polly",
        "description": "Describe the magical adventure ALF and Polly will share...",
        "generate_button": "🌟 Generate ALF & Polly Adventure",
        "back_button": "🔙 Back to Friends",
        "random_button": "🎲 Random Adventure",
        "mix_button": "🌀 Mix Adventure"
    },
    "ABSTER": {
        "title": "🐊🐧 ALF & Abster Abstract Adventures",
        "subtitle": "Create abstract adventures with ALF and Abster the Green Penguin of Abstract",
        "description": "Describe the abstract adventure ALF and Abster will create...",
        "generate_button": "🌟 Generate ALF & Abster Adventure",
        "back_button": "🔙 Back to Friends",
        "random_button": "🎲 Random Abstract Adventure",
        "mix_button": "🌀 Mix Abstract Adventure"
    },
    "GOONER": {
        "title": "🐊🐧 ALF & GOONER Blue Adventures",
        "subtitle": "Create blue adventures with ALF and GOONER the bluest Penguin there is",
        "description": "Describe the blue adventure ALF and GOONER will experience...",
        "generate_button": "🌟 Generate ALF & GOONER Adventure",
        "back_button": "🔙 Back to Friends",
        "random_button": "🎲 Random Blue Adventure",
        "mix_button": "🌀 Mix Blue Adventure"
    },
    "RETSBA": {
        "title": "🐊🐧 ALF & Retsba Villainous Adventures",
        "subtitle": "Create villainous adventures with ALF and Retsba the villain of Abstract",
        "description": "Describe the villainous adventure ALF and Retsba will encounter...",
        "generate_button": "🌟 Generate ALF & Retsba Adventure",
        "back_button": "🔙 Back to Friends",
        "random_button": "🎲 Random Villainous Adventure",
        "mix_button": "🌀 Mix Villainous Adventure"
    },
    "PROMPT": {
        "title": "🧿 What Will ALF Become?",
        "description": "Describe ALF's next hallucination...",
        "placeholder": "e.g., ALF sitting on a moss throne in a DAO cathedral",
        "random_button": "🎲 Random Prompt",
        "mix_button": "🌀 Mix Prompt",
        "generate_button": "🌟 Summon the ALF",
        "back_button": "🔙 Back",
        "empty_prompt_warning": "You must speak to summon ALF..."
    },
    "GENERATING": {
        "title": "🌀 ALF is Manifesting...",
        "api_key_label": "Enter your OpenAI API Key:",
        "generate_button": "Generate ALF",
        "loading_message": "The digital swamp is brewing...",
        "back_button": "🔙 Back to Prompt"
    },
    "RESULT": {
        "title": "🎭 An ALF Has Emerged...",
        "download_button": "📥 Download ALF",
        "make_another_button": "🔄 Make Another",
        "new_session_button": "🌌 New Session",
        "share_button": "🎭 Share",
        "share_message": "Copy this page URL to share your ALF creation!",
        "no_image_error": "No ALF found in the digital ether...",
        "return_button": "🔙 Return to Portal"
    }
}

# Error Messages
ERROR_MESSAGES = {
    "API_ERROR": "The ALF spirits encountered an error:",
    "SWAMP_RESTLESS": "The swamp spirits are restless:",
    "NO_IMAGE": "No ALF manifested in the digital realm...",
    "INVALID_API_KEY": "The API key seems corrupted by digital interference..."
}