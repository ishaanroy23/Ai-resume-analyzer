from groq import Groq
from system_prompt import analysis_prompt, critique_prompt
from dotenv import load_dotenv
import os

def generate_response(resume_text: str, job_description: str, choice: str) -> str:
    load_dotenv()

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    if choice == 'Resume Analyzer':
        sys_prompt = analysis_prompt
        user_prompt = f'Analyze my resume against this job:\n\n{resume_text}\n\n{job_description}'

    elif choice == 'Resume Critique':
        sys_prompt = critique_prompt
        user_prompt = f'Critique my resume:\n\n{resume_text}'

    else:
        raise ValueError(f"Invalid choice received: {choice!r}")

    response = client.chat.completions.create(
        model='openai/gpt-oss-20b',
        messages=[
            {'role': 'system', 'content': sys_prompt},
            {'role': 'user', 'content': user_prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
