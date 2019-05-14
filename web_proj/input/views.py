from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Jiana Xu',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'testuser',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'input/home.html', context)


# input -> templates -> input -> templates for input 
def about(request):
	return render(request, 'input/about.html')