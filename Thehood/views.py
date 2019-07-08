from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ProfileForm,PostForm,HoodForm
from .models import Profile,Neighbourhood,Post,HoodDetails
# Create your views here.


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user=request.user
    details=HoodDetails.objects.all()
    posts=Post.objects.all()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        postform = PostForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        if postform.is_valid():
            post = postform.save(commit=False)
            post.user = current_user
            post.neighbourhood = current_user.profile.neighbourhood
            post.save()
    else:
        form = ProfileForm()
        postform = PostForm()
    return render(request, 'profile.html',{"form":form,"posts":posts,"postform":postform,"details":details})

def timeline(request):
    hoods=Neighbourhood.objects.all()
    return render(request, 'live.html',{"hoods":hoods})
  
@login_required(login_url='/accounts/login')    
def add_hood(request):
    if request.method == 'POST':
        hoodform = HoodForm(request.POST, request.FILES)
        if hoodform.is_valid():
            upload = hoodform.save()
            return redirect('home_page')
    else:
        hoodform = HoodForm()
    return render(request,'add-hood.html',{"hoodform":hoodform})
    


@login_required(login_url='/accounts/login')
def join(request,neighbourhood_id):
    hood = Neighbourhood.objects.get(id=neighbourhood_id)
    current_user = request.user
    current_user.profile.neighbourhood = hood
    current_user.profile.save()
    return redirect('hood',neighbourhood_id)

@login_required(login_url='/accounts/login')
def leave(request,neighbourhood_id):
    current_user = request.user
    current_user.profile.neighbourhood = None
    current_user.profile.save()
    return redirect('home_page')

@login_required(login_url='/accounts/login/')
def hood(request,neighbourhood_id):
    current_user = request.user
    hood_name = current_user.profile.neighbourhood
    single_hood = Neighbourhood.objects.get(id = neighbourhood_id)
  
    return render(request,'hood.html',locals())

@login_required(login_url='/accounts/login')
def upload_business(request):
    hood = NeighborHood.objects.get(id=request.user.profile.neighborhood.id)
    if request.method == 'POST':
        businessform = BusinessForm(request.POST, request.FILES)
        if businessform.is_valid():
            upload = businessform.save(commit=False)
            upload.user=request.user
            upload.neighborHood=request.user.profile.neighborhood
            upload.save()
        return redirect('hood',request.user.profile.neighborhood.id)
    else:
        businessform = BusinessForm()
    return render(request,'Business.html',locals())
