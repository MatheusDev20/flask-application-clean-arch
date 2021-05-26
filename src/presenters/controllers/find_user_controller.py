from typing import Type
from src.domain.use_cases import FindUser
from src.presenters.helpers.http_models import HttpRequest, HttpReponse
from src.presenters.errors.http_errors import HttpErrors


class FindUserController:
    """Class to define the controller to handle Find User"""

    def __init__(self, find_user_use_case: Type[FindUser]):
        self.find_user_use_case = find_user_use_case

    def handle(self, http_request: Type[HttpRequest]) -> HttpReponse:
        """Metjod to call use Case and Handle Request"""
        response = None

        if http_request.query:
            query_string_params = http_request.query.keys()

            if "user_id" in query_string_params and "user_name" in query_string_params:
                print(http_request)
                user_id = http_request.query["user_id"]
                user_name = http_request.query["user_name"]
                response = self.find_user_use_case.by_name_and_id(
                    user_id=user_id, name=user_name
                )

            elif (
                "user_id" in query_string_params
                and "user_name" not in query_string_params
            ):
                user_id = http_request.query["user_id"]
                response = self.find_user_use_case.by_id(user_id=user_id)

            elif (
                "user_id" not in query_string_params
                and "user_name" in query_string_params
            ):
                user_name = http_request.query["user_name"]
                response = self.find_user_use_case.by_name(user_name=user_name)

            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                return HttpReponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpReponse(status_code=200, body=response["Data"])

        http_error = HttpErrors.error_400()

        return HttpReponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
