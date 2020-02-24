from django.test import TestCase
from .models import TextbookPost

# Create your tests here.

# E3_test1
# Tests the textbookpost model, and our database
# Creates a listing for a textbook (first in the database)
# and checks to see if it is in the database.
class TextbookPostTests(TestCase):
    def setUp(self):
        TextbookPost.objects.create(title="Homegoing", author="Gyasi, Yaa", dept="AAS", classnum="3500", sect="GHANA", isbn="978-1-101-97106-2", condition=5, price='10.00' )

    def test_check_listing(self):
        listing = TextbookPost.objects.get(isbn="978-1-101-97106-2")
        self.assertEqual(listing.author, "Gyasi, Yaa")
