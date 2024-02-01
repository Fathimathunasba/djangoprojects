from django.shortcuts import render
from django.shortcuts import HttpResponse
from apps.models import Movie
from apps.forms import movieform


# Create your views here.
def add(request):
        if(request.method == "POST"):
            n= request.POST['n']
            d= request.POST['d']
            y= request.POST['y']
            i= request.FILES['i']
            m=Movie.objects.create(name=n,desc=d, year=y,img=i)

            m.save()
            return viewmovies(request)

        return render(request,'add.html')
def add1(request):
    form = movieform()  # empty form object
    if (request.method == "POST"):  # after form submission
        form = movieform(request.POST)  # initializing form object using request.POST
        if (form.is_valid()):
            form.save()
            return viewmovies(request)
    return render(request,'add1.html',{'form':form})
def viewmovies(request):
    movie = Movie.objects.all()
    return render(request,'viewmovies.html',{'movie':movie})
def viewmoviebyid(request,p):
    movie = Movie.objects.get(id=p)
    return render(request,'viewmovie.html',{'movie':movie})
def deletemoviebyid(request,p):
    movie= Movie.objects.get(id=p)
    movie.delete()
    return viewmovies(request)
def editmoviebyid(request,p):
    movie=Movie.objects.get(id=p)
    form=movieform(instance=movie)
    if (request.method == "POST"):  # after form submission
        form = movieform(request.POST,request.FILES,instance=movie)  # initializing form object using request.POST
        if (form.is_valid()):
            form.save()
            return viewmovies(request)
    return render(request,'add1.html',{'form': form})