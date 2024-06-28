from datetime import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


current_year = datetime.today().year

class Location(models.Model):
    town = models.CharField(max_length=50)
    state = models.CharField(max_length=25)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.town}, {self.state}, {self.country}"


class Date(models.Model):
    month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    year = models.IntegerField(validators=[MinValueValidator(1990), MaxValueValidator(current_year)])
    
    def __str__(self):
        return f"{self.month}_{self.year}"

class Education(models.Model):
    school_name = models.CharField(max_length=200)
    school_short_name = models.CharField(max_length=25)
    degree_name = models.CharField(max_length=250)
    gpa = models.FloatField(null=True, blank=True)
    final_work = models.CharField(max_length=250)
    link_to_final_work = models.URLField(max_length=300, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    start_date = models.ForeignKey(Date, related_name="education_start_date", on_delete=models.CASCADE)
    end_date = models.ForeignKey(Date, related_name="education_end_date", on_delete=models.CASCADE, 
                                 null=True, blank=True)
    
    def __str__(self):
        return f"{self.school_short_name}_{self.degree_name.split()[0]}"


class Image(models.Model):
    image_type = models.CharField(max_length=100)
    image_name = models.CharField(max_length=50, null=True, blank=True)
    image_desc = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to="images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_type