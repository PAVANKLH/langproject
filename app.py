import streamlit as st
from langchain_helper import generate_weekend_plan
 
# Page configuration
st.set_page_config(page_title="🗓️ Weekend Planner", layout="centered")
 
# App title
st.title("🗺️ Weekend Planner with LangChain + Groq")
 
# Form input
with st.form("planner_form"):
    city = st.text_input("📍 Enter your city", value="San Francisco")
    preferences = st.text_input("🎯 Enter your interests (comma-separated)", value="outdoors, food, and art")
    submitted = st.form_submit_button("✨ Generate Weekend Plan")
 
# Generate itinerary on form submission
if submitted:
    with st.spinner("🧠 Thinking and planning your perfect weekend..."):
        try:
            itinerary_name, activities = generate_weekend_plan(city, preferences)
 
            st.success(f"🗓️ Your Weekend Itinerary: **{itinerary_name}**")
 
            st.markdown("### 📋 Recommended Activities")
            for i, act in enumerate(activities, 1):
                st.markdown(f"**{i}.** {act}")
 
        except Exception as e:
            st.error(f"❌ Something went wrong: {e}")