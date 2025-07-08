#!/usr/bin/env python
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_result_project.settings')
django.setup()

from student_result_project.models import Student

# Create a test student
try:
    # Check if test student already exists
    test_student = Student.objects.filter(username='teststudent').first()
    
    if test_student:
        print(f"Test student already exists: {test_student.username}")
        print(f"Password: testpass123")
        print(f"Class: {test_student.class_name}")
    else:
        # Create new test student
        student = Student.objects.create(
            first_name='Test',
            last_name='Student',
            username='teststudent',
            password='testpass123',
            class_name='3 Class',
            section='A',
            roll_number='TEST001',
            email='teststudent@example.com',
            phone_number='1234567890',
            address='Test Address',
            parent_name='Test Parent',
            parent_phone='0987654321'
        )
        print(f"Test student created successfully!")
        print(f"Username: {student.username}")
        print(f"Password: {student.password}")
        print(f"Class: {student.class_name}")
        
except Exception as e:
    print(f"Error creating test student: {e}") 