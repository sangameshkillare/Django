from django.db import models

# Create your models here.


class student(models.model):
    name=models.CharField(max_length=500)
    age =models.IntegerField()
    email=models.EmailFeild()
    
    
def __str__(self):
    return self.name

    

# after creating models we need to make a migration
#command one - python manage.py make migrations 
#2nd command - python manage.py migrate


# a migration in ajango is a file  that  stores changes made by us to our models  like a adding feilds , delete table etc .
