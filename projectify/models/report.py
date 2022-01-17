from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from projectify.models.project import Project

class Report(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    percentage = models.DecimalField(
        decimal_places = 2, 
        max_digits = 4,
        validators = [
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    creation_date = models.DateField(auto_now_add=True)
    modification_date = models.DateField(auto_now=True)

    def __str__(self):
        return "{} - {} - {} - {}".format(
            self.id,
            self.project.id,
            self.user.username,
            self.percentage
        )
    