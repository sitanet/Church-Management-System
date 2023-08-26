from django import forms
from .models import User, UserProfile
from .validators import allow_only_images_validator


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter First Name', 'required': 'required'}))
    # middle_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Middle Name', 'required': 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name', 'required': 'required'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Username ', 'required': 'required'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Email', 'required': 'required'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Phone Number', 'required': 'required'}))
    gender = forms.CharField(widget=forms.TextInput(attrs={}))
    staff_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Staff ID', 'required': 'required'}))
    # role = forms.CharField(widget=forms.TextInput(attrs={}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'role', 'gender', 'staff_id', 'password']

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )
        


# class UserProfileForm(forms.ModelForm):
#     address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Start typing...', 'required': 'required'}))
#     profile_picture = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}), validators=[allow_only_images_validator])
#     cover_photo = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}), validators=[allow_only_images_validator])
    
    
#     class Meta:
#         model = UserProfile
#         fields = ['profile_picture', 'cover_photo', 'address', 'country', 'state', 'city', 'pin_code', 'latitude', 'longitude']

#     def __init__(self, *args, **kwargs):
#         super(UserProfileForm, self).__init__(*args, **kwargs)
#         for field in self.fields:
#             if field == 'latitude' or field == 'longitude':
#                 self.fields[field].widget.attrs['readonly'] = 'readonly'