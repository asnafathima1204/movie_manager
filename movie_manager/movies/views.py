from django.shortcuts import render,redirect
from .models import MovieInfo
from . forms import MovieForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login/')
def create(request):
    frm=MovieForm()
    if request.POST:
        # print(request.POST)
        # title =request.POST.get('title')
        # year =request.POST.get('year')
        # desc =request.POST.get('description')
        # movie_obj=MovieInfo(
        #     title=title,
        #     year=year,
        #     description=desc
        # )
        # movie_obj.save()
        frm=MovieForm(request.POST,request.FILES)
        print(request.FILES) 
        if frm.is_valid():
            frm.save()
            return redirect('create')
        else:
            print(frm.errors)
    else:
        frm=MovieForm

        
    return render(request,'create.html',{'frm':frm})

@login_required(login_url='login/')
def list(request):
    # movie_data ={
    #     'movies':[
    # {
    #     'title':'Snow White and the Seven Dwarfs',
    #     'year':1937,
    #     'summary':'The story of Snow White, a princess who befriends seven dwarfs while evading her wicked stepmother, the Queen.',
    #     'success':True,
    #     'img':'snow_white.jpg'
    # },
    # {
    #     'title':'The Lion King',
    #     'year':1994,
    #     'summary':'A young lion prince, on his journey to reclaim his rightful place as king after the death of his father, Mufasa.',
    #     'success':False,
    #     'img':'the_lion_king.jpg'
    # },
    # {
    #     'title':'Frozen',
    #     'year':2013,
    #     'summary':'The story of sisters Elsa and Anna, who embark on a journey to save their kingdom from eternal winter, discovering the true meaning of sisterhood along the way.',
    #     'success':True,
    #     'img':'frozen.jpg'
    # }]} 
    # print(request.session)
    recent_visits=request.session.get('recent_visits',[])
    count=request.session.get('count',0)
    count=int(count)
    count=count+1
    recent_movie_set=MovieInfo.objects.filter(pk__in=recent_visits)
    request.session['count']=count
    # visits=int(request.COOKIES.get('visits',0))
    # visits=visits+1
    movie_set=MovieInfo.objects.all()
    print(movie_set) 
    response=render(request,'list.html',{'movies':movie_set,
                                         'count': count,
                                         'recent_movies':recent_movie_set})
    # response.set_cookie('visits',visits)
    return response

@login_required(login_url='login/')
def edit(request,pk): 
    instance_to_be_edited=MovieInfo.objects.get(pk=pk)
    if request.POST:
        # title =request.POST.get('title')
        # year =request.POST.get('year')
        # description =request.POST.get('description')
        # instance_to_be_edited.title=title
        # instance_to_be_edited.year=year
        # instance_to_be_edited.description=description
        frm=MovieForm(request.POST,instance=instance_to_be_edited)
        if frm.is_valid():
            instance_to_be_edited.save()
    else:
        
        recent_visits=request.session.get('recent_visits',[])
        recent_visits.insert(0,pk)
        request.session['recent_visits']=recent_visits
        frm=MovieForm(instance=instance_to_be_edited)

    return render(request,'create.html',{'frm':frm})

@login_required(login_url='login/')
def delete(request,pk):
    instance=MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_set=MovieInfo.objects.all()
    print(movie_set) 
    return render(request,'list.html',{'movies':movie_set})
    # return render(request,'delete.html')
