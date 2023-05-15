from rest_framework.exceptions import APIException

class alreadyBorrowed(APIException):
    status_code = 400
    default_detail = "copy is already borrowed."
    default_code = "service_unavailable"

class blockedUser(APIException):
    status_code = 400
    default_detail = "user cannot borrow."
    default_code = "service_unavailable"

class alreadyDevoluted(APIException):
    status_code = 400
    default_detail = "copy is already devoluted."
    default_code = "service_unavailable"




