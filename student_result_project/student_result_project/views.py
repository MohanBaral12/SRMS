from django.shortcuts import*
from student_result_project.models import *

def home(request):
    return render(request,'index/home.html',{})



def index(request):
    return render(request,'index/home.html',{})



def contact(request):
    return render(request,'index/contact.html',{})

def fetch_data(request):
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
    return render(request, 'index/contact.html', {'success': True})
