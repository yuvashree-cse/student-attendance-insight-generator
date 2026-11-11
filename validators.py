import math

class AttendanceValidationError(ValueError):
    """Raised when attendance input is invalid."""

def validate_attendance(value):

    if value is None or not str(value).strip():
        raise AttendanceValidationError(
            "Attendance percentage is required."
        )

    try:
        percentage = float(value)

    except (ValueError, TypeError):
        raise AttendanceValidationError(
            "Please enter a valid numeric percentage."
        )

    if not math.isfinite(percentage):
        raise AttendanceValidationError(
            "Attendance must be a finite number."
        )

    if not 0 <= percentage <= 100:
        raise AttendanceValidationError(
            "Attendance must be between 0 and 100."
        )

    return percentage