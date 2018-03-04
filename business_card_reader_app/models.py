from django.db import models


class BusinessCard(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.name + " " + self.surname + " " + self.company + " " + self.email
