from django.test import TestCase
from django.test import Client

from .models import Listing


class ListingBasic(TestCase):

    def test_response(self):
        self.client = Client()
        response = self.client.get('http://127.0.0.1:8000/listings/')
        self.assertEqual(response.status_code, 200)

    def listings_test(self):
        listing = Listing()
        listing.title = 'title'
        listing.price = '30000000'
        listing.sqft = "50000"
        listing.save()

        record = Listing.objects.get(pk=1)
        self.assertEqual(record, listing)
