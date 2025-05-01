from django.db import models

# Create your models here.

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    class Meta:
        unique_together = ('reservation_date', 'reservation_slot')

    def __str__(self):
        return f'{self.first_name} - {self.reservation_date} - {self.reservation_slot}'
