from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile

from .models import StudentProfile, User, EmployerProfile
from helpers.profile_img_validation import validate_profile_img

'''
Student profile model as a form
Can be viewed and mutated on students profile page 
'''


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        exclude = ['user']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'})
        }
        labels = {
            'phone': 'Phone Number',
            'dob': 'Date of Birth',
            'hs': 'High School Name',
            'hs_addy': 'High School Address',
            'teacher_or_counselor_email': 'Teacher or Counselor Email',
            'teacher_or_counselor_name': 'Teacher or Counselor Name',
            'awards_achievements': 'Awards and Achievements',
            'work_exp': 'Word Experience',
            'volunteering_exp': 'Volunteering Experience',
            'extracurriculars': 'Extracurricular Activities',
            'skills': 'Skills',
            'leadership_roles': 'Leadership Roles',
            'link1': 'Link 1',
            'link2': 'Link 2',
            'link3': 'Link 3',
            'link4': 'Link 4'
        }


'''
Employer profile model as a form
Can be viewed and mutated on employers profile page
'''


class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        exclude = ['user']


'''
General user model as a form
Displays viewable and editable data applicable to employers and students
Can be viewed and edited on current users profile page 
'''


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'profile_picture': forms.FileInput
        }
        fields = ['email', 'profile_picture', 'first_name', 'last_name']

    def clean_profile_picture(self):
        '''
        Checks if the total size of the uploaded profile picture is < 2,073,600px (1920x1080)
        Only validates if a new picture has been uploaded
        '''
        pic = self.cleaned_data['profile_picture']
        # check if new image was uploaded
        if type(pic) is InMemoryUploadedFile:
            return validate_profile_img(pic)
        return pic
