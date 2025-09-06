import random

# App settings
APP_TITLE = "NeuralHire - AI Hiring Assistant"
APP_ICON = "🎯"
LAYOUT = "wide"
INITIAL_SIDEBAR_STATE = "collapsed"

# Question settings
NUM_QUESTIONS = 5

# File paths
QUESTIONS_FILE = "generated_questions.json"
INTERVIEW_DATA_FILE = "interview_data.json"

# LLM settings - Enhanced for better responses
MAX_TOKENS = 1000  # Increased for more detailed responses
TEMPERATURE = 0.6  # Slightly lower for more consistent, professional responses
MODEL_ID = "meta-llama/llama-4-scout-17b-16e-instruct"

# Enhanced loading messages for better UX
LOADING_MESSAGES = [
    "🧠 Analyzing your technical background...",
    "🎯 Crafting questions tailored to your expertise...", 
    "⚡ Optimizing difficulty level for your experience...",
    "🔍 Selecting the most relevant technical topics...",
    "✨ Finalizing your personalized interview experience..."
]

# Emotional response variations for more human-like interaction
ENCOURAGING_RESPONSES = [
    "Great perspective! Your approach shows solid thinking.",
    "I appreciate your detailed explanation - that's exactly the kind of insight we value.",
    "Excellent point! Your experience really comes through in that answer.",
    "That's a thoughtful way to approach the problem.",
    "Nice work! Your understanding of the concept is clear."
]

SUPPORTIVE_RESPONSES = [
    "Thank you for your honesty - that's exactly the kind of authenticity we appreciate.",
    "That's a great start, and your thinking process is valuable.",
    "I can see you're working through this thoughtfully.",
    "Your approach shows good problem-solving instincts.",
    "That's perfectly fine - not everyone has experience with every technology."
]

# Interview completion messages
COMPLETION_MESSAGES = {
    'positive': [
        "🌟 Outstanding performance! Your technical knowledge and problem-solving approach have been impressive throughout this interview.",
        "🎯 Excellent work! You've demonstrated both technical competency and clear communication skills.",
        "💡 Great job! Your answers show strong technical understanding and practical experience."
    ],
    'balanced': [
        "👍 Well done! You've shown good technical thinking and a willingness to tackle challenging questions.",
        "🤝 Nice work! Your approach to problem-solving and honest communication are valued qualities.",
        "✨ Good effort! You've demonstrated both technical knowledge and professional maturity."
    ],
    'encouraging': [
        "🙏 Thank you for your thoughtful participation! Your genuine approach and effort are exactly what we look for.",
        "💪 Great job engaging with challenging topics! Your willingness to think through problems is impressive.",
        "🌱 Excellent work! Your enthusiasm for learning and growth really comes through."
    ]
}

# Question difficulty mapping
DIFFICULTY_LEVELS = {
    'Fresher': 'foundational',
    'Intern': 'foundational', 
    '1 Year': 'intermediate',
    '2 Years': 'intermediate',
    '3-5 Years': 'advanced',
    '5+ Years': 'expert'
}

# Position-specific focus areas
POSITION_FOCUS_AREAS = {
    'Full Stack Developer': ['frontend', 'backend', 'databases', 'system_design'],
    'Frontend Developer': ['ui_ux', 'javascript', 'frameworks', 'performance'],
    'Backend Developer': ['apis', 'databases', 'scalability', 'security'],
    'DevOps Engineer': ['automation', 'cloud', 'monitoring', 'deployment'],
    'Data Scientist': ['algorithms', 'statistics', 'tools', 'visualization'],
    'Mobile Developer': ['platform_specific', 'performance', 'user_experience', 'deployment'],
    'Software Engineer': ['algorithms', 'system_design', 'best_practices', 'debugging']
}