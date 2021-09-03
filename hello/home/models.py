from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    TASTER = "ta"
    DEVELOPER = "de"
    MANAGER = "ma"

    working_role_choice = [
        (TASTER,'Taster'),
        (DEVELOPER,'Developer'),
        (MANAGER,'Manager'),
    ]
    working_role = models.CharField(
        max_length=2,
        choices=working_role_choice,
    )
    analyst = models.CharField(max_length=122) 
    team = models.CharField(max_length=122) 
    manager = models.CharField(max_length=122) 
    backup_person = models.CharField(max_length=122)
    FULL_TIME = "fu"
    PART_TIME = "pa"
    HOURLY_BASIS = "ho"
    time_choice = [
        (FULL_TIME,'Full Time'),
        (PART_TIME, 'Part Time'),
        (HOURLY_BASIS,'Hourly Basis'),
    ]
    job_nature = models.CharField(
        max_length=2,
        choices=time_choice,
    )
    phone = models.CharField(max_length=122)

    def __str__(self):
        return self.name
    




# Create your models here.
