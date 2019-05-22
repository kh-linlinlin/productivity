from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from input.forms import UserForm, GroupForm
from input.models import *
from input.operatedb import * 
import json

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


    def post(request):
        if request.method == 'POST':
            form = UserForm(request.POST)
            text = validate(form, request) 
            return HttpResponse(text)

        else:
            return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )



def get_user_info(request):
    print(request)
    username = request.GET.get('username', None)
    user = User.objects.filter(username = username).first()
    profile = Profile.objects.filter(user = user).first()

    user_is_grp = profile.is_grp
    user_status = profile.status
    user_curr_task = profile.current_task

    data = {
        'status': user_status,
        'is_grp': user_is_grp,
        'task': user_curr_task
    }
    return JsonResponse(data)


def get_member_list(request):
    username = request.GET.get('username', None)
    user = User.objects.filter(username = username).first()
    group = Group.objects.get(curr_grp = user)
    all_members = group.users.all()
    members = []
    names = []
    for member in all_members:
        member_info = User.objects.filter(username = member.username).first()
        members.append(member_info.pk)
        names.append(member_info.username)

    data = {
        'members': members,
        'member_names': names
    }
    return JsonResponse(data)


def modify_grp(request, owner, modification, member):
    member = User.objects.filter(username = member).first()
    owner = User.objects.filter(username = owner).first()

    if modification == 'add':
        Group.add_member(owner, member)
        msg = member.username + " is added to " + owner.username
    elif modification == 'remove':
        Group.remove_member(owner, member)
        msg = member.username + " is removed from " + owner.username
    return HttpResponse(msg)
