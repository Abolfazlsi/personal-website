from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=30)
    address = models.CharField(max_length=130)
    image = models.ImageField(upload_to="resume")

    def __str__(self):
        return self.title

