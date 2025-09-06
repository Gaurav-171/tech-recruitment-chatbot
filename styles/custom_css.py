import streamlit as st

def apply_custom_css():
    """Apply custom CSS styles to the app with enhanced color scheme"""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&family=Poppins:wght@600&family=Inter:wght@500&family=Open+Sans:wght@400&display=swap');

        body {
            font-family: 'Roboto', sans-serif;
            background-color: #f8fafc;
            color: #2d3748;
        }

        /* Hide the sidebar */
        [data-testid="stSidebar"] {
            display: none;
        }
        /* Adjust main content to full width when sidebar is hidden */
        .main .block-container {
            max-width: 100%;
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .main-header {
            text-align: center;
            padding: 2rem 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 15px;
            margin-bottom: 2rem;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
            font-family: 'Poppins', sans-serif;
        }

        .main-header h1 {
            font-size: 2.8rem;
            margin: 0;
            text-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .welcome-card {
            background: linear-gradient(145deg, #ffffff 0%, #f7fafc 100%);
            padding: 2.5rem;
            border-radius: 20px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
            margin: 2rem 0;
            border-left: 6px solid #667eea;
            color: #2d3748;
            transition: transform 0.3s ease;
        }

        .welcome-card:hover {
            transform: translateY(-5px);
        }

        .welcome-card h2 {
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            font-size: 1.8rem;
            color: #4a5568;
            margin-bottom: 1rem;
        }

        .welcome-card p {
            font-family: 'Open Sans', sans-serif;
            font-size: 1.1rem;
            color: #2d3748;
            line-height: 1.6;
        }

        .form-card {
            background: linear-gradient(145deg, #ffffff 0%, #f7fafc 100%);
            padding: 2.5rem;
            border-radius: 20px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
            margin: 1rem 0;
            border: 1px solid #e2e8f0;
        }

        .chat-message {
            padding: 1.8rem;
            margin: 1rem 0;
            border-radius: 15px;
            max-width: 85%;
            font-size: 1.05rem;
            line-height: 1.6;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }

        .bot-message {
            background: linear-gradient(145deg, #edf2f7 0%, #e2e8f0 100%);
            border-left: 5px solid #667eea;
            margin-right: 15%;
            color: #2d3748;
            font-family: 'Roboto', sans-serif;
        }

        .bot-message strong {
            font-family: 'Poppins', sans-serif;
            font-size: 1.2rem;
            color: #4a5568;
        }

        .user-message {
            background: linear-gradient(145deg, #e6fffa 0%, #b2f5ea 100%);
            border-right: 5px solid #38b2ac;
            margin-left: 15%;
            text-align: right;
            color: #2d3748;
            font-family: 'Roboto', sans-serif;
        }

        .interview-header {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            padding: 2rem;
            border-radius: 15px;
            text-align: center;
            margin-bottom: 2rem;
            font-family: 'Poppins', sans-serif;
            box-shadow: 0 10px 30px rgba(240, 147, 251, 0.3);
        }

        .progress-bar {
            background: #e2e8f0;
            border-radius: 15px;
            padding: 6px;
            margin: 1.5rem 0;
            box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .progress-fill {
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            height: 25px;
            border-radius: 12px;
            transition: width 0.6s ease;
            box-shadow: 0 2px 8px rgba(102, 126, 234, 0.4);
        }

        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 0.8rem 2.5rem;
            border-radius: 30px;
            font-weight: 600;
            font-family: 'Roboto', sans-serif;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }

        .stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
            background: linear-gradient(135deg, #5a67d8 0%, #6b46c1 100%);
        }

        .completion-message {
            background: linear-gradient(145deg, #f0fff4 0%, #c6f6d5 100%);
            padding: 3rem;
            border-radius: 20px;
            text-align: center;
            margin: 2rem 0;
            box-shadow: 0 15px 35px rgba(72, 187, 120, 0.2);
            border-left: 6px solid #48bb78;
            font-family: 'Roboto', sans-serif;
            color: #2d3748;
        }

        .completion-message h2 {
            font-family: 'Poppins', sans-serif;
            color: #276749;
            font-size: 2rem;
            margin-bottom: 1.5rem;
        }

        .completion-message ul {
            text-align: left;
            display: inline-block;
            font-size: 1.1rem;
            color: #2d3748;
        }

        .question-header {
            font-family: 'Poppins', sans-serif;
            font-size: 1.4rem;
            color: #4a5568;
            background: linear-gradient(145deg, #f7fafc 0%, #edf2f7 100%);
            padding: 1.5rem;
            border-radius: 12px;
            margin-bottom: 1rem;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            border-left: 4px solid #667eea;
        }

        /* Enhanced input field styling */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > select {
            border-radius: 12px;
            border: 2px solid #e2e8f0;
            transition: border-color 0.3s ease;
        }

        .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus,
        .stSelectbox > div > div > select:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }

        /* Loading spinner enhancement */
        .stSpinner > div > div {
            border-color: #667eea #e2e8f0 #e2e8f0 #e2e8f0;
        }

        /* Custom alert styles */
        .stAlert > div {
            border-radius: 12px;
            border-left-width: 6px;
        }

        /* Enhanced button variants */
        .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #38b2ac 0%, #319795 100%);
            box-shadow: 0 4px 15px rgba(56, 178, 172, 0.3);
        }

        .stButton > button[kind="primary"]:hover {
            background: linear-gradient(135deg, #319795 0%, #2c7a7b 100%);
            box-shadow: 0 8px 25px rgba(56, 178, 172, 0.4);
        }

        /* Skip button styling */
        .stButton > button:not([kind="primary"]) {
            background: linear-gradient(135deg, #a0aec0 0%, #718096 100%);
            color: white;
        }

        .stButton > button:not([kind="primary"]):hover {
            background: linear-gradient(135deg, #718096 0%, #4a5568 100%);
            transform: translateY(-2px);
        }
    </style>
    """, unsafe_allow_html=True)