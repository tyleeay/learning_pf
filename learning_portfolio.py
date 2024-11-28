import streamlit as st
import pandas as pd
from PIL import Image

def load_image(image_path):
    try:
        return Image.open(image_path)
    except FileNotFoundError:
        st.error(f"Image not found: {image_path}")
        return None

def main():
    st.set_page_config(
        page_title="Oral Presentations Portfolio",
        page_icon="🎤",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Enhanced CSS with better spacing and visual hierarchy
    st.markdown("""
        <style>
        /* Global Styles */
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        /* Container Styles */
        .video-container {
            border: 1px solid #e0e4e8;
            padding: 2rem;

            border-radius: 8px;
            margin: 1.5rem 0;
            background-color: #f8f9fa;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        
        /* Button Styles */
        .button-link {
            display: inline-block;
            padding: 0.75rem 1.5rem;
            background-color: #f0f2f6;
            border-radius: 6px;
            text-decoration: none;
            color: #0066cc;
            margin: 0.75rem 0;
            border: 1px solid #ddd;
            transition: all 0.3s ease;
            font-weight: 500;
        }
        
        .button-link:hover {
            background-color: #e6e9ef;
            transform: translateY(-1px);
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        /* Text Container Styles */
        .reflection-text {
            background-color: #f8f9fa;
            padding: 2rem;
            border-radius: 8px;
            margin: 1.5rem 0;
            border-left: 4px solid #0066cc;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        
        .learning-journey {
            background-color: #f0f7ff;
            padding: 2rem;
            border-radius: 8px;
            margin: 1.5rem 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        
        /* Milestone Styles */
        .milestone {
            border-left: 4px solid #28a745;
            padding: 1.5rem;
            margin: 1.25rem 0;
            background-color: #fff;
            border-radius: 0 8px 8px 0;
        }
        
        /* Evaluation Form Styles */
        .evaluation-form {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 8px;
            margin: 1.5rem 0;
            border: 1px solid #e0e0e0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        
        .evaluation-item {
            margin: 1.5rem 0;
            padding: 1.5rem;
            background-color: #f8f9fa;
            border-left: 4px solid #0066cc;
            border-radius: 0 8px 8px 0;
        }
        
        /* Comment Styles */
        .comment {
            color: #666;
            font-style: italic;
            margin-top: 1rem;
            line-height: 1.6;
        }
        
        /* Learning Strategy Styles */
        .learning-strategy {
            margin-top: 1.5rem;
            padding: 1.5rem;
            background-color: #e8f4ff;
            border-radius: 8px;
            border: 1px solid #b8daff;
        }
        
        /* Additional Notes Styles */
        .additional-notes {
            margin-top: 1.5rem;
            padding: 1.5rem;
            background-color: #fff3cd;
            border-radius: 8px;
            border: 1px solid #ffeeba;
        }
        
        /* Typography Improvements */
        h1 {
            color: #1a1a1a;
            margin-bottom: 1.5rem;
            font-size: 2.5rem !important;
            font-weight: 700 !important;
        }
        
        h2 {
            color: #2c3e50;
            margin: 1.5rem 0 1rem 0;
            font-size: 2rem !important;
        }
        
        h3 {
            color: #34495e;
            margin: 1.25rem 0 0.75rem 0;
            font-size: 1.5rem !important;
        }
        
        p {
            line-height: 1.7;
            margin-bottom: 1rem;
        }
        
        /* List Styles */
        ul, ol {
            margin: 1rem 0;
            padding-left: 1.5rem;
        }
        
        li {
            margin: 0.5rem 0;
            line-height: 1.6;
        }
        
        /* Tab Styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 1rem;
            margin-bottom: 1rem;
        }
        
        .stTabs [data-baseweb="tab"] {
            padding: 1rem 1.5rem;
            font-weight: 500;
        }
        
        /* Expander Styling */
        .streamlit-expanderHeader {
            font-size: 1.1rem !important;
            font-weight: 600 !important;
            color: #2c3e50 !important;
            padding: 1rem !important;
        }
        
        /* Video Link Styling */
        .video-link {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin: 1rem 0;
        }
        
        .video-link svg {
            width: 24px;
            height: 24px;
        }
        
        /* Sidebar Improvements */
        .css-1d391kg {
            padding: 2rem 1rem;
        }
        
        /* Custom Classes for Specific Elements */
        .section-header {
            border-bottom: 2px solid #e0e4e8;
            padding-bottom: 0.75rem;
            margin: 2rem 0 1.5rem 0;
        }
        
        .highlight-box {
            background-color: #e8f4ff;
            padding: 1.5rem;
            border-radius: 8px;
            margin: 1.5rem 0;
            border: 1px solid #b8daff;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
        /* Hide radio buttons but keep labels clickable */
        div[data-testid="stSidebarNav"] div[role="radiogroup"] label {
            cursor: pointer;
            width: 100%;
            padding: 0.5rem;
            display: block;
        }
        
        /* Hide the actual radio button */
        div[data-testid="stSidebarNav"] div[role="radiogroup"] input[type="radio"] {
            display: none;
        }
        
        /* Style for the text */
        div[data-testid="stSidebarNav"] div[role="radiogroup"] label span p {
            font-size: 1rem;
            margin: 0;
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
        }
        
        /* Hover effect */
        div[data-testid="stSidebarNav"] div[role="radiogroup"] label:hover span p {
            background-color: rgba(151, 166, 195, 0.15);
        }

        /* Remove default container styles */
        section[data-testid="stSidebar"] > div {
            padding-top: 2rem;
        }

        /* Hide top padding in radio group */
        div[role="radiogroup"] > div {
            margin-top: 0 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar navigation
    with st.sidebar:
        st.title("Navigation")
        
        # Create navigation using radio buttons
        selected_page = st.radio(
            label="Navigation",
            options=[
                "Learning Journey Overview",
                "Oral Presentation 1",
                "Oral Presentation 2",
                "Development & Reflections"
            ],
            label_visibility="collapsed"
        )

    # Display the selected page
    if selected_page == "Learning Journey Overview":
        show_overview()
    elif selected_page == "Oral Presentation 1":
        show_presentation_one()
    elif selected_page == "Oral Presentation 2":
        show_presentation_two()
    else:
        show_development()

def show_overview():
    st.title("🎯 My Journey in Public Speaking Development")
    
    st.markdown("""
    <div class="learning-journey">
    <h2 style='margin-top: 0;'>Welcome to My Learning Portfolio</h2>
    This collection documents my growth as a public speaker, representing my commitment to developing 
    effective presentation skills through practice, reflection, and continuous improvement.
    
    <div class="highlight-box">
    <h3 style='margin-top: 0;'>Learning Objectives</h3>
    
    1. **Develop Confident Delivery**
       - Master engaging presentation techniques
       - Build stage presence
    
    2. **Create Impactful Content**
       - Craft audience-focused messages
       - Develop actionable takeaways
    
    3. **Perfect Non-verbal Communication**
       - Enhance body language
       - Improve gesture effectiveness
    
    4. **Implement Systematic Improvement**
       - Learn from feedback
       - Apply continuous refinement
    </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2 class='section-header'>Portfolio Structure</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="milestone">
        <h3 style='margin-top: 0;'>Oral Presentation 1: Foundation Building</h3>
        
        • Practice & Final Recordings<br>
        • Detailed Feedback Analysis<br>
        • Implementation Strategy
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="milestone">
        <h3 style='margin-top: 0;'>Oral Presentation 2: Skill Development</h3>
        
        • Applied Learning<br>
        • Growth Evidence<br>
        • Continued Development
        </div>
        """, unsafe_allow_html=True)


def show_presentation_one():
    st.title("Oral Presentation 1: Building Foundation")
    
    # Create tabs for different sections
    tabs = st.tabs(["Practice & Self-Assessment", "Final Presentation", "Feedback Analysis", "Peer Evaluation"])
    
    with tabs[0]:
        st.subheader("Practice Recording")

        profile_image = load_image("images/IMG_1298.jpg")

        if profile_image:
            st.image(profile_image, caption="Case 1 Presentation Group", use_column_width=True)

        st.markdown(f"""
            <div class="video-container">
                <h4>Practice Session Recording</h4>
                <a href="https://bitly.cx/WTb7iC" target="_blank" class="button-link">
                    🎥 View Practice Recording
                </a>
                <p><em>Initial practice session demonstrating my baseline presentation skills</em></p>
            </div>
            
            <div class="reflection-text">
            <strong>Self-Assessment of Practice Session:</strong>
            
            This practice session was a crucial learning opportunity that helped me identify several areas for improvement:

            1. **Content Organization:**
            - Recognized the need for clearer transitions between points
            - Identified areas where examples could be more specific
            - Noted where audience engagement could be enhanced

            2. **Delivery Aspects:**
            - Observed my tendency to use non-meaningful hand gestures
            - Noticed variations in vocal projection
            - Identified opportunities for better eye contact

            3. **Learning Points:**
            - The importance of rehearsal in building confidence
            - The need for more structured timing
            - The value of recording myself for self-assessment
            </div>
            """, unsafe_allow_html=True)
    
    with tabs[1]:
        st.subheader("Final Recording")
        st.markdown(f"""
                <div class="video-container">
                    <h4>Final Graded Presentation</h4>
                    <a href="https://bitly.cx/X45Jo" target="_blank" class="button-link">
                        🎥 View Final Presentation
                    </a>
                    <p><em>Final presentation showcasing implemented improvements</em></p>
                </div>
                """, unsafe_allow_html=True)
            
    with tabs[2]:
        st.subheader("Professor's Feedback Analysis")
        st.markdown("""
            <div class="reflection-text">
            <strong>Analyzing Feedback for Growth:</strong>

            The professor's detailed feedback has provided valuable insights for my development:

            1. **Strengths Identified:**
            - Successfully identified and analyzed problems
            - Developed realistic, practical recommendations
            - Maintained appropriate audience awareness
            
            2. **Areas for Enhancement:**
            - **Making Content More Actionable:**
                * Need to provide more specific, practical examples
                * Should break down complex suggestions into implementable steps
                * Important to connect recommendations to daily operations
            
            - **Delivery Refinement:**
                * Hand gestures should be more purposeful and meaningful
                * Facial expressions can better match content tone
                * Vocal projection needs more consistency
                * Timing between group members needs better balance

            3. **Implementation Strategy:**
            To address these areas, I've developed a specific action plan:
            - Practice with recorded sessions to work on delivery aspects
            - Create detailed examples for each key point
            - Use timing markers during practice
            - Focus on matching non-verbal cues with content

            This feedback has been instrumental in shaping my approach to future presentations.
            </div>
            """, unsafe_allow_html=True)

    with tabs[3]:
        st.title("Peer Evaluation")
        
        # Body Language Evaluation Form
        with st.expander("Delivery (Body Language) Evaluation", expanded=True):

            st.markdown("""
                <div style='border: 1px solid #ddd; padding: 2rem; border-radius: 20px; margin: 2rem 0; min-height: 25px;'>
                    <h3 style='color: #333; margin: 0;'>LABU2040 Oral Presentation Peer Evaluation (delivery)</h3>
                </div>
            """, unsafe_allow_html=True)
                    
            st.markdown("**Evaluator:** Lee Te Ying, David")
            st.markdown("**Presenter:** Federico")
            
            st.markdown("### Delivery (Body Language)")
            
            st.markdown("**Overall Impression for Delivery:** Very Good (VG)")

            # Question 1
            st.markdown("""
            <div class='evaluation-item'>
                <strong>1. Did the presenter appear composed and confident?</strong><br/>
                <span style='color: #0066cc;'>Response: Yes</span><br/>
                <span style='color: #666; font-style: italic;'>
                    Comment: Federico demonstrated a remarkably confident stance throughout the presentation, maintaining professional posture while directly engaging with the audience. His natural confidence created a strong first impression and helped establish credibility with the audience. While his overall delivery was very effective, there were moments where slightly less movement could have enhanced his commanding presence even further.
                </span>
            </div>
            """, unsafe_allow_html=True)
            
            # Question 2
            st.markdown("""
            <div class='evaluation-item'>
                <strong>2. Did the presenter maintain effective eye contact with the audience?</strong><br/>
                <span style='color: #0066cc;'>Response: Yes</span><br/>
                <span style='color: #666; font-style: italic;'>
                    Comment: Federico excelled at maintaining consistent and meaningful eye contact with audience members throughout his presentation. He effectively scanned the room and connected with different segments of the audience, creating an inclusive atmosphere. His natural ability to maintain eye contact while delivering key points particularly enhanced the impact of his message and demonstrated strong audience awareness.
                </span>
            </div>
            """, unsafe_allow_html=True)
            
            # Question 3
            st.markdown("""
            <div class='evaluation-item'>
                <strong>3. Did the presenter use hand movements that seemed natural and controlled?</strong><br/>
                <span style='color: #0066cc;'>Response: Yes</span><br/>
                <span style='color: #666; font-style: italic;'>
                    Comment: Federico's hand gestures were notably professional and well-controlled, adding a natural flow to his presentation style. His movements appeared rehearsed yet authentic, never distracting from the content. The controlled nature of his gestures demonstrated good preparation and awareness of non-verbal communication techniques.
                </span>
            </div>
            """, unsafe_allow_html=True)
            
            # Question 4
            st.markdown("""
            <div class='evaluation-item'>
                <strong>4. Did the presenter use hand movements that deliberately enhanced the message?</strong><br/>
                <span style='color: #0066cc;'>Response: Yes</span><br/>
                <span style='color: #666; font-style: italic;'>
                    Comment: Federico demonstrated excellent skill in using purposeful hand gestures that effectively emphasized his key points and signposts. His movements were particularly effective when highlighting transitions and important concepts, helping the audience follow the presentation structure. The synchronization between his verbal content and gestures showed thoughtful preparation and enhanced the overall clarity of his message.
                </span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='learning-strategy'>
                <strong>Learning / Practicing Strategy Suggestion:</strong><br/>
                As someone who had the privilege of working with Federico, I would like to share some collaborative suggestions that could help both of us enhance our presentation skills further. Building on Federico's already strong foundation, we could practice together using these strategies:
                <ul>
                    <li>Perhaps we could schedule some joint practice sessions where we can give each other real-time feedback on our movements and gestures</li>
                    <li>We might find it beneficial to record our practice sessions together and review them as a team, sharing insights on what works best</li>
                    <li>We could work on developing a shared understanding of effective body language techniques that complement our team's presentation style</li>
                </ul>
                These suggestions come from a place of mutual learning, as I believe we can both benefit from exchanging feedback and strategies.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### Language (Use of Voice)")
            
            st.markdown("**Overall Impression for Use of Voice:** Very Good (VG)")

            # Question 1
            st.markdown("""
            <div class='evaluation-item'>
                <strong>1. Did the presenter sound composed and confident?</strong><br/>
                <span style='color: #0066cc;'>Response: Yes</span><br/>
                <span style='color: #666; font-style: italic;'>
                    Comment: Federico's voice projection demonstrated remarkable professionalism and confidence throughout the presentation. His clear, steady tone effectively conveyed authority while remaining approachable and engaging. The consistency in his vocal delivery helped establish a strong connection with the audience and maintained their attention throughout his speaking time.
                </span>
            </div>
            """, unsafe_allow_html=True)
            
            # Question 2
            st.markdown("""
            <div class='evaluation-item'>
                <strong>2. Did the presenter use pace, pausing, and intonation that enhance the message?</strong><br/>
                <span style='color: #0066cc;'>Response: Somewhat</span><br/>
                <span style='color: #666; font-style: italic;'>
                    Comment: Federico maintained an excellent pace that made it easy for the audience to follow and comprehend his message. His natural speaking rhythm generally enhanced the presentation flow, though there were some occasions in the second part where brief hesitations occurred. These moments, while noticeable, did not significantly impact the overall quality of his delivery, and in some ways added a thoughtful quality to his presentation style.
                </span>
            </div>
            """, unsafe_allow_html=True)
            
            # Question 3
            st.markdown("""
            <div class='evaluation-item'>
                <strong>3. Did the presenter use language that created rapport with the audience?</strong><br/>
                <span style='color: #0066cc;'>Response: Yes</span><br/>
                <span style='color: #666; font-style: italic;'>
                    Comment: Federico exhibited excellent skill in using conversational phrases that created a natural and engaging atmosphere. His choice of language effectively bridged the formal aspects of the presentation with a more accessible, audience-friendly approach. The way he incorporated engaging phrases and interactive elements demonstrated his strong ability to connect with the audience while maintaining professional standards.
                </span>
            </div>
            """, unsafe_allow_html=True)
            
            # Question 4
            st.markdown("""
            <div class='evaluation-item'>
                <strong>4. Did the presenter use language that seemed appropriate for the audience?</strong><br/>
                <span style='color: #0066cc;'>Response: Yes</span><br/>
                <span style='color: #666; font-style: italic;'>
                    Comment: Federico's language choices were consistently professional and well-suited to the academic context of the presentation. He demonstrated excellent judgment in balancing technical terminology with clear, accessible explanations. His ability to maintain this appropriate level of language throughout the presentation showcased his strong awareness of audience needs and expectations.
                </span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='learning-strategy'>
                <strong>Learning / Practicing Strategy Suggestion:</strong><br/>
                As teammates working together toward excellence in presentation skills, I'd like to share some collaborative suggestions that could benefit our entire group:
                <ol>
                    <li>We could practice our presentations together, using our combined allocated time to ensure we're each maximizing our individual portions while maintaining a cohesive group flow</li>
                    <li>Perhaps we could set up regular team practice sessions where we can work on smooth transitions between speakers and maintain consistent energy throughout</li>
                    <li>We might find it helpful to create shared cue cards or transition points that could help reduce any hesitations while maintaining our natural speaking styles</li>
                </ol>
                These suggestions stem from my belief that our combined strengths can help us deliver even more impactful presentations as a team.
            </div>
            """, unsafe_allow_html=True)

def show_presentation_two():
    st.title("Oral Presentation 2: Demonstrating Growth")
    
    with st.expander("Applied Learning & Development", expanded=True):

        st.subheader("Final Presentation")

        profile_image = load_image("images/IMG_1297.jpg")

        if profile_image:
            st.image(profile_image, caption="Case 2 Presentation Group", use_column_width=True)

        st.markdown("""
        <div class="video-container">
            <h4>Enhanced Presentation Skills Demonstration</h4>
            <a href="https://bitly.cx/aH7GCM" target="_blank" class="button-link">
                🎥 View Presentation
            </a>
            <p><em>Demonstrating improved presentation techniques and applied learning</em></p>
        </div>
        
        <div class="reflection-text">
        <strong>Evidence of Growth and Development:</strong>

        This presentation demonstrates my commitment to implementing previous feedback and showing growth:

        1. **Enhanced Content Delivery:**
           - Incorporated specific, actionable examples
           - Improved structure and flow
           - Better balanced theoretical and practical content

        2. **Refined Presentation Skills:**
           - More purposeful use of gestures
           - Improved vocal projection and pacing
           - Better eye contact and audience engagement
           - Enhanced facial expressions matching content

        3. **Strategic Improvements:**
           - Implemented structured timing
           - Used clearer transitions
           - Enhanced audience interaction
        </div>
        """, unsafe_allow_html=True)

def show_development():
    st.title("Continuous Development & Learning Evidence")
    
    # Combined expander with all content
    with st.expander("Video Learning Resources", expanded=True):
        # Introduction section
        st.markdown("""
        <div class="reflection-text">
        <strong>Video Learning Resources & Development Journey:</strong>
        
        Throughout this learning journey, I've actively sought resources to improve my presentation skills,
        focusing on professional development through various video resources and practical techniques. Here are
        the key learning materials and their impact on my development:
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns([0.95, 0.05])
        with col1:
            # Video 1
            st.markdown("""
            **1. The 3 Magic Ingredients of Amazing Presentations by Phil Waknell**  
            [🎥 Watch Video](https://www.youtube.com/watch?v=yoD8RMq2OkU)
            
            Key Takeaways:
            - Clear message definition is essential for effective communication
            - Logical structure guides audience through the narrative
            - Interactive elements make presentations more memorable
            - Combining these elements transforms standard presentations
            - Focus on audience engagement and connection
            """)

            # Video 2
            st.markdown("""
            **2. 4 Essential Body Language Tips by Dananjaya Hettiarachchi**  
            [🎥 Watch Video](https://www.youtube.com/watch?v=ZK3jSXYBNak)
            
            Key Takeaways:
            - Maintain open and confident posture for authority projection
            - Use purposeful hand movements to emphasize points
            - Align facial expressions with message content
            - Establish consistent eye contact for trust building
            - Focus on non-verbal communication effectiveness
            """)

            # Video 3
            st.markdown("""
            **3. HOW TO Give a Great Presentation - 7 Presentation Skills and Tips**  
            [🎥 Watch Video](https://www.youtube.com/watch?v=MnIPpUiTcRc)
            
            Key Takeaways:
            - Begin with a powerful opening to capture attention
            - Understand and adapt to your audience's needs
            - Structure content with clear beginning, middle, and end
            - Use visual aids effectively without cluttering
            - Practice delivery to build confidence
            - Manage nervousness through preparation
            - Encourage audience interaction and engagement
            """)

        # Condensed Development Journey and Implementation
        st.markdown("""
        <div class="reflection-text">
        <strong>Development Journey & Implementation Strategy:</strong>
        
        Based on these valuable resources, I'm focusing on enhancing my presentation skills through regular practice and recording sessions. My key areas of development include message structure, body language refinement, and audience engagement techniques. Moving forward, I'll continue to apply these learnings while seeking new opportunities to expand my presentation contexts.
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()