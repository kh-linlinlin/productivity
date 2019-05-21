from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import JsonResponse

from input.forms import UserForm, GroupForm
from input.models import *
from input.operatedb import * 

from users.models import Profile


def home(request):
    return render(request, 'input/home.html')

def about(request):
    users = User.objects.all()
    return render(request, 'input/about.html', {'users': users})

def introduction(request):
    return render(request, 'input/introduction.html')


class ScanView(TemplateView):

    template_name = 'input/scan.html'

    def form_invalid(self, form):
        response = super(ScanView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(ScanView, self).form_valid(form)
        if self.request.is_ajax():
            return get_user_info(response)
        else:
            return response

    def get(self, request):
        form1 = UserForm()
        form2 = GroupForm()
        args = {'form1': form1, 'form2': form2 }
        return render(request, self.template_name, args)


    def post(self, request):
        form = UserForm(request.POST)
        text = validate(form, request)    

        form = UserForm() 
        args = {'form': form, 'text': text} 
        return render(request, self.template_name, args)



def get_user_info(request):
    username = request.GET.get('username', None)
    user = User.objects.filter(username = username).first()
    profile = Profile.objects.filter(user = user).first()

    user_is_grp = profile.is_grp
    user_status = profile.status
    user_curr_task = profile.current_task
    if user_is_grp:
        members, names = get_member_list(user)
        data = {
            'status': user_status,
            'is_grp': user_is_grp,
            'task': user_curr_task,
            'members': members,
            'member_names': names
        }
    else:
        data = {
            'status': user_status,
            'is_grp': user_is_grp,
            'task': user_curr_task,
            'members': [],
            'member_names': []
        }

    return JsonResponse(data)


def get_member_list(user):
    group = Group.objects.get(curr_grp = user)
    all_members = group.users.all()
    members = []
    names = []
    for member in all_members:
        member_info = User.objects.filter(username = member.username).first()
        members.append(member_info.pk)
        names.append(member_info.username)
    print(names)
    print(members)
    return members, names


def modify_grp(request, modification, pk):
    member = User.objects.get(pk=pk)

    if modification == 'add':
        Group.add_member(request.user, member)
    elif modification == 'remove':
        Group.remove_member(request.user, member)
    return redirect('input:scan')
