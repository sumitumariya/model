from django.db import models

# Create your models here.
class Student(models.Model):
    
            Name=models.CharField(max_length=50)  
            Email=models.EmailField()
            Contact=models.IntegerField()
            City=models.CharField(max_length=50)
            address=models.CharField(max_length=50 ,null=True)
            class Meta:
                # ordering=["Name"]
                ordering=["-Name"]
                verbose_name_plural ='Student'
                # verbose_name = "stu"
                db_table ="stud"