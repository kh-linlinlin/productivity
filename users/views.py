from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.forms import UserForm, UserProfileForm
from django.contrib import messages

# def register(request):
# 	form = UserCreationForm()
# 	return render(request, 'users/register.html', {'form': form})

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'users/profile.html', args)

def upload_csv(request):
	data = {}
	if "GET" == request.method:
		return render(request, "users/upload_csv.html", data)
    # if not GET, then proceed
	try:
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			messages.error(request,'File is not CSV type')
			return HttpResponseRedirect(reverse("users:upload_csv"))
        #if file is too large, return
		if csv_file.multiple_chunks():
			messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
			return HttpResponseRedirect(reverse("users:upload_csv"))

		file_data = csv_file.read().decode("utf-8")		

		lines = file_data.split("\n")
		#loop over the lines and save them in db. If error , store as string and then display
		for line in lines:						
			fields = line.split(",")
			data_dict = {}
			data_dict["username"] = fields[0]
			data_dict["pwassword"] = fields[1]
			data_dict["wms id"] = fields[2]
			data_dict["whs_id"] = fields[3]
			data_dict["email"] = fields[4]
			data_dict["name"] = fields[5]
			data_dict["default_func"] = fields[6]
			data_dict["status"] = fields[7]
			try:
				form = EventsForm(data_dict)
				if form.is_valid():
					form.save()					
				else:
					logging.getLogger("error_logger").error(form.errors.as_json())												
			except Exception as e:
				logging.getLogger("error_logger").error(repr(e))					
				pass

	except Exception as e:
		logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
		messages.error(request,"Unable to upload file. "+repr(e))

	return HttpResponseRedirect(reverse("users:upload_csv"))

#in views.py
def register(request):

	if request.method == "POST":
		uform = UserForm(data = request.POST)
		pform = UserProfileForm(data = request.POST)
		if uform.is_valid() and pform.is_valid():
			user = uform.save()
			profile = pform.save(commit = False)
			profile.user = user
			profile.save()
			messages.success(request, 'User added successfully!')
		else:
			messages.error(request, 'Error adding user')
		
	else:
		uform = UserForm()
		pform = UserProfileForm()
	return render(request, 'users/register.html', {'uform': uform, 'pform': pform}) 
            
