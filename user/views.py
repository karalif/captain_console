from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from user.models import Profile
from user.forms.profile_form import ProfileForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html',{
        'form': UserCreationForm()
    })


@login_required
def edit_profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/edit_profile.html', {
        'form': ProfileForm(instance=profile)
})


@login_required
def profile(request):
    context = {'user': Profile.objects.filter(user=request.user).first(), 'auth': request.user.is_authenticated, 'super': request.user.is_superuser }
    return render(request,'user/profile.html', context)
