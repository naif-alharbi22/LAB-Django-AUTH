from django.db import models
from Doctor.models import Doctor
# Create your models here.



class Clinic(models.Model):
    class WorkHours(models.TextChoices):
        MORNING_TIME  = "morning", "07:00 AM - 03:00 PM"
        EVENING_PERIOD = "EVENING", "03:00 PM - 11:00 AM"
        NIGHT_PERIOD = "NIGHT" , "11:00 PM - 07:00 AM"
    name = models.CharField(max_length=100)
    description = models.TextField()
    work_hours = models.CharField(max_length=100 , choices=WorkHours.choices)
    feature_image = models.ImageField(upload_to='images/clinic/' , default='images/clinic/default.jpg')
    doctor = models.ManyToManyField(Doctor)
    
    
    
    
    
    
    
    
