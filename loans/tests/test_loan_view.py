from rest_framework.test import APITestCase
from rest_framework.views import status
from copys.models import Copy
from users.models import User
from books.models import Book
from rest_framework_simplejwt.tokens import RefreshToken

import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

class AccountViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        book_data = {
            "title": "Moby Dick2",
            "category": "aventura",
            "realese_date": "2000-01-01",
            "synopsis": "Passado no mar, o livro conta a história de um navio baleeiro que persegue e ataca várias vezes um cachalote sem conseguir matá-lo.",
            "author": "Herman Melville",
            "quantity": 10,
        }

        book = Book.objects.create(**book_data)
        cls.copy = Copy.objects.create(book=book)

        cls.base_url = f"/api/loans/user/{cls.copy.id}/"

    def setUp(self) -> None:
        user_data = {
            "username": "user",
            "email": "user@gmail.com",
            "password": "1234",
            "is_employe": False,
        }
        superuser_data = {
            "username": "superuser",
            "email": "superuser@gmail.com",
            "password": "1234",
            "is_employe": True,
        }

        self.user = User.objects.create_user(**user_data)
        self.superuser = User.objects.create_superuser(**superuser_data)

        self.user_token = RefreshToken.for_user(self.user).access_token
        self.superuser_token = RefreshToken.for_user(self.superuser).access_token

    def test_can_create_loan(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(self.user_token))
        res = self.client.post(self.base_url, data={}, format="json")
        result = res.json()

        expected_status_code = status.HTTP_201_CREATED
        returned_status_code = res.status_code

        msg = f"Verifique se o status code da rota `{self.base_url}` é {expected_status_code}."
        self.assertEqual(expected_status_code, returned_status_code, msg)

        expected_data = {
            "borrowed_date": None,
            "devolution_date": None,
            "is_devoluted": False,
            "blocked_until": None,
            "copy": self.copy.id,
            "user_id": self.superuser.id,
        }

        result.pop("id")
        result["copy"] = self.copy.id
        result["user_id"] = self.superuser.id

        self.assertEqual(expected_data, result)

    def test_can_list_all_loans(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer " + str(self.superuser_token)
        )
        res = self.client.get("/api/loans/")

        expected_status_code = status.HTTP_200_OK
        returned_status_code = res.status_code

        msg = f"Verifique se o status code da rota `/api/loans/` é {expected_status_code}."
        self.assertEqual(expected_status_code, returned_status_code, msg)

    def test_can_list_all_loans_without_permission(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(self.user_token))
        res = self.client.get("/api/loans/")

        expected_status_code = status.HTTP_403_FORBIDDEN
        returned_status_code = res.status_code

        msg = f"Verifique se o status code da rota `/api/loans/` é {expected_status_code}."
        self.assertEqual(expected_status_code, returned_status_code, msg)

    def test_can_update_loans_without_permission(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(self.user_token))
        res = self.client.post(self.base_url, data={}, format="json")
        result = res.json().pop("id")

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(self.user_token))
        res = self.client.patch(f"/api/loans/{result}/")

        expected_status_code = status.HTTP_403_FORBIDDEN
        returned_status_code = res.status_code

        msg = f"Verifique se o status code da rota `/api/loans/{result}/` é {expected_status_code}."
        self.assertEqual(expected_status_code, returned_status_code, msg)

    def test_can_update_loans(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(self.user_token))
        res = self.client.post(self.base_url, data={}, format="json")
        result = res.json().pop("id")

        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer " + str(self.superuser_token)
        )
        res = self.client.patch(f"/api/loans/{result}/")
        result = res.json()

        expected_status_code = status.HTTP_200_OK
        returned_status_code = res.status_code

        msg = f"Verifique se o status code da rota `/api/loans/{result}/` é {expected_status_code}."
        self.assertEqual(expected_status_code, returned_status_code, msg)

    def test_can_devolution_copy(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(self.user_token))
        res = self.client.post(self.base_url, data={}, format="json")
        result = res.json().pop("id")

        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer " + str(self.superuser_token)
        )
        res = self.client.patch(f"/api/loans/{result}/")

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(self.user_token))
        res = self.client.patch(f"/api/loans/user/{result}/")

        expected_status_code = status.HTTP_200_OK
        returned_status_code = res.status_code

        msg = f"Verifique se o status code da rota `/api/loans/user/{result}/` é {expected_status_code}."
        self.assertEqual(expected_status_code, returned_status_code, msg)

    def test_can_devolution_copy_without_owner(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(self.user_token))
        res = self.client.post(self.base_url, data={}, format="json")
        result = res.json().pop("id")

        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer " + str(self.superuser_token)
        )
        res = self.client.patch(f"/api/loans/{result}/")

        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer " + str(self.superuser_token)
        )
        res = self.client.patch(f"/api/loans/user/{result}/")

        expected_status_code = status.HTTP_403_FORBIDDEN
        returned_status_code = res.status_code

        msg = f"Verifique se o status code da rota `/api/loans/user/{result}/` é {expected_status_code}."
        self.assertEqual(expected_status_code, returned_status_code, msg)
