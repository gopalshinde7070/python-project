from django.db import models

# Create your models here.
class Resume(models.Model):
    resume=models.FileField(upload_to='resume')
class JobDescription(models.Model):
    job_title=models.CharField(max_length=100)
    job_description=models.TextField()

    def __str__(self):
        return self.job_title # TODO
    
from django.db import models

class RegisterUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=18)  # hashed later
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.RegisterUser
        
