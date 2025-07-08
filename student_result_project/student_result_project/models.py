from django.db import models

class ContactForm(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return 'Message from ' + self.name + ' Message is ' + self.message

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, null=False)  # Add this line
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return 'Teacher Name: ' + self.username
    




class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100, default="password", null=False, blank=False)  # Add this line
    class_name = models.CharField(max_length=50, choices=[
        ('1 Class', '1 Class'),
        ('2 Class', '2 Class'),
        ('3 Class', '3 Class'),
        ('4 Class', '4 Class'),
        ('5 Class', '5 Class'),
        ('6 Class', '6 Class'),
        ('7 Class', '7 Class'),
        ('8 class', '8 Class'),], null=False, blank=False)
    section=models.CharField(max_length=50, choices=[
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),], null=False, blank=False)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone_number= models.CharField(max_length=20, blank=False)
    address= models.CharField(max_length=20, blank=False)
    parent_name = models.CharField(max_length=100, blank=False)
    parent_phone = models.CharField(max_length=20, blank=False)
    date_joined = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'Student Name: {self.first_name} {self.last_name}, Class: {self.class_name}, Roll No: {self.roll_number}'
    