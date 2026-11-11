import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
app = Flask(__name__)

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY")
)

prompt = ChatPromptTemplate.from_template("""
You are a student attendance advisor.

Student attendance: {user_input}%

Generate feedback using EXACTLY this format:

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
- Do not make assumptions about the student's behavior.
- Classify below 75% as Poor, 75-84% as Average,
  85-94% as Good, and 95-100% as Excellent.
""")

chain = prompt | llm

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    user_input = ""

    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()

        try:
            percentage = float(user_input)
            if not 0 <= percentage <= 100:
                raise ValueError()

            result = chain.invoke({
                "user_input": percentage
            }).content

        except ValueError:
            result = "Please enter a valid percentage between 0 and 100."
        except Exception:
            result = "Error generating feedback."

    return render_template(
        "index.html",
        result=result,
        user_input=user_input
    )

if __name__ == "__main__":
    app.run(debug=True)