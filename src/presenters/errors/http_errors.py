class HttpErrors:
    """Mapping possible exceptions for the requests"""

    @staticmethod
    def error_422():
        """Unprocessable entity"""
        return {"status_code": 422, "body": {"error": "Unprocessable Entity"}}

    @staticmethod
    def error_400():
        """Http Bad Request"""
        return {"status_code": 400, "body": {"error": "Bad Request"}}
