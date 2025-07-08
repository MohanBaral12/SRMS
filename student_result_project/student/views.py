from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from student_result_project.models import Student
from django.contrib.auth.hashers import check_password


# Create your views here.
def stu_home(request):
    return render(request, 'student/home.html')

def stu_home(request):
    return render(request, 'student/home.html')

def stu_profile(request):
    return render(request, 'student/profile.html')

def login(request):
    return render(request, 'student/login.html')

def check_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        stu_class = request.POST.get('class')
        
    
        # Your authentication logic here
        try:
            # Check if student exists with the provided credentials
            student = Student.objects.get(
                username=username, 
                password=password, 
                class_name=stu_class
            )
            
            # If we reach here, authentication is successful
            # Store username in session
            request.session['student_username'] = student.username
            request.session['student_password'] = student.password
            request.session['student_class'] = student.class_name
            
            # Redirect to student home page
            return redirect('stu_home')
            
        except Student.DoesNotExist:
            # Authentication failed
            print("Authentication failed for username:", username, "class:", stu_class)
            # Show error message on login page
            return render(request, 'student/login.html', {
                'error': 'Invalid username, password, or class. Please try again.',
                'username': username,
                'class': stu_class
            })
        except Exception as e:
            # Handle any other unexpected errors
            print("An error occurred during login:", e)
            return render(request, 'student/login.html', {
                'error': 'An error occurred. Please try again.',
                'username': username,
                'class': stu_class
            })
    
    # If not POST request, show login form
    return render(request, 'student/login.html')





def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        stu_class = request.POST.get('class')

        try:
            # Try to fetch the student with the given username and class
            student = Student.objects.get(username=username, password=password, class_name=stu_class)

            print("Student found:", student)
            # Check if the password is correct (securely)
            if check_password(password, student.password):
                # Save session data
                request.session['student_username'] = student.username
                request.session['student_id'] = student.student_id
                request.session['student_class'] = student.class_name

                return redirect('stu_home')  # Redirect to student home page
            else:
                # Password didn't match
                messages.error(request,)
                print("Password mismatch for username:", username, "class:", stu_class)

        except Student.DoesNotExist:
            print("No matching student found for username:", username, "class:", stu_class)
            messages.error(request, {'error': True})

        except Exception as e:
            print("Something went wrong. Please try again later.")
            messages.error(request,)
            # Optional: log the actual error to console or log file
            print("Login error:", e)

        # On error, show login page with previously entered data
        return render(request, 'student/login.html', {
            'username': username,
            'class': stu_class
        })

    # If GET request, just show login form
    return render(request, 'student/login.html')
