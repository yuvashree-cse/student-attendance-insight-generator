# 🎓 Student Attendance Insight Generator

An AI-powered web application that analyzes student attendance percentages and generates personalized attendance insights, performance classifications, and improvement suggestions.

Built using **Python, Flask, LangChain, and Groq**, this project combines AI-powered feedback generation with structured backend validation and error handling.

## ✨ Features

- **AI-Powered Attendance Analysis:** Generates feedback based on the student's attendance percentage.
- **Attendance Classification:** Categorizes attendance into four levels:
  - Excellent: 95%–100%
  - Good: 85%–below 95%
  - Average: 75%–below 85%
  - Poor: Below 75%
- **Performance Analysis:** Provides a short explanation of the student's attendance status.
- **Improvement Suggestions:** Generates three practical suggestions to improve attendance.
- **Input Validation:** Rejects empty, non-numeric, infinite, and out-of-range values.
- **Error Handling:** Handles missing API credentials and AI service failures gracefully.
- **Modular Backend:** Separates application logic, input validation, and AI functionality.
- **Automated Testing:** Uses pytest to verify application behavior and validation logic.

## 🛠️ Tech Stack

| Category               | Technologies   |
| ---------------------- | -------------- |
| Programming Language   | Python         |
| Frontend               | HTML, CSS      |
| Backend                | Flask          |
| AI Framework           | LangChain      |
| AI Model Provider      | Groq           |
| Environment Management | python-dotenv  |
| Testing                | pytest         |
| Version Control        | Git and GitHub |

## 📁 Project Structure

```text
Student-Attendance-Insight-Generator/
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
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ How It Works

1. The user enters their attendance percentage through the web interface.
2. Flask receives the submitted input.
3. The validation module checks whether the input is valid and within the range of 0–100.
4. The validated percentage is passed to the AI service.
5. LangChain constructs the prompt and communicates with the configured Groq language model.
6. The AI generates an attendance classification, performance analysis, and improvement suggestions.
7. Flask displays the generated insights on the web page.

## 🚀 Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate into the project directory:

```bash
cd Student-Attendance-Insight-Generator
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory.

Add your Groq API credentials:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-120b
```

Replace `your_groq_api_key` with your actual API key.

**Important:** Never upload your `.env` file or expose your API key on GitHub.

### 5. Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## 🧪 Running Automated Tests

This project uses pytest to test input validation and Flask application behavior.

Run the test suite using:

```bash
python -m pytest -v
```

### Test Coverage

The current test suite verifies:

- Valid attendance percentages.
- Invalid numeric inputs.
- Empty input handling.
- Boundary values such as 0 and 100.
- Rejection of NaN and Infinity values.
- Successful homepage rendering.
- Invalid form submissions.
- Successful feedback generation using a mocked AI service.
- Missing API key handling.
- AI service failure handling.

**Latest Test Result:**

```text
18 passed
0 failed
```

## 🏗️ Backend Architecture

The backend follows a modular structure to improve maintainability and separation of responsibilities.

| File                | Responsibility                                                 |
| ------------------- | -------------------------------------------------------------- |
| `app.py`            | Flask application, routes, configuration, and request handling |
| `validators.py`     | Attendance input validation and validation errors              |
| `ai_service.py`     | LangChain prompt construction and Groq API communication       |
| `tests/test_app.py` | Automated tests for validation and application behavior        |

## 🔐 Error Handling and Validation

The application includes backend safeguards to handle:

- Missing attendance values.
- Non-numeric input.
- Attendance values outside the 0–100 range.
- Non-finite numeric values.
- Missing Groq API credentials.
- AI service failures.
- Unexpected application errors.

These checks help prevent invalid inputs from reaching the AI service and provide meaningful error messages to users.

## 🎯 Project Objectives

This project was developed to gain practical experience in:

- Building AI-powered web applications.
- Integrating Large Language Models using LangChain.
- Connecting external AI services through APIs.
- Developing backend applications with Flask.
- Implementing input validation and error handling.
- Writing automated tests using pytest.
- Organizing Python applications using modular architecture.
- Managing source code using Git and GitHub.

## 🔮 Future Improvements

Potential enhancements for future versions include:

- Student attendance history and tracking.
- Database integration for storing attendance records.
- Interactive attendance analytics and visualizations.
- More detailed and structured AI-generated reports.
- Downloadable attendance reports.
- User authentication and personalized dashboards.
- API endpoints for external integrations.
- Production deployment and performance optimization.
- Rate limiting and additional security protections.

## 👩‍💻 Author

**Yuvashree C**

B.E. Computer Science and Engineering Student

Interested in Artificial Intelligence, Large Language Models, and AI-powered application development.

---

⭐ If you find this project interesting, consider giving the repository a star!