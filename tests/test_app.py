import pytest

import ai_service

from app import create_app
from validators import (
    validate_attendance,
    AttendanceValidationError
)

@pytest.mark.parametrize(
    "value, expected",
    [
        ("85", 85.0),
        ("72.5", 72.5),
        ("0", 0.0),
        ("100", 100.0),
    ]
)
def test_valid_attendance(value, expected):

    assert validate_attendance(value) == expected

@pytest.mark.parametrize(
    "value",
    [
        "-10",
        "150",
        "hello",
        "NaN",
        "Infinity",
        "-Infinity",
        "",
        "   ",
        None
    ]
)
def test_invalid_attendance(value):

    with pytest.raises(AttendanceValidationError):
        validate_attendance(value)

@pytest.fixture
def client():

    app = create_app({
        "TESTING": True,
        "GROQ_API_KEY": "test-key",
        "GROQ_MODEL": "test-model"
    })

    with app.test_client() as client:
        yield client

def test_home_page(client):

    response = client.get("/")

    assert response.status_code == 200
    assert b"Student Attendance Insight Generator" in response.data

def test_invalid_form_input(client):

    response = client.post(
        "/",
        data={"user_input": "150"}
    )

    assert response.status_code == 200
    assert b"Attendance must be between 0 and 100." in response.data

def test_successful_feedback(client, monkeypatch):

    def mock_feedback(percentage, api_key, model):
        return "Attendance Classification: Good"

    monkeypatch.setattr(
        ai_service,
        "generate_feedback",
        mock_feedback
    )

    response = client.post(
        "/",
        data={"user_input": "90"}
    )

    assert response.status_code == 200
    assert b"Attendance Classification: Good" in response.data

def test_missing_api_key(client, monkeypatch):

    app = client.application
    app.config["GROQ_API_KEY"] = None

    response = client.post(
        "/",
        data={"user_input": "90"}
    )

    assert response.status_code == 200
    assert b"AI service is not configured" in response.data

def test_ai_service_failure(client, monkeypatch):

    def mock_failure(**kwargs):
        raise ai_service.AIServiceError("Provider unavailable")

    monkeypatch.setattr(
        ai_service,
        "generate_feedback",
        mock_failure
    )

    response = client.post(
        "/",
        data={"user_input": "90"}
    )

    assert response.status_code == 200
    assert b"Unable to generate feedback" in response.data