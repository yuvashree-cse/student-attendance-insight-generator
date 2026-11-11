import logging

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

logger = logging.getLogger(__name__)

class AIServiceError(Exception):
    """Raised when AI feedback generation fails."""

class MissingAPIKeyError(AIServiceError):
    """Raised when the Groq API key is unavailable."""

def generate_feedback(percentage, api_key, model):

    if not api_key:
        raise MissingAPIKeyError(
            "Groq API key is not configured."
        )

    prompt = ChatPromptTemplate.from_template("""
You are a student attendance advisor.

Student attendance: {user_input}%

Generate feedback using this exact format:

Attendance Classification: [Excellent/Good/Average/Poor]

Performance Analysis:
Write exactly 2 short sentences.

Improvement Tips:
1. [Short tip]
2. [Short tip]
3. [Short tip]

Rules:
- Keep the response under 80 words.
- Use simple English.
- Do not generate tables.
- Do not make assumptions about student behavior.
- Below 75%: Poor.
- 75% to below 85%: Average.
- 85% to below 95%: Good.
- 95% to 100%: Excellent.
""")

    try:

        llm = ChatGroq(
            model=model,
            api_key=api_key,
            temperature=0.2,
            max_retries=2
        )

        chain = prompt | llm

        response = chain.invoke({
            "user_input": percentage
        })

        feedback = response.content

        if not isinstance(feedback, str) or not feedback.strip():
            raise AIServiceError(
                "The AI model returned an empty response."
            )

        return feedback.strip()

    except AIServiceError:
        raise

    except Exception as error:

        logger.exception(
            "AI feedback generation failed."
        )

        raise AIServiceError(
            "Unable to generate feedback at the moment."
        ) from error