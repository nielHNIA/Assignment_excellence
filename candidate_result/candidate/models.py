from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/candidates"





class Test(models.Model):
    name = models.ForeignKey(Candidate, on_delete=models.CASCADE, unique=True)
    first_round = models.IntegerField(validators= [MinValueValidator(0), MaxValueValidator(10)], default=0)
    second_round = models.IntegerField(validators= [MinValueValidator(0), MaxValueValidator(10)], default=0)
    third_round = models.IntegerField(validators= [MinValueValidator(0), MaxValueValidator(10)], default=0)


    def avg_scorer(self):
        avg = (self.first_round + self.second_round + self.third_round)/3
        return round(avg, 2)

    def get_total(self):
        total = self.first_round + self.second_round + self.third_round





    def get_absolute_url(self):
        return "/tests"
