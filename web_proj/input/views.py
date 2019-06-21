from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from input.forms import ScanForm
from input.models import Post


class ScanView(TemplateView):
    template_name = 'input/idle_scan.html'

    def get(self, request):
        form = ScanForm()
        return render(request, self.template_name, {'form': form})


    def post(self, request):
        form = ScanForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False) 
            if request.user is None:
                post.user = post['wms_id']
            else:
                print(request.user)
                post.user = request.user
            post.save()

            ### show the records done by this within the day ### 


            text = form.cleaned_data
            form = ScanForm()

        args = {'form': form, 'text': text } 
        return render(request, self.template_name, args)



