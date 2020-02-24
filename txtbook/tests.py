from django.test import TestCase
from .models import TextbookPost

# Create your tests here.

class TextbookPostTests(TestCase):
    def setUp(self):
        TextbookPost.objects.create(title="Homegoing", author="Gyasi, Yaa", dept="AAS", classnum="3500", sect="GHANA", isbn="978-1-101-97106-2", condition=5, price='10.00' )

    def test_check_listing(self):
        listing = TextbookPost.objects.get(isbn="978-1-101-97106-2")
        self.assertEqual(listing.author, "Gyasi, Yaa")
