from django.db import models
from student_result_project.models import Teacher  # adjust import if needed
from django.contrib.auth.models import User
from teacher.models import Teacher

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# class SutedentMarks(models.Model):
#     pass




class StudentMarks(models.Model):
     
     student_id = models.BigIntegerField(primary_key=True)  # For large student IDs
     student_name = models.CharField(max_length=100 , null=False)     
     student_class = models.CharField(max_length=50,choices=[
         ('1 Class', '1 Class'),
         ('2 Class', '2 Class'),
         ('3 Class', '3 Class'),
         ('4 Class', '4 Class'),
         ('5 Class', '5 Class'),
         ('6 Class', '6 Class'),
         ('7 Class', '7 Class'),
         ('8 class', '8 Class'),   
         ])     
     English= models.PositiveIntegerField(default=0, null=False)
     Nepali= models.PositiveIntegerField(default=0,null=False)
     Math= models.PositiveIntegerField(default=0,null=False)
     Science= models.PositiveIntegerField(default=0,null=False)
     Social= models.PositiveIntegerField(default=0,null=False)
     Computer= models.PositiveIntegerField(default=0,null=False)
     Biyakran= models.PositiveIntegerField(default=0, null=True, blank=True)
     Grammer= models.PositiveIntegerField(default=0, null=True, blank=True)
     Health= models.PositiveIntegerField(default=0, null=True, blank=True)
     Moral= models.PositiveIntegerField(default=0, null=True, blank=True)
     GK= models.PositiveIntegerField(default=0, null=True, blank=True)
     OPT_Math= models.PositiveIntegerField(default=0, null=True, blank=True)

     def __str__(self):
         return f"{self.student_id} - {self.student_name} - {self.student_class}"



class SetAssignment(models.Model):
    title = models.CharField(max_length=200 , null=False, blank=False)
    AssignmentType = models.CharField(max_length=50, choices=[
        ('Homework', 'Homework'),('Quiz', 'Classwork'), ('Project', 'Project')
        ,('Presentation', 'Presentation')], null=False, blank=False)
    EstimatedTime= models.CharField(max_length=50, null=False, blank=False)
    Description= models.TextField(null=False, blank=False)
    DueDate= models.DateField(null=False, blank=False)
    DueTime= models.TimeField(null=False, blank=False)
    Class= models.CharField(max_length=50, choices=[
        ('1 Class', '1 Class'),
        ('2 Class', '2 Class'),
        ('3 Class', '3 Class'),
        ('4 Class', '4 Class'),
        ('5 Class', '5 Class'),
        ('6 Class', '6 Class'),
        ('7 Class', '7 Class'),
        ('8 class', '8 Class'),], null=False, blank=False)
    Subject= models.CharField(null=False, blank=False)
    