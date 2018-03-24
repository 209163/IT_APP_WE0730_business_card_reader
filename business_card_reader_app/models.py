from django.core.validators import RegexValidator
from django.db import models


class BusinessCard(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    img_path = models.FilePathField(max_length=50, blank=True, null=True)

    def add_card(self):
        self.save()

    def __str__(self):
        return self.name + " " + self.surname + " " + self.company + " " + self.email + " " + self.phone_number


class ImageFile(models.Model):
    img_path_regex = RegexValidator(regex=r'.*\.jpg$',
                                    message="Possible extensions: .jpg")
    file = models.ImageField(validators=[img_path_regex], upload_to='business_cards/', default='business_cards/')
