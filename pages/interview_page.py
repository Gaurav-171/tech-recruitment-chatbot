import streamlit as st
from utils.file_handler import load_questions_from_json, update_question_index, delete_questions_file
from utils.llm_handler import get_llm_response, initialize_groq_client
from utils.session_manager import initialize_session_state
from prompts import (get_evaluation_prompt, get_evaluation_system_prompt, 
                    get_interview_introduction_prompt, get_contextual_followup_prompt)
from datetime import datetime

def evaluate_answer_with_context(client, question, answer, tech_stack, position, interview_history):
    """Evaluate candidate's answer with emotional intelligence and context awareness"""
    system_prompt = get_evaluation_system_prompt()
    
    # Create context from previous Q&A pairs
    previous_questions = [item.get('question', '') for item in interview_history if item.get('question')]
    previous_answers = [item.get('answer', '') for item in interview_history if item.get('answer')]
    
    # Enhanced evaluation prompt with memory
    prompt = f"""
    **Current Assessment:**
    Question: {question}
    Candidate's Answer: {answer}
    
    **Candidate Profile:**
    Position: {position}
    Tech Stack: {', '.join(tech_stack)}
    
    **Interview Memory & Context:**
    {chr(10).join([f"Previous Q{i+1}: {q}{chr(10)}Previous A{i+1}: {a}{chr(10)}" for i, (q, a) in enumerate(zip(previous_questions[-2:], previous_answers[-2:]))])}
    
    **Emotional Intelligence Guidelines:**
    - Assess confidence level from response length and detail
    - Notice enthusiasm, uncertainty, or stress indicators in their language
    - Adapt tone accordingly: encouraging for hesitant candidates, challenging for confident ones
    - Reference their previous answers when relevant to show active listening
    - Build on their demonstrated strengths and interests
    
    **Response Style Adaptation:**
    - If answer is short/uncertain: Be more encouraging and supportive
    - If answer shows confidence: Acknowledge expertise and perhaps probe deeper
    - If answer builds on previous responses: Acknowledge the connection
    - If answer reveals passion: Respond with matching enthusiasm
    
    Provide personalized feedback that demonstrates you're actively listening and building rapport.
    """
    
    return get_llm_response(client, prompt, system_prompt)

def generate_personalized_introduction(client, candidate_info):
    """Generate a personalized interview introduction"""
    prompt = get_interview_introduction_prompt(
        candidate_info['name'],
        candidate_info['position'],
        candidate_info['tech_stack'],
        candidate_info['experience']
    )
    
    system_prompt = """You are a warm, professional technical interviewer known for making candidates feel comfortable and confident. Create personalized, encouraging interview introductions that set a positive tone."""
    
    return get_llm_response(client, prompt, system_prompt)

