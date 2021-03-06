from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{} - {}".format(
            self.id, 
            self.name
        )
    