import os
import logging

from flask import Flask, render_template
from flask import request

from dotenv import load_dotenv

import ai_service

from validators import (
    validate_attendance,
    AttendanceValidationError
)


load_dotenv()


def create_app(test_config=None):

    app = Flask(__name__)

    app.config.from_mapping(
        GROQ_API_KEY=os.getenv("GROQ_API_KEY"),
        GROQ_MODEL=os.getenv(
            "GROQ_MODEL",
            "openai/gpt-oss-120b"
        )
    )

    if test_config:
        app.config.update(test_config)

    logging.basicConfig(level=logging.INFO)

    @app.route("/", methods=["GET", "POST"])
    def home():

        result = ""
        error = ""
        user_input = ""

        if request.method == "POST":

            user_input = request.form.get(
                "user_input", ""
            )

            try:

                percentage = validate_attendance(
                    user_input
                )

                result = ai_service.generate_feedback(
                    percentage=percentage,
                    api_key=app.config.get("GROQ_API_KEY"),
                    model=app.config.get("GROQ_MODEL")
                )

            except AttendanceValidationError as exc:

                error = str(exc)

            except ai_service.MissingAPIKeyError:

                app.logger.error(
                    "Groq API key is missing."
                )

                error = (
                    "AI service is not configured. "
                    "Please contact the administrator."
                )

            except ai_service.AIServiceError:

                error = (
                    "Unable to generate feedback. "
                    "Please try again later."
                )

            except Exception:

                app.logger.exception(
                    "Unexpected application error."
                )

                error = (
                    "An unexpected error occurred. "
                    "Please try again."
                )

        return render_template(
            "index.html",
            result=result,
            error=error,
            user_input=user_input
        )

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)