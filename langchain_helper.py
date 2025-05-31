import os
from pathlib import Path
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
 
# Load environment variables
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)
 
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY is not set. Check your .env file.")
 
# Initialize Groq LLM
llm = ChatGroq(
    temperature=0.7,
    model_name="llama3-8b-8192",
    api_key=groq_api_key
)
 
def generate_weekend_plan(city: str, preferences: str):
    prompt_itinerary_name = PromptTemplate(
        input_variables=["city", "preferences"],
        template="Suggest ONE catchy and creative weekend itinerary name for a trip in {city} focused on {preferences}. Only return the name."
    )
 
    name_chain = LLMChain(llm=llm, prompt=prompt_itinerary_name)
    itinerary_name = name_chain.run({"city": city, "preferences": preferences}).strip()
 
    prompt_activities = PromptTemplate(
        input_variables=["itinerary_name", "city", "preferences"],
        template=(
            "Suggest exactly 5 engaging activities for the weekend itinerary named '{itinerary_name}', "
            "planned for the city {city} with focus on {preferences}. "
            "Return ONLY a comma-separated list of activity titles with short descriptions."
        )
    )
 
    activities_chain = LLMChain(llm=llm, prompt=prompt_activities)
    activities_raw = activities_chain.run({
        "itinerary_name": itinerary_name,
        "city": city,
        "preferences": preferences
    })
 
    activities = [act.strip() for act in activities_raw.split(",") if act.strip()]
    return itinerary_name, activities