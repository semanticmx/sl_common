import pytest
from sl_common.rest.responses import success_response, error_response


def test_success_response():
    # Test basic success response
    response = success_response("Operation successful", {"key": "value"}, 200)
    assert response["status"] == "success"
    assert response["message"] == "Operation successful"
    assert response["data"] == {"key": "value"}
    assert response["code"] == 200

    # Test success response with created status
    response = success_response("Resource created successfully", {"id": 1}, 201)
    assert response["status"] == "created"
    assert response["message"] == "Resource created successfully"
    assert response["data"] == {"id": 1}
    assert response["code"] == 201

    # Test success response with no data provided
    response = success_response("No data provided")
    assert response["status"] == "success"
    assert response["message"] == "No data provided"
    assert response["data"] == {}
    assert response["code"] == 200


def test_error_response():
    # Test basic error response
    response = error_response("Invalid request", [{"field": "username", "message": "Username is required"}], 400)
    assert response["status"] == "bad_request"
    assert response["message"] == "Invalid request"
    assert response["errors"] == [{"field": "username", "message": "Username is required"}]
    assert response["code"] == 400

    # Test unauthorized error response
    response = error_response("Unauthorized access", code=401)
    assert response["status"] == "unauthorized"
    assert response["message"] == "Unauthorized access"
    assert response["errors"] == []
    assert response["code"] == 401

    # Test server error response
    response = error_response("Internal server error", code=500)
    assert response["status"] == "server_error"
    assert response["message"] == "Internal server error"
    assert response["errors"] == []
    assert response["code"] == 500
