from django.test import TestCase
from loans.models import Loan
from copys.models import Copy
from users.models import User
from books.models import Book

class LoanModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # cls -> class
        book_data={
            "title": "Moby Dick2",
	        "category":"aventura",
	        "realese_date": "2000-01-01",
	        "synopsis": "Passado no mar, o livro conta a história de um navio baleeiro que persegue e ataca várias vezes um cachalote sem conseguir matá-lo.",
	        "author": "Herman Melville",
	        "quantity": 10
        }

        book = Book.objects.create(**book_data)
        user = User.objects.create()
        copy = Copy.objects.create(book=book)

        cls.loan = Loan.objects.create(user=user, copy=copy)

        cls.loan_data = {
            "borrowed_date": None,
	        "devolution_date": None,
	        "is_devoluted": False,
	        "blocked_until": None,
	        "copy": copy,
            "user": user
        }
		   
	
    def test_loans_fields(self):
        self.assertEqual(
            self.loan.borrowed_date,
            self.loan_data["borrowed_date"],
        )

        self.assertEqual(
            self.loan.devolution_date,
            self.loan_data["devolution_date"],
            
        )

        self.assertEqual(
            self.loan.is_devoluted,
            self.loan_data["is_devoluted"],
        )

        self.assertEqual(
            self.loan.blocked_until,
            self.loan_data["blocked_until"],
        )

        self.assertEqual(
            self.loan.copy,
            self.loan_data["copy"],
        )

        self.assertEqual(
            self.loan.user,
            self.loan_data["user"],
        )
