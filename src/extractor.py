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
    if(not text):
        raise ValueError("Please enter a valid text")
    else:
        return client.chat.completions.create(
            model = "gemini-2.5-flash",
            response_model= JobOffer,
            messages= [{"role" : "user" , 
                        "content" : f"""
                        Extract the job offer information from this text
                        If the text is not a job offer, return empty strings for required fields and null for optional fields.
                        Do not invent or hallucinate information that is not present in the text.
                        Text: {text}"""}]
        )
    

result = extract_job_offer("Bonjour je m'appelle Anas")

print(result)