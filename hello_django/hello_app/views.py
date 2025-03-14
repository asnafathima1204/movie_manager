from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def print_hello(requset):
#     return HttpResponse("<b>hello django</b>")

def print_hello(request):
    movie_data ={'movies':[{
        'title':'Godfather',
        'year':1990,
        'summary':'story of underworld kin',
        'success':True,
    },
    {
        'title':'Titanic',
        'year':2002,
        'summary':'story of underworld kin',
        'success':False,
    },
    {
        'title':'Goldfish',
        'year':1980,
        'summary':'story of underworld kin',
        'success':True,
    }]}
    return render(request,'hello.html',movie_data)
