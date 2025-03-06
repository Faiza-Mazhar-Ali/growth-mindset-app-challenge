import streamlit as st
import pandas as pd
import os
from PIL import Image

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Quiz", "Daily Challenge", "Success Stories", "Progress Tracker"])

# Home Page
if page == "Home":
    st.title("Growth Mindset Challenge 🌱")
    st.write("""
    Welcome to the Growth Mindset Challenge Web App! 🚀  
    This app will help you develop a growth mindset through challenges, quizzes, and motivation.  
    Use the sidebar to explore different sections.
    """)
    # Display the image
    image = Image.open(r"F:\growth mindset challenge\image1.jpg")
    st.image(image, caption="Embrace Growth!", use_container_width=True)
    
# Placeholder for other pages
#Quiz section
elif page == "Quiz":
    st.title("Growth Mindset Quiz 🎯")

    questions = [
        {
            "question": "What is a growth mindset?",
            "options": ["Believing intelligence is fixed", "Believing abilities can be developed", "Avoiding challenges", "Focusing only on talent"],
            "answer": "Believing abilities can be developed"
        },
        {
            "question": "Which of the following is an example of a growth mindset?",
            "options": ["Giving up when facing challenges", "Seeing failure as a learning opportunity", "Avoiding feedback", "Believing success comes without effort"],
            "answer": "Seeing failure as a learning opportunity"
        },
        {
            "question": "How should you react to failure?",
            "options": ["Quit immediately", "Blame others", "See it as a learning experience", "Ignore it"],
            "answer": "See it as a learning experience"
        }
    ]

   


#Daily Challenge section
elif page == "Daily Challenge":
    st.title("Daily Challenge 🔥")

    challenges = [
        "Reflect on a recent mistake and write down what you learned from it.",
        "Step out of your comfort zone: try a new hobby or activity today.",
        "Seek feedback on a recent project and identify areas for improvement.",
        "Set a learning goal for the week and outline steps to achieve it.",
        "Embrace a challenging task you've been avoiding and commit to tackling it today."
    ]

    import random
    daily_challenge = random.choice(challenges)
    st.subheader("Your Challenge for Today:")
    st.write(daily_challenge)

    if st.button("Show Another Challenge"):
        daily_challenge = random.choice(challenges)
        st.write(daily_challenge)


#Success Stories Section
elif page == "Success Stories":
    st.title("Success Stories 🌟")

    stories = [
        {
            "name": "Thomas Edison",
            "story": "Failed thousands of times before inventing the light bulb. He viewed each failure as a step closer to success."
        },
        {
            "name": "J.K. Rowling",
            "story": "Faced multiple rejections before 'Harry Potter' was published. She persevered and is now one of the best-selling authors."
        },
        {
            "name": "Michael Jordan",
            "story": "Was cut from his high school basketball team. He used this setback as motivation to become one of the greatest basketball players."
        }
    ]

    for story in stories:
        st.subheader(story["name"])
        st.write(story["story"])
        st.write("---")


#Progress Tracker Section
elif page == "Progress Tracker":
    st.title("Progress Tracker 📈")
    st.write("Reflect on your recent experiences and track your growth mindset journey.")

    # Define the CSV file path
    csv_file = os.path.join(os.getcwd(), "reflections.csv")


    # Check if the CSV file exists; if not, create it with headers
    if not os.path.exists(csv_file):
        df = pd.DataFrame(columns=["Date", "Challenge", "Approach", "Lessons"])
        df.to_csv(csv_file, index=False)

    # Load existing reflections
    df = pd.read_csv(csv_file)

    with st.form("reflection_form"):
        challenge = st.text_area("**Reflect on a recent challenge:**", "")
        approach = st.text_area("**How did you overcome it?**", "")
        lessons = st.text_area("**What did you learn from this experience?**", "")
        submitted = st.form_submit_button("Save Reflection")

    if submitted:
        if challenge and approach and lessons:
         new_reflection = pd.DataFrame([{
            "Date": pd.Timestamp.now(),
            "Challenge": challenge,
            "Approach": approach,
            "Lessons": lessons
        }])

        df = pd.concat([df, new_reflection], ignore_index=True)  # Use pd.concat()
        df.to_csv(csv_file, index=False)
        st.success("Your reflection has been saved!")
    else:
        st.error("Please fill out all fields before submitting.")


