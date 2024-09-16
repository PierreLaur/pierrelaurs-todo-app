from django.db import models

# Create your models here.


class Task(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + " - " + self.name + " - " + str(self.completed)
