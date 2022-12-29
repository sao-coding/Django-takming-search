from django.db import models

# Create your models here.

class Member_info(models.Model):
    maker = (
        ('台灣', '台灣'),
        ('日本', '日本'),
        ('香港', '香港'),
        ('越南', '越南'),
        )
    country = models.CharField(max_length=4, choices=maker, default='台灣')
    room = models.PositiveIntegerField()
    bed = models.SlugField(max_length=10)
    member_class = models.CharField(max_length=5)
    student_ID = models.CharField(max_length=10)
    name = models.CharField(max_length=5)
    ID_number = models.CharField(max_length=10)
    birthday = models.DateField()
    phone = models.CharField(max_length=10)
    home_phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    emergency_contact = models.CharField(max_length=10)
    emergency_contact_phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name