# Job Finder Agent

Initial project scaffold for a job-finder assistant.

The repository currently includes a simple Gemini API connectivity script in `test_gemini.py` so the environment and credentials can be verified before the larger agent workflow is built out.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file with:

```env
API_KEY=your_gemini_api_key
```

## Run

```bash
python test_gemini.py
```

If your API key is configured correctly, the script will request a short French response from Gemini and print the result.
