from django import forms
from input.models import Post
from django.contrib.auth.models import User 

class ScanForm(forms.ModelForm):
	## fields in one form
	user_name = forms.CharField()
	task = forms.CharField()

	class Meta:
		model = Post 
		fields = ('user_name', 'task')

class EndForm(forms.ModelForm):
	## fields in one form
	work_complete = forms.CharField()

	class Meta:
		model = Post 
		fields = ('work_complete',)


# class groupScanFrom(forms.ModelForm):

#     user_name = forms.CharField(required=True)

#     def __init__(self, *args, **kwargs):

#         super().__init__(*args, **kwargs)
#         members = User.objects.filter(
#             profile = self.instance
#         )
#         for i in range(len(members) + 1):
#             field_name = 'members_%s' % (i,)
#             self.fields[field_name] = forms.CharField(required=False)
#             try:
#                 self.initial[field_name] = interests[i].interest
#             except IndexError:
#                 self.initial[field_name] = ""
#         # create an extra blank field
#         field_name = 'members_%s' % (i + 1,)
#         self.fields[field_name] = forms.CharField(required=False)

