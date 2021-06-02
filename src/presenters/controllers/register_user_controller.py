from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers.http_models import HttpReponse, HttpRequest
from typing import Type
from src.domain.use_cases import RegisterUser


class RegisterUserController:
    """Controller to handle create user request"""

    def __init__(self, register_user_use_case: Type[RegisterUser]):
        self.register_user_use_case = register_user_use_case

    def handle(self, http_request: Type[HttpRequest]) -> HttpReponse:
        """Method to handle the user creation"""

        response = None
        if http_request.body:
            body_params = http_request.body.keys()
            if "name" in body_params and "password" in body_params:
                name = http_request.body["name"]
                password = http_request.body["password"]
                response = self.register_user_use_case.register(
                    name=name, password=password
                )
            else:
                http_error = HttpErrors.error_400()
                return HttpReponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                return HttpReponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )
            print(response)
            return HttpReponse(status_code=200, body=response["Data"])

        http_error = HttpErrors.error_400()
        return HttpReponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
