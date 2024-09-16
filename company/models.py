from django.db import models

# Create your models here.

class Branches(models.Model):
    name = models.CharField(max_length=50,unique=True)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    def __str__(self):
            return self.name

class Departments(models.Model):
    name = models.CharField(max_length=50)
    dept_branch = models.ForeignKey(Branches,related_name="Dept_Branch",on_delete=models.CASCADE)
    description = models.CharField(max_length=150,help_text="no more than 150 chars")
    class Meta:
        unique_together = ('name', 'dept_branch')
    def __str__(self):
        return self.name
    
    

