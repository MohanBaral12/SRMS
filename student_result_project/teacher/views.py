from django.shortcuts import render, redirect
from django.http import HttpResponse
from student_result_project.models import Teacher
from teacher.models import Subject
from django.forms import modelformset_factory
from .forms import StudentMarksForm
from teacher.models import StudentMarks
from student_result_project.models import *
# Create your views here.

from django.shortcuts import render, redirect
from .models import *

def teacher_home(request):
    teacher_username = request.session.get('teacher_username')
    
    if not teacher_username:
        return redirect('login')
    
    try:
        teacher = Teacher.objects.get(username=teacher_username)
        return render(request, 'teacher/home.html', {'TName': teacher.username})
    except Teacher.DoesNotExist:
        return redirect('login')





# Login view for teacher
def login(request):
    return render(request, 'teacher/login.html',{})




# Check login teacher
def check_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Your authentication logic here
        try:
            teacher = Teacher.objects.get(username=username, password=password)
            # Store username in session
            request.session['teacher_username'] = teacher.username
            return redirect('teacher_home')  # or wherever you want to redirect
        except Teacher.DoesNotExist:
            return render(request, 'teacher/login.html', {'error': True})
    return render(request, 'teacher/login.html')



    

# Add marks view for teacher
def add_marks_form(request):
    return render(request, 'teacher/add_marks.html', {})


# Set marks for a student
def set_marks(request):
  
     if request.method == 'POST':
         student_id = request.POST.get('student_id')
         student_name = request.POST.get('student_name')
         student_class = request.POST.get('student_class')
         SubEnglish = request.POST.get('english')
         SubNepali = request.POST.get('nepali')
         SubMath = request.POST.get('math')
         SubScience= request.POST.get('science')
         SubComputer = request.POST.get('computer')
         SubSocial = request.POST.get('social')


         # Optional fields (skip if empty)
         SubBiyakrun = request.POST.get('grammar')
         SubBiyakrun = int(SubBiyakrun) if SubBiyakrun else None

         SubHealth = request.POST.get('health')
         SubHealth = int(SubHealth) if SubHealth else None

         SubGrammar = request.POST.get('Grammer')
         SubGrammar = int(SubGrammar) if SubGrammar else None

         SubMoral = request.POST.get('moral')
         SubMoral = int(SubMoral) if SubMoral else None

         SubGK = request.POST.get('gk')
         SubGK = int(SubGK) if SubGK else None

         SubOPTMath = request.POST.get('opt_math')
         SubOPTMath = int(SubOPTMath) if SubOPTMath else None

         # Check if student_id already exists
         if StudentMarks.objects.filter(student_id=student_id).exists():
            return render(request, 'teacher/add_marks.html', {
                "id_error": f"Student ID  or Roll Number {student_id} is already exists."
            })
         
         # Check if the student already has marks
         print(f"Checking marks \nstudent ID: {student_id} \nstudent name:  {student_name} \nstudent class: {student_class} \n SubEnglish:  {SubEnglish} \nSubNepali: {SubNepali} \nSubMath: {SubMath}  \nSubScience: {SubScience} \nSubComputer: {SubComputer} \nSubSocial:  {SubSocial} \nSubGrammar: {SubGrammar} \nSubBiyakrun: {SubBiyakrun}  \nSubHealth: {SubHealth} \nSubMoral: {SubMoral} \nSubOPTMath:  {SubOPTMath} \nSubGK: {SubGK}")
     
         student_marks = StudentMarks(
             student_id=student_id, student_class=student_class, student_name=student_name, English=SubEnglish, Nepali=SubNepali, Math=SubMath, Science=SubScience, Computer=SubComputer, Social=SubSocial, Grammer=SubGrammar, Biyakran=SubBiyakrun, Health=SubHealth, Moral=SubMoral, OPT_Math=SubOPTMath, GK=SubGK
             )
         student_marks.save()
         print("Marks updated successfully")
         return render(request, 'teacher/add_marks.html', {"success": True})
     
     return render(request, 'teacher/add_marks.html', {"success": False})
    
 

   


def show_subject_name(request):
    subjects = Subject.objects.all()
    # subject_name=subjects.join([subject.name for subject in subjects])

    return HttpResponse(f'<br> Subject Name is '.join([subject.name for subject in subjects])) 



def add_assignment(request):
    return render(request, 'teacher/add_assignment.html', {})



def set_assignment(request):
    if request.method == '':
        return render(request, 'teacher/add_assignment.html', {"error": True})
    if request.method == 'POST':
        assignment_title = request.POST.get('title')
        assignment_type = request.POST.get('type')
        estimated_time = request.POST.get('estimated_time')
        assignment_description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        due_time = request.POST.get('due_time')
        student_class = request.POST.get('student_class')
        subject = request.POST.get('subject')

        print(f"Assignment Title: {assignment_title}\nType: {assignment_type}\nEstimated Time: {estimated_time}\nDescription: {assignment_description}\nDue Date: {due_date}\nDue Time: {due_time}\nClass: {student_class}\nSubject: {subject}")

        #Save the assignment to the database
        assignment = SetAssignment(
            title=assignment_title,
            AssignmentType=assignment_type,
            EstimatedTime=estimated_time,
            Description=assignment_description,
            DueDate=due_date,
            DueTime=due_time,
            Class=student_class,
            Subject=subject
        )
        assignment.save()

        return render(request, 'teacher/add_assignment.html', {"success": True})

    return render(request, 'teacher/add_assignment.html', {"success": False})




def contact_form(request):
    return render(request,'teacher/contact.html',{})




def student(request):
    return render(request, 'teacher/Add_student.html', {})


def set_student(request):
    if request.method == 'POST':
        student_id = request.POST.get('id')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        student_class = request.POST.get('class')
        section = request.POST.get('section')
        student_roll_number = request.POST.get('roll_number')
        student_email = request.POST.get('email')
        student_phone = request.POST.get('phone')
        address = request.POST.get('address')
        parent_name = request.POST.get('parent_name')
        parent_phone = request.POST.get('parent_phone')

        # Print the received data for debugging
        print(f"Student IDs: {student_id}\nFirst Name: {fname}\nLast Name: {lname}\nUsername: {username}\nPassword: {password}\nClass: {student_class}\nSection: {section}\nRoll Number: {student_roll_number}\nEmail: {student_email}\nPhone: {student_phone}\nAddress: {address}\nParent Name: {parent_name}\nParent Phone: {parent_phone}")

        # Save the student data to the database
        new_student = Student(
            student_id=student_id,
            first_name=fname,
            last_name=lname,
            username=username,
            password=password,
            class_name=student_class,
            section=section,
            roll_number=student_roll_number,
            address=address,
            email=student_email,
            parent_name=parent_name,
            phone_number=student_phone,
            parent_phone=parent_phone
        )
        new_student.save()

        return render(request, 'teacher/Add_student.html', {"success": True})

    return render(request, 'teacher/Add_student.html', {"success": False})



def contact_data(request):
    if request.method == 'POST':
        # Fetch form data from the request
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Here you can handle the form data, e.g., save it to the database or send an email
        print(f"Name: {name}, Email: {email}, Message: {message}")
       
    
        # save the contact form data to the database if needed
        c= ContactForm(name=name, email=email, message=message)                   
        c.save()
     # Redirect or render a success page after processing
    return render(request, 'teacher/contact.html', {'success': True})
