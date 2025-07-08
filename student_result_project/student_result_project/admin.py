from django.contrib import admin
from .models import ContactForm
from .models import *
# Register your models here.
admin.site.register(ContactForm)
admin.site.register(Teacher)
admin.site.register(Student)

