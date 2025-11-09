from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Booking(models.Model):
    SLOT_CHOICES = [
        ('09:00-10:00','09:00-10:00'),
        ('10:00-11:00','10:00-11:00'),
        ('11:00-12:00','11:00-12:00'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_date = models.DateField()
    reservation_slot = models.CharField(max_length=20, choices=SLOT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('reservation_date','reservation_slot')
        ordering = ['reservation_date','reservation_slot']

    def __str__(self):
        return f'{self.user.username} - {self.reservation_date} {self.reservation_slot}'
