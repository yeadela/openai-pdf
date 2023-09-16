from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30,null=True,blank=True)
    last_name = models.CharField(max_length=30,unique=True,default='Lucy')
   # email = models.EmailField()
    id =models.BigAutoField(primary_key=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

