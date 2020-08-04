from django.shortcuts import render

## dummy posts 

posts = [
    {'author':'admin', 'title':'Post 1', 'content':'First Post' ,'date_posted':'August 3, 2020'},
    {'author': 'testuser', 'title':'Post 2', 'content':'Second Post', 'date_posted':'August 4, 2020'}
]

# Create your views here.
def home(request):
    context = {'posts': posts }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})