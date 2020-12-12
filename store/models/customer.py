from django.db import models
from django.core.validators import MinLengthValidator

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=12,validators=[MinLengthValidator(6)])

    @staticmethod
    def get_cusomer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except :
            return False

    def register(self):
        self.save()

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False