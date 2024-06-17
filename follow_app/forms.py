from django import forms

from accounts.models import User
from .models import Child, Team_Lead, Member, Comment, TeamMember


class MemberForm(forms.ModelForm):
    # coordinator = forms.ModelChoiceField(queryset=User.objects.filter(role='2'))
    # team_member = forms.ModelChoiceField(queryset=User.objects.filter(role='3'))
    
    class Meta:
        model = Member
        fields = ['image','first_name','middle_name', 'last_name', 'date_of_birth','email', 'phone_no','gender',
                  'marital_status',
                  'team_lead', 'team_member','status','kin_fullname','kin_birth','kin_gender',
                   'kin_relationship','kin_address','kin_phone_no','kin_email','emergency_phone_no' ]
        # exclude = ['staff']
        # widgets = {
        #     'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
        #     'middle_name': forms.TextInput(attrs={'placeholder': 'Middle Name'}),
        #     'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        #     'phone_no': forms.TextInput(attrs={'placeholder': 'Phone No'}),
        #     'email': forms.TextInput(attrs={'placeholder': 'Email'}),
        #     'occupation': forms.TextInput(attrs={'placeholder': 'Occupation'}),
           
        #     'address': forms.TextInput(attrs={'placeholder': 'Address'}),
        #     'nationality': forms.TextInput(attrs={'placeholder': 'Nationality'}),

            
        #     'landmark': forms.TextInput(attrs={'placeholder': 'Landmark'}),
           
        # }
        
class CommentForm(forms.ModelForm):       
        
    class Meta:
        model = Comment
        fields = ['first_name','last_name', 'phone_no', 'comment', 'coor_comm','team_mem']



class Team_LeadForm(forms.ModelForm):       
        
    class Meta:
        model = Team_Lead
        fields = ['name']



class TeamMemberForm(forms.ModelForm):       
        
    class Meta:
        model = TeamMember
        fields = ['team_lead','name']





from django import forms
from .models import Family

class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ['family_name',   'address']



class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['name', 'age']


from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'parent_address',
            'parent_phone_number',
            'university_name',
            'program_of_study',
            'program',
            'work_type',
            'company_name',
            'position',
            'duration',
            'responsibilities',
        ]
        widgets = {
            'parent_address': forms.TextInput(attrs={'class': 'form-control bg-light'}),
            'parent_phone_number': forms.TextInput(attrs={'class': 'form-control bg-light'}),
            'university_name': forms.TextInput(attrs={'class': 'form-control bg-light'}),
            'program_of_study': forms.TextInput(attrs={'class': 'form-control bg-light'}),
            'program': forms.Select(attrs={'class': 'form-control bg-light'}),
            'work_type': forms.Select(attrs={'class': 'form-control bg-light'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control bg-light'}),
            'position': forms.TextInput(attrs={'class': 'form-control bg-light'}),
            'duration': forms.TextInput(attrs={'class': 'form-control bg-light'}),
            'responsibilities': forms.Textarea(attrs={'class': 'form-control bg-light'}),
        }





# forms.py

# forms.py

from django import forms
from .models import NYSC

class NYSCForm(forms.ModelForm):
    class Meta:
        model = NYSC
        exclude = ['member']
        widgets = {
            'parent_address': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter parent address'
            }),
            'parent_phone_number': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter parent phone number'
            }),
            'university_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter university name'
            }),
            'program_of_study': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter program of study'
            }),
            'year_of_graduation': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter year of graduation'
            }),
            'place_of_assignment': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter place of assignment'
            }),
        }





# forms.py

from django import forms
from .models import Children

class ChildrenForm(forms.ModelForm):
    class Meta:
        model = Children
        exclude = ['member']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter child name'}),
            'school': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter school name'}),
            'class_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter class name'}),
            'allergies': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter any allergies', 'rows': 3}),
            'medical_conditions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter any medical conditions', 'rows': 3}),
        }



# forms.py


# from django import forms
# from .models import Kbn

# class BusinessProfileForm(forms.ModelForm):
#     class Meta:
#         model = Kbn
#         fields = [
#             'business_name', 
#             'is_registered', 
#             'brief_description', 
#             'years_of_experience', 
#             'number_of_employees', 
#             'business_sector'
#         ]
#         widgets = {
#             'business_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter business name'}),
#             'is_registered': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#             'brief_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter brief description', 'rows': 3}),
#             'years_of_experience': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter years of experience'}),
#             'number_of_employees': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number of employees'}),
#             'business_sector': forms.Select(attrs={'class': 'form-control'}),
#         }



# class CareerProfileForm(forms.ModelForm):
#     class Meta:
#         model = Kbn
#         fields = [
#             'current_employment_job_title', 'current_employment_company_name', 'current_employment_duration', 'current_employment_responsibilities',
#             'previous_employment_job_title', 'previous_employment_company_name', 'previous_employment_duration', 'previous_employment_responsibilities',
#             'highest_qualification_degree', 'highest_qualification_institution', 'highest_qualification_year_of_graduation', 'highest_qualification_gpa',
#             'other_qualification_certification', 'other_qualification_institution', 'other_qualification_year_of_graduation', 'other_qualification_gpa',
#             'skills', 'achievements_and_awards', 'additional_information'
#         ]
#         widgets = {
#             'current_employment_job_title': forms.TextInput(attrs={'class': 'form-control'}),
#             'current_employment_company_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'current_employment_duration': forms.TextInput(attrs={'class': 'form-control'}),
#             'current_employment_responsibilities': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
#             'previous_employment_job_title': forms.TextInput(attrs={'class': 'form-control'}),
#             'previous_employment_company_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'previous_employment_duration': forms.TextInput(attrs={'class': 'form-control'}),
#             'previous_employment_responsibilities': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
#             'highest_qualification_degree': forms.TextInput(attrs={'class': 'form-control'}),
#             'highest_qualification_institution': forms.TextInput(attrs={'class': 'form-control'}),
#             'highest_qualification_year_of_graduation': forms.TextInput(attrs={'class': 'form-control'}),
#             'highest_qualification_gpa': forms.TextInput(attrs={'class': 'form-control'}),
#             'other_qualification_certification': forms.TextInput(attrs={'class': 'form-control'}),
#             'other_qualification_institution': forms.TextInput(attrs={'class': 'form-control'}),
#             'other_qualification_year_of_graduation': forms.TextInput(attrs={'class': 'form-control'}),
#             'other_qualification_gpa': forms.TextInput(attrs={'class': 'form-control'}),
#             'skills': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
#             'achievements_and_awards': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
#             'additional_information': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
#         }





# forms.py

from django import forms
from .models import Business

class BusinessProfileForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = [
            'business_name', 'is_registered', 'brief_description', 'years_of_experience',
            'number_of_employees', 'business_sector'
        ]
        widgets = {
            'business_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter business name'}),
            'is_registered': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'brief_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter brief description'}),
            'years_of_experience': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'number_of_employees': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'business_sector': forms.Select(attrs={'class': 'form-control'}),
        }




from django import forms
from django.forms import inlineformset_factory
from .models import Career, CurrentEmployment, PreviousEmployment, EducationalBackground, OtherQualification

class CareerProfileForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ['skills', 'achievements_and_awards', 'additional_information']
        widgets = {
            'skills': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'achievements_and_awards': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'additional_information': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }

class CurrentEmploymentForm(forms.ModelForm):
    class Meta:
        model = CurrentEmployment
        fields = ['job_title', 'company_name', 'duration', 'responsibilities']
        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
            'responsibilities': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }

class PreviousEmploymentForm(forms.ModelForm):
    class Meta:
        model = PreviousEmployment
        fields = ['job_title', 'company_name', 'duration', 'responsibilities']
        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
            'responsibilities': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }

class EducationalBackgroundForm(forms.ModelForm):
    class Meta:
        model = EducationalBackground
        fields = ['degree', 'institution', 'year_of_graduation', 'gpa']
        widgets = {
            'degree': forms.TextInput(attrs={'class': 'form-control'}),
            'institution': forms.TextInput(attrs={'class': 'form-control'}),
            'year_of_graduation': forms.NumberInput(attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class OtherQualificationForm(forms.ModelForm):
    class Meta:
        model = OtherQualification
        fields = ['certification', 'institution', 'year_of_graduation', 'gpa']
        widgets = {
            'certification': forms.TextInput(attrs={'class': 'form-control'}),
            'institution': forms.TextInput(attrs={'class': 'form-control'}),
            'year_of_graduation': forms.NumberInput(attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control'}),
        }

CurrentEmploymentFormSet = inlineformset_factory(Career, CurrentEmployment, form=CurrentEmploymentForm, extra=1)
PreviousEmploymentFormSet = inlineformset_factory(Career, PreviousEmployment, form=PreviousEmploymentForm, extra=1)
EducationalBackgroundFormSet = inlineformset_factory(Career, EducationalBackground, form=EducationalBackgroundForm, extra=1)
OtherQualificationFormSet = inlineformset_factory(Career, OtherQualification, form=OtherQualificationForm, extra=1)
