from django.test import TestCase
from django.contrib.auth.models import User
from .models import Booking, MenuItem

class BookingTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser','test@test.com','password123')
        Booking.objects.create(user=self.user,reservation_date='2025-11-10',reservation_slot='09:00-10:00')

    def test_booking_exists(self):
        booking = Booking.objects.get(user=self.user,reservation_slot='09:00-10:00')
        self.assertEqual(booking.reservation_slot,'09:00-10:00')

class MenuTestCase(TestCase):
    def setUp(self):
        MenuItem.objects.create(name='Pizza',price=9.99)

    def test_menu_item(self):
        item = MenuItem.objects.get(name='Pizza')
        self.assertEqual(item.price,9.99)
