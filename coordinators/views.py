from tokenize import Comment
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.models import User

from accounts.views import check_role_coordinator
from follow_app.forms import CommentForm, MemberForm
from django.contrib import messages

from follow_app.models import Team_Lead, Member, TeamMember
from follow_app.models import Comment


# Create your views here.

@user_passes_test(check_role_coordinator)
def coor_register_member(request):
    
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        
        
       
        if form.is_valid():
            
            # type_of_account = form.cleaned_data['type_of_account']
            # image = form.cleaned_data['image']
            # first_name = form.cleaned_data['first_name']
            # middle_name = form.cleaned_data['middle_name']
            # last_name = form.cleaned_data['last_name']
            # date_of_birth = form.cleaned_data['date_of_birth']
            # email = form.cleaned_data['email']
            # phone_no = form.cleaned_data['phone_no']
            # gender = form.cleaned_data['gender']
            # marital_status = form.cleaned_data['marital_status']
            # occupation = form.cleaned_data['occupation']
       
            # address = form.cleaned_data['address']
            # nationality = form.cleaned_data['nationality']
         
            # kcc_center = form.cleaned_data['kcc_center']
            # wedding_ann = form.cleaned_data['wedding_ann']
            # join = form.cleaned_data['join']
            # # reg_date = form.cleaned_data['reg_date']
            # about = form.cleaned_data['about']
            # dept = form.cleaned_data['dept']
            # purpose = form.cleaned_data['purpose']
            # team_lead = form.cleaned_data['team_lead']
            # team_member = form.cleaned_data['team_member']
            
            # customer = Customer(first_name=first_name,middle_name=middle_name,last_name=last_name,date_of_birth=date_of_birth,email=email,phone_no=phone_no,gender=gender,marital_status=marital_status,occupation=occupation,district=district,acct_off=acct_off,id_type=id_type,id_no=id_no,issued_authority=issued_authority,issued_state=issued_state,expiry_date=expiry_date,address=address,nationality=nationality,state=state,local_govt=local_govt,city=city,landmark=landmark,next_of_kin=next_of_kin,next_address=next_address,next_phone_no=next_phone_no,type_of_account=type_of_account, customer= True)
            # member = form.save(commit=False)
            
            # member.staff = staff.objects.get(user=request.user)
            # user = staff.objects.get(user=request.user)
            form = form.save(commit=False)
            
            form.user = request.user
          
            form.save()
            messages.success(request, 'Account has been registered successfully!.')
            return redirect('coor_display_all_member')
        
    
        
        else:
            messages.warning(request, form.errors)
            messages.warning(request, 'Please Check the form filed and fill them before submission!.')
            return redirect('coor_register_member')
            # print('invalid form')
            
    else:
       
        form = MemberForm()
        current_user = request.user
        team_lead = Team_Lead.objects.filter(name=current_user)
        team_members = TeamMember.objects.all()
        member = User.objects.all()
       

        
        # cust_coa = Coa.objects.raw("select * from chart_of_accounts_coa where right(gl_no,3) = '200'")
        
        
        context = {
             'form': form,
             'team_lead': team_lead,
             'team_members': team_members,
             'member': member,
          
            
        }
   

    return render(request, 'coordinators/coor_register_member.html', context)



def coor_member_detail(request, id):
    member = get_object_or_404(Member, id=id)
    
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been Updated successfully!.')
            return redirect('coor_display_all_member')
    else:
        form = MemberForm(instance=member)
        current_user = request.user
        team_lead = Team_Lead.objects.filter(name=current_user)
        team_members = TeamMember.objects.all()
    return render(request, 'coordinators/coor_member_detail.html', {'form': form, 'member': member, 'team_lead': team_lead, 'team_members': team_members,})


@user_passes_test(check_role_coordinator)
def coor_display_comment(request):
    current_user = request.user
    comment = Comment.objects.filter(coor_comm=current_user)
    mem_com = Member.objects.all()
    context = {
         'comment':comment,
         'mem_com':mem_com,
         
     } 
    return render(request, 'coordinators/coor_display_comment.html', context)

@login_required(login_url='login')
@user_passes_test(check_role_coordinator)
def coor_display_all_member(request):
    current_user = request.user
    member = Member.objects.filter(user=current_user).filter(status='1')

    return render(request, 'coordinators/coor_display_all_member.html', {'member': member})

# @login_required(login_url='login')
# def coor_display_comment(request):
#     return render(request, 'coordinators/display_comment.html')


@login_required(login_url='login')
@user_passes_test(check_role_coordinator)
def coor_new_comment(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.member = member
            comment.team_sup = request.user
            # comment.phone_number = UserProfile.phone_number
            comment.save()
            return redirect('coor_display_comment')
   
    else:
        form = CommentForm()
    context = {
         'member':member,
         'form':form,   
     }
    return render(request, 'coordinators/coor_new_comment.html', context)




@login_required(login_url='login')
@user_passes_test(check_role_coordinator)
def my_team_member_list(request):
    current_user = request.user
    member = Member.objects.filter(taem_lead=current_user)
    context = {
         'member':member,
     } 
    return render(request, 'coordinators/my_team_member_list.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_coordinator)
def my_team_member_comment(request):
    current_user = request.user
    member = Comment.objects.filter(coor_comm=current_user)
    context = {
         'member':member,
     } 
    return render(request, 'coordinators/my_team_member_comment.html', context)