from django.contrib import admin
from .models import Resume,JobDescription,RegisterUser
# Register your models here.
admin.site.register(Resume)
admin.site.register(JobDescription)
admin.site.register(RegisterUser)