def interview_page():
    """Interactive interview page with enhanced emotional intelligence"""
    client = initialize_groq_client()
    candidate = st.session_state.candidate_info
    
    questions_data = load_questions_from_json()
    if not questions_data:
        st.error("❌ No question found. Please restart the interview process.")
        if st.button("🏠 Return to Welcome"):
            st.session_state.page = 'welcome'
            st.rerun()
        return
    
    questions = questions_data['questions']
    total_questions = len(questions)
    current_index = questions_data['current_question_index']
    
    # Validate index and questions
    if not questions or current_index >= total_questions:
        st.error("❌ Invalid question data or index out of range. Resetting interview.")
        if st.button("🏠 Return to Welcome"):
            delete_questions_file()
            st.session_state.page = 'welcome'
            st.rerun()
        return
    
    st.markdown(f"""
    <div class="interview-header">
        <h1>🎤 Technical Interview - {candidate['name']}</h1>
        <p>Position: {candidate['position']} | Experience: {candidate['experience']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    progress_percentage = (current_index / total_questions) * 100 if total_questions > 0 else 0
    
    st.markdown(f"""
    <div class="progress-bar">
        <div class="progress-fill" style="width: {progress_percentage}%"></div>
    </div>
    <p style="text-align: center; margin: 0.5rem 0; font-size: 1.1rem; color: #4a5568;">
        Progress: {current_index}/{total_questions} questions completed
    </p>
    """, unsafe_allow_html=True)
    
    # Initialize interview with personalized introduction
    if not st.session_state.interview_started:
        with st.spinner("🤖 Preparing personalized welcome message..."):
            personalized_intro = generate_personalized_introduction(client, candidate)
        
        welcome_msg = f"""
        {personalized_intro}
        
        **Interview Structure:**
        • {total_questions} thoughtfully selected questions based on your {candidate['position']} role
        • Questions tailored to your tech stack: {', '.join(candidate['tech_stack'][:3])}
        • Focused on practical knowledge and problem-solving approach
        
        **Remember:** 
        ✨ There are no "wrong" answers - we value your thinking process
        🤝 Feel free to ask for clarification if needed
        💭 It's perfectly fine to think out loud or admit when you're unsure
        
        Let's begin this conversation! 🚀
        """
        
        # Initialize interview history for memory
        if 'interview_history' not in st.session_state:
            st.session_state.interview_history = []
        
        st.session_state.chat_history.append({
            'role': 'assistant',
            'content': welcome_msg,
            'timestamp': datetime.now()
        })
        st.session_state.interview_started = True
        st.session_state.current_question_index = 0
    
    # Display chat history
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.chat_history:
            if message['role'] == 'assistant':
                content_formatted = message['content'].replace('\n', '<br>')
                if content_formatted.startswith('**Question'):
                    question_number = content_formatted.split('of')[0].replace('**Question ', '').strip()
                    question_text = content_formatted.split(':**<br><br>')[1] if ':**<br><br>' in content_formatted else content_formatted
                    st.markdown(f"""
                    <div class="chat-message bot-message">
                        <div class="question-header">🤖 AI Interviewer: Question {question_number}</div>
                        {question_text}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="chat-message bot-message">
                        <strong>🤖 AI Interviewer:</strong><br>
                        {content_formatted}
                    </div>
                    """, unsafe_allow_html=True)
            else:
                content_formatted = message['content'].replace('\n', '<br>')
                st.markdown(f"""
                <div class="chat-message user-message">
                    <strong>👤 You:</strong><br>
                    {content_formatted}
                </div>
                """, unsafe_allow_html=True)
    
    # Check if interview is completed
    if st.session_state.interview_completed:
        st.markdown("""
        <div class="completion-message">
            <h2>🎉 Interview Completed Successfully!</h2>
            <p><strong>Thank you for sharing your expertise and insights with us!</strong></p>
            <p>Your thoughtful responses have given us valuable insight into your technical abilities and problem-solving approach.</p>
            <p><strong>What happens next:</strong></p>
            <ul>
                <li>🔍 Our technical team will carefully review your responses within 24 hours</li>
                <li>📧 You'll receive detailed feedback via email within 2-3 business days</li>
                <li>🤝 If there's a mutual fit, we'll schedule a follow-up conversation</li>
                <li>✨ Regardless of outcome, we appreciate the time you've invested with us</li>
            </ul>
            <p style="margin-top: 1.5rem;"><em>We believe in transparent, respectful hiring processes and will keep you informed every step of the way.</em></p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🏠 Return to Welcome", help="Start a new interview session"):
            delete_questions_file()
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            initialize_session_state()
            st.rerun()
        return
    
    # Ask next question if available and not waiting
    if current_index < total_questions and not st.session_state.waiting_for_answer:
        current_question = questions[current_index]
        question_msg = f"**Question {current_index + 1} of {total_questions}:**\n\n{current_question}"
        
        st.session_state.chat_history.append({
            'role': 'assistant',
            'content': question_msg,
            'timestamp': datetime.now()
        })
        st.session_state.waiting_for_answer = True
        st.rerun()
    
    # User input section - FIXED BUTTON LOGIC
    if not st.session_state.interview_completed and st.session_state.waiting_for_answer:
        st.markdown("---")
        
        # Create unique key for text area to avoid conflicts
        answer_key = f"answer_input_{current_index}_{st.session_state.get('answer_counter', 0)}"
        
        user_input = st.text_area(
            "✍️ Your Answer:",
            placeholder="Take your time to think through your response... Feel free to explain your reasoning and share examples from your experience.",
            height=150,
            key=answer_key
        )
        
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            # FIXED: Skip button with proper state management
            if st.button("⏭️ Skip Question", key=f"skip_btn_{current_index}", help="Skip this question if you'd prefer not to answer"):
                # Immediately update session state
                st.session_state.chat_history.append({
                    'role': 'user',
                    'content': "I'd like to skip this question.",
                    'timestamp': datetime.now()
                })
                
                # Empathetic skip response
                skip_responses = [
                    "Absolutely no problem! It's perfectly fine to skip questions you're not comfortable with. Let's move forward! 👍",
                    "That's completely understandable! Not every question will align with your experience. Let's continue! ✨",
                    "No worries at all! Honesty about what you do and don't know is exactly what we appreciate. Moving on! 🚀"
                ]
                import random
                skip_response = random.choice(skip_responses)
                
                st.session_state.chat_history.append({
                    'role': 'assistant',
                    'content': skip_response,
                    'timestamp': datetime.now()
                })
                
                # Update progress immediately in session state
                new_index = current_index + 1
                st.session_state.current_question_index = new_index
                st.session_state.waiting_for_answer = False
                
                # Update JSON file
                update_question_index(new_index)
                
                # Check if interview is complete
                if new_index >= total_questions:
                    st.session_state.interview_completed = True
                
                # Increment counter to force text area refresh
                st.session_state.answer_counter = st.session_state.get('answer_counter', 0) + 1
                
                st.rerun()
        
        with col3:
            # FIXED: Submit button with proper state management
            submit_disabled = not user_input or not user_input.strip()
            
            if st.button("📤 Submit Answer", 
                        type="primary", 
                        disabled=submit_disabled,
                        key=f"submit_btn_{current_index}"):
                
                # Handle exit commands
                if user_input.strip().lower() in ['exit', 'quit', 'end', 'stop']:
                    st.session_state.interview_completed = True
                    st.rerun()
                    return
                
                # Immediately update session state
                st.session_state.chat_history.append({
                    'role': 'user',
                    'content': user_input,
                    'timestamp': datetime.now()
                })
                
                # Add to interview history for memory
                if 'interview_history' not in st.session_state:
                    st.session_state.interview_history = []
                
                st.session_state.interview_history.append({
                    'question': questions[current_index],
                    'answer': user_input,
                    'question_number': current_index + 1
                })
                
                # Generate feedback with loading spinner
                with st.spinner("🤔 Analyzing your response with care..."):
                    try:
                        feedback = evaluate_answer_with_context(
                            client,
                            questions[current_index],
                            user_input,
                            candidate['tech_stack'],
                            candidate['position'],
                            st.session_state.interview_history
                        )
                        
                        st.session_state.chat_history.append({
                            'role': 'assistant',
                            'content': f"Thank you for that thoughtful response! {feedback}",
                            'timestamp': datetime.now()
                        })
                    except Exception as e:
                        st.error(f"Error generating feedback: {e}")
                        st.session_state.chat_history.append({
                            'role': 'assistant',
                            'content': "Thank you for your response! I appreciate your detailed answer.",
                            'timestamp': datetime.now()
                        })
                
                # Update progress immediately in session state
                new_index = current_index + 1
                st.session_state.current_question_index = new_index
                st.session_state.waiting_for_answer = False
                
                # Update JSON file
                update_question_index(new_index)
                
                # Check if interview is complete
                if new_index >= total_questions:
                    st.session_state.interview_completed = True
                
                # Increment counter to force text area refresh
                st.session_state.answer_counter = st.session_state.get('answer_counter', 0) + 1
                
                st.rerun()