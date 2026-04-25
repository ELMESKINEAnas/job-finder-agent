import os
from google import genai
from dotenv import load_dotenv
import instructor
from src.models.job_offer import JobOffer


#Load Enviromment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")

raw_client = genai.Client(api_key=API_KEY)

client = instructor.from_genai(raw_client)



def extract_job_offer(text:str) -> JobOffer :

    return client.chat.completions.create(
        model = "gemini-2.5-flash",
        response_model= JobOffer,
        messages= [{"role" : "user" , "content" : f"Extract the job offer information from this text: {text}"}]
    )