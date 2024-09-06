from django.db import models

# Create your models here.
class UserLogin(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(default='default@example.com')
    password = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.username