from django import forms

from accounts.models import User
from .models import Team_Lead, Member, Comment, TeamMember


class MemberForm(forms.ModelForm):
    # coordinator = forms.ModelChoiceField(queryset=User.objects.filter(role='2'))
    # team_member = forms.ModelChoiceField(queryset=User.objects.filter(role='3'))
    
    class Meta:
        model = Member
        fields = ['image','first_name','middle_name', 'last_name', 'date_of_birth','email', 'phone_no','gender',
                  'marital_status','occupation','address','nationality','kcc_center','wedding_ann',
                  'join','about','dept','purpose', 'team_lead', 'team_member','status']
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
        fields = ['first_name','last_name',  'comment', 'coor_comm','team_mem']



class Team_LeadForm(forms.ModelForm):       
        
    class Meta:
        model = Team_Lead
        fields = ['name']



class TeamMemberForm(forms.ModelForm):       
        
    class Meta:
        model = TeamMember
        fields = ['team_lead','name']



