import os

from dotenv import load_dotenv
from google import genai


MODEL_NAME = "gemini-2.5-flash"


def main() -> None:
    load_dotenv()
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError("Missing API_KEY. Add it to your .env file before running this script.")

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents="Dis-moi Bonjour en francais et confirme que tu fonctionnes",
    )

    print(response.text)


if __name__ == "__main__":
    main()
