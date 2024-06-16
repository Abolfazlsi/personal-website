from django.db import models


class Footer(models.Model):
    telegram = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)

    name = models.CharField(max_length=50)


class Message(models.Model):
    name = models.CharField(max_length=50, null=True)
    content = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    body = models.TextField(null=True)

    def __str__(self):
        return f"{self.name} - {self.body}"


class Info(models.Model):
    age = models.CharField(max_length=60, null=True)
    address = models.CharField(max_length=50, null=True)
    call = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True)
