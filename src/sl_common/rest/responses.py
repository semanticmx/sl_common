from typing import Any, List, Dict, Optional


def success_response(message: str, data: Optional[Dict[str, Any]] = None, code: int = 200) -> Dict[str, Any]:
    """
    Creates a standardized success response.

    Args:
        message (str): A message describing the success.
        data (Optional[Dict[str, Any]]): Additional data for the response.
        code (int): HTTP status code, default is 200.

    Returns:
        dict: A dictionary representing the success response.
    """
    return {
        "status": get_status_from_code(code),
        "message": message,
        "data": data if data is not None else {},
        "code": code
    }


def error_response(message: str, errors: Optional[List[Dict[str, Any]]] = None, code: int = 400) -> Dict[str, Any]:
    """
    Creates a standardized error response.

    Args:
        message (str): A message describing the error.
        errors (Optional[List[Dict[str, Any]]]): A list of specific error details.
        code (int): HTTP status code, default is 400.

    Returns:
        dict: A dictionary representing the error response.
    """
    return {
        "status": get_status_from_code(code),
        "message": message,
        "errors": errors if errors is not None else [],
        "code": code
    }


def get_status_from_code(code: int) -> str:
    """
    Maps the HTTP status code to a descriptive status string.

    Args:
        code (int): The HTTP status code.

    Returns:
        str: The descriptive status corresponding to the HTTP code.
    """
    if 200 <= code < 300:
        if code == 201:
            return "created"
        return "success"
    elif code == 400:
        return "bad_request"
    elif code == 401:
        return "unauthorized"
    elif code == 403:
        return "forbidden"
    elif code == 404:
        return "not_found"
    elif 500 <= code < 600:
        return "server_error"
    else:
        return "unknown_status"
