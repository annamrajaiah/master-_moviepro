from django.shortcuts import render
from testapp.models import Movie
from testapp.forms import MovieForm

# Create your views here.
def movie_view (request):
    return render(request,'testapp/index.html')

def addmovie(request):
    form = MovieForm()
    if request.method=='POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return movie_view(request)
    return render(request,'testapp/add.html',{'form':form})

def list_view(request):
    movies_list=Movie.objects.all()
    return render(request,'testapp/list.html',{'movies_list':movies_list})



