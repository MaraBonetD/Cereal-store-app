from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from users.forms.profile_form import ProfileForm
from users.models import Profile


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'users/register.html', {
        'form': UserCreationForm()
    })

def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False) # we get the object but we don't save it because we excluded the user
            profile.user = request.user # we set the user attribute in the profile object as the user who sent the request
            profile.save() # then it's saved in the DB
            return redirect('profile')
    return render(request, 'users/profile.html', {
        'form': ProfileForm(instance=profile),
        'profile_picture': profile.profile_picture
    })