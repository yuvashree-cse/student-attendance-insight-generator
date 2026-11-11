# 🎓 Student Attendance Insight Generator

An AI-powered student attendance analysis application built using **Python, Flask, LangChain, and Groq**.

The application allows students to enter their attendance percentage and receive AI-generated feedback, including an attendance classification, performance analysis, and improvement suggestions.

## 📌 Project Overview

The Student Attendance Insight Generator aims to make attendance tracking and analysis more informative for students.

Instead of simply displaying an attendance percentage, the application uses a Large Language Model (LLM) to generate understandable feedback and practical suggestions based on the entered attendance value.

## ✨ Features

- **Attendance Input:** Enter attendance percentages between 0 and 100.
- **AI-Powered Analysis:** Generate feedback using a Groq-hosted language model through LangChain.
- **Attendance Classification:** Classify attendance into Excellent, Good, Average, or Poor categories.
- **Performance Analysis:** Receive a short explanation of the entered attendance percentage.
- **Improvement Suggestions:** Get three practical attendance improvement tips.
- **Input Validation:** Reject invalid attendance values.
- **Responsive Interface:** Use a simple dark-themed interface with blue and cyan accents.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Backend web framework |
| LangChain | LLM integration and prompt management |
| Groq | Language model inference |
| HTML | Webpage structure |
| CSS | Interface styling |
| python-dotenv | Environment variable management |

## 📂 Project Structure

```text
student-attendance-insight-generator/
│
├── tests/
│   └── test_app.py
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── validators.py
├── ai_service.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-GITHUB-USERNAME/student-attendance-insight-generator.git
```

### 2. Navigate to the project directory

```bash
cd student-attendance-insight-generator
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file in the project root directory.

Add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace the placeholder with your actual API key.

**Important:** Never upload your `.env` file or expose your API key publicly.

## 🚀 Running the Application

After completing the installation and configuration:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

Enter an attendance percentage and click **Generate Feedback** to receive AI-generated attendance insights.

## 🔄 Application Workflow

1. The student enters an attendance percentage.
2. Flask receives the submitted value.
3. The backend validates that the value is between 0 and 100.
4. LangChain passes the input to the configured Groq language model.
5. The language model generates attendance feedback.
6. Flask sends the generated result to the webpage.
7. The student views the attendance insights.

## 📊 Attendance Classification

The current prompt uses the following classification thresholds:

| Attendance | Classification |
|---|---|
| Below 75% | Poor |
| 75% – 84% | Average |
| 85% – 94% | Good |
| 95% – 100% | Excellent |

These are configurable project thresholds and may differ from an institution's official attendance policy.

## 🔮 Future Enhancements

The following features are planned for future versions:

- Automatic attendance percentage calculation using classes attended and total classes.
- Attendance eligibility checker based on a configurable minimum requirement.
- Calculator for the number of classes required to reach a target percentage.
- Interactive attendance dashboard with progress indicators.
- Attendance history and data storage using SQLite or PostgreSQL.
- Improved analytics and visual representations.
- Application deployment for public access.

## 🎯 Project Objective

This project is being developed to explore practical AI application development by combining Python web development, prompt engineering, LLM integration, backend validation, and user interface design.

## 👩‍💻 Author

**Yuvashree C**

Computer Science and Engineering Student

GitHub: https://github.com/yuvashree-cse

---

⭐ If you find this project interesting, consider giving the repository a star!