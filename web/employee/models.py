from django.db import models

class Employee(models.Model):
    """"Employee model"""

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    STATUS_CHOICES = (
        (0, 'Inactive'),
        (1, 'Active'),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.CharField(max_length=120)
    status = models.SmallIntegerField(choices=STATUS_CHOICES)

    def fullname(self):
        return ' '.join([self.first_name, self.last_name]).strip()

    def __str__(self):
        return self.fullname()
    