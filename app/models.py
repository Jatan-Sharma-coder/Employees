from django.db import models

class employees(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    emp_id=models.IntegerField()
    emp_ph=models.IntegerField()
    emp_emailid=models.CharField(max_length=20)

    def __str__(self):
        return self.firstname