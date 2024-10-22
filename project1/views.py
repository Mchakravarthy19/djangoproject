from django.shortcuts import render

# Create your views here.
def home_view(requests):
    return render(requests,'project1\home.html')

