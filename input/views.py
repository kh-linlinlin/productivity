from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder


from input.forms import  ActionForm, GroupForm
from input.models import *
from input.operatedb import * 
import json, datetime

from users.models import Profile


def home(request, *args, **kwargs):
    return render(request, 'input/home.html', {})

def get_data(request, *args, **kwargs):
    queryset =  Profile.objects.values('name', 'current_task')
    current_tasks = json.loads(json.dumps(list(queryset), cls=DjangoJSONEncoder))
    
    labels = []
    tabledata = {}
    chartdata = {}

    for v in current_tasks:
        task = v['current_task']
        if task not in labels:
            labels.append(task)
            chartdata[task] = 1
            tabledata[task] = {}
            tabledata[task]['numbers'] = 1
            tabledata[task]['names'] = [v['name']]
        else:
            chartdata[task] += 1
            tabledata[task]['numbers'] += 1
            tabledata[task]['names'].append(v['name'])

    info = {
     "labels": labels,
     "tabledata": tabledata, 
     "chartdata": list(chartdata.values()),  
    }

    return JsonResponse(info)

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
        form1 = ActionForm()
        form2 = GroupForm()
        posts = Post.objects.filter(ctime__gte=datetime.datetime.now().date()).order_by('-ctime')
        args = {'form1': form1, 'form2': form2 , 'posts': posts}
        return render(request, self.template_name, args)


    def post( request):
        print(request)
        if request.method == 'POST':
            form = ActionForm(request.POST)
            text = validate(form, request, update_status = True) 
            return HttpResponse(text)

        else:
            return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

    def record(request):
        if request.method == 'POST':
            form = ActionForm(request.POST)
            text = validate(form, request, update_status = False) 
            return JsonResponse(text)

        else:
            return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )



def get_user_info(request):
    username = request.GET.get('username', None)
    user = User.objects.filter(username = username).first()
    profile = Profile.objects.filter(user = user).first()

    user_is_grp = True if int(profile.is_grp) == 1 else False
    user_status = profile.status
    user_curr_task = profile.current_task

    data = {
        'status': user_status,
        'is_grp': user_is_grp,
        'task': user_curr_task,
    }
    return JsonResponse(data)


def get_member_list(request):
    username = request.GET.get('username', None)
    user = User.objects.filter(username = username).first()
    group = Group.objects.get(curr_grp = user)
    group_profile = Profile.objects.filter(user = user).first()
    group_status = group_profile.status
    all_members = group.users.all()
    members = []
    names = []
    for member in all_members:
        member_info = User.objects.filter(username = member.username).first()
        member_profile = Profile.objects.filter(user = member_info).first()
        if group_status == member_profile.status:
            members.append(member_info.pk)
            names.append(member_info.username)
        else:
            Group.remove_member(user, member)

    data = {
        'members': members,
        'member_names': names
    }
    return JsonResponse(data)


def modify_grp(request, owner, modification, member):
    member = User.objects.filter(username = member).first()
    owner = User.objects.filter(username = owner).first()

    if modification == 'add':
        member_profile = Profile.objects.filter(user = member).first()
        if member_profile.status == 2:
            msg = "Currently in other tasks"
            print(msg)
            return HttpResponse(msg)
        else:
            Group.add_member(owner, member)
            msg = member.username + " is added to " + owner.username
    elif modification == 'remove':
        Group.remove_member(owner, member)
        msg = member.username + " is removed from " + owner.username
    return HttpResponse(msg)


def check_task(request):
    task = request.GET.get('task', None)
    need_output = Task.objects.get(task_code = task).output_record 
    data = {
        'need_output': need_output
    }
    return JsonResponse(data)