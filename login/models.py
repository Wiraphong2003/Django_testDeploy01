from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    urlpath = models.CharField(max_length=1000)
    fontpath = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.username}\t{self.password}"