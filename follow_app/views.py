import os
from sre_constants import BRANCH
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth

from accounts.views import check_role_admin
from .models import Coordinator, TeamMember
# from accounts.context_processors import get_staff
from .forms import MemberForm, CommentForm
from .models import Member, Comment
from django.shortcuts import render, get_object_or_404
# from .utils import custom_id
from accounts.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.
@login_required(login_url='login')
@user_passes_test(check_role_admin)
def dashboard(request):
    return render(request, 'admin_staff/dashboard.html')

@user_passes_test(check_role_admin)
@login_required(login_url='login')
def register_member(request):
    return render(request, 'admin_staff/register_member.html')



@login_required(login_url='login')
@user_passes_test(check_role_admin)
def register_member(request):
    
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        
        
       
        if form.is_valid():
            
            # type_of_account = form.cleaned_data['type_of_account']
            image = form.cleaned_data['image']
            first_name = form.cleaned_data['first_name']
            middle_name = form.cleaned_data['middle_name']
            last_name = form.cleaned_data['last_name']
            date_of_birth = form.cleaned_data['date_of_birth']
            email = form.cleaned_data['email']
            phone_no = form.cleaned_data['phone_no']
            gender = form.cleaned_data['gender']
            marital_status = form.cleaned_data['marital_status']
            occupation = form.cleaned_data['occupation']
       
            address = form.cleaned_data['address']
            nationality = form.cleaned_data['nationality']
         
            kcc_center = form.cleaned_data['kcc_center']
            wedding_ann = form.cleaned_data['wedding_ann']
            join = form.cleaned_data['join']
            reg_date = form.cleaned_data['reg_date']
            about = form.cleaned_data['about']
            dept = form.cleaned_data['dept']
            purpose = form.cleaned_data['purpose']
            coordinator = form.cleaned_data['coordinator']
            team_member = form.cleaned_data['team_member']
            
            # customer = Customer(first_name=first_name,middle_name=middle_name,last_name=last_name,date_of_birth=date_of_birth,email=email,phone_no=phone_no,gender=gender,marital_status=marital_status,occupation=occupation,district=district,acct_off=acct_off,id_type=id_type,id_no=id_no,issued_authority=issued_authority,issued_state=issued_state,expiry_date=expiry_date,address=address,nationality=nationality,state=state,local_govt=local_govt,city=city,landmark=landmark,next_of_kin=next_of_kin,next_address=next_address,next_phone_no=next_phone_no,type_of_account=type_of_account, customer= True)
            # member = form.save(commit=False)
            
            # member.staff = staff.objects.get(user=request.user)
            # user = staff.objects.get(user=request.user)
          
            form.save()
            messages.success(request, 'Account has been registered successfully!.')
            return redirect('display_all_member')
        
    
        
        else:
            messages.warning(request, form.errors)
            messages.warning(request, 'Please Check the form filed and fill them before submission!.')
            return redirect('register_member')
            # print('invalid form')
            
    else:
       
        form = MemberForm()
        coordinators = Coordinator.objects.all()
        team_members = TeamMember.objects.all()
        member = User.objects.all()
       

        
        # cust_coa = Coa.objects.raw("select * from chart_of_accounts_coa where right(gl_no,3) = '200'")
        
        
        context = {
             'form': form,
             'coordinators': coordinators,
             'team_members': team_members,
             'member': member,
          
            
        }

    return render(request, 'admin_staff/register_member.html', context)

@login_required(login_url='login')
@user_passes_test(check_role_admin)
def display_all_member(request):
    member = Member.objects.all()
    return render(request, 'admin_staff/display_all_member.html', {'member': member})

@login_required(login_url='login')
@user_passes_test(check_role_admin)
def display_comment(request):
    current_user = request.user
    comment = Comment.objects.filter(team_sup=current_user)
    context = {
         'comment':comment,
         
     } 
    return render(request, 'admin_staff/display_comment.html', context)






@login_required(login_url='login')
@user_passes_test(check_role_admin)
def delete_object(request, id):
    member = get_object_or_404(Member, id=id)
    member.delete()
    return redirect('display_all_member')


@login_required(login_url='login')
@user_passes_test(check_role_admin)
def member_detail(request, id):
    member = get_object_or_404(Member, id=id)

    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(member.image) > 0:
                os.remove(member.image.path)
            member.image = request.FILES['image']
        member.first_name = request.POST.get('first_name')
        member.middle_name = request.POST.get('middle_name')
        member.last_name = request.POST.get('last_name')
        member.date_of_birth = request.POST.get('date_of_birth')
        member.email = request.POST.get('email')
        member.phone_no = request.POST.get('phone_no')
        member.gender = request.POST.get('gender')
        member.marital_status = request.POST.get('marital_status')
        member.occupation = request.POST.get('occupation')
        member.address = request.POST.get('address')
        member.nationality = request.POST.get('nationality')
        member.kcc_center = request.POST.get('kcc_center')
        member.wedding_ann = request.POST.get('wedding_ann')
        member.join = request.POST.get('join')
        member.reg_date = request.POST.get('reg_date')
        member.about = request.POST.get('about')
        member.dept = request.POST.get('dept')
        member.purpose = request.POST.get('purpose')
        member.coordinator = request.POST.get('coordinator')
        member.team_member = request.POST.get('team_member')
        member.save()
        messages.success(request, 'Account has been updated successfully!.')
        return redirect('display_all_member')
    context = {
         'member':member,
         
     }   

    return render(request, 'admin_staff/member_detail.html', {'member': member,})







# def dropdown_view(request):
#     coordinators = Coordinator.objects.all()
#     team_members = TeamMember.objects.all()
#     return render(request, 'admin_staff/register_member.html', {'coordinators': coordinators, 'team_members': team_members})




    
    
@login_required(login_url='login')
@user_passes_test(check_role_admin)
def new_comment(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.member = member
            comment.team_sup = request.user
            comment.save()
            return redirect('display_comment')
   
    else:
        form = CommentForm()
        
        
        
    context = {
         'member':member,
         'form':form,
         
        
       
         
     }
    return render(request, 'admin_staff/new_comment.html', context)