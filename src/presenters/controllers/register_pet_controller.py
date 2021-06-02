from typing import Type
from src.presenters.helpers.http_models import HttpRequest, HttpReponse
from src.domain.use_cases import RegisterPet
from src.presenters.errors import HttpErrors


class RegisterPetController:
    """Controller to handle Http requests to register a new PET"""

    def __init__(self, register_pet_use_case: Type[RegisterPet]):
        self.register_pet_use_case = register_pet_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpReponse:
        """Method to call use case"""

        response = None
        if http_request.body:
            body_params = http_request.body.keys()
            if (
                "name" in body_params
                and "specie" in body_params
                and "user_info" in body_params
            ):
                user_info_params = http_request.body["user_info"].keys()

                if "user_id" in user_info_params or "user_name" in user_info_params:
                    name = http_request.body["name"]
                    specie = http_request.body["specie"]
                    user_info = http_request.body["user_info"]

                    if "age" in body_params:
                        age = http_request.body["age"]
                    else:
                        age = None
                    response = self.register_pet_use_case.register(
                        name=name, specie=specie, user_info=user_info, age=age
                    )
                else:
                    response = {"Success": False, "Data": None}
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
