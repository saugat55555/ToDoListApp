from django.db import models

# Create your models here.
class Lists(models.Model):
    task = models.CharField(max_length=20)
    done = models.BooleanField(default = False)

    def __str__(self):
        return self.task