from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import JsonResponse

from input.forms import ScanForm, EndForm
from input.models import Post, Group
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

    template_name = 'input/idle_scan.html'

    def get(self, request):
        form = ScanForm()
        members = get_member_list(request.user)

        args = {'form': form, 'members': members}
        return render(request, self.template_name, args)


    def post(self, request):
        form = ScanForm(request.POST)
        text = validate(form, request, action = 'Start')     

        ### show the records done by this within the day ### 

        form = ScanForm() 
        args = {'form': form, 'text': text } 
        return render(request, self.template_name, args)



def modify_grp(request, modification, pk):
    member = User.objects.get(pk=pk)

    if modification == 'add':
        Group.add_member(request.user, member)
    elif modification == 'remove':
        Group.remove_member(request.user, member)
    return redirect('input:scan')




class EndView(TemplateView):
    template_name = 'input/in_task_scan.html'

    def get(self, request):
        form = EndForm()
        return render(request, self.template_name, {'form': form})


    def post(self, request):
        form = EndForm(request.POST)
        text = validate(form, request, action = 'End')

        ### show the records done by this within the day ### 

        form = EndForm()

        args = {'form': form, 'text': text } 
        return render(request, self.template_name, args)
