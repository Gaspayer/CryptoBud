from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from .forms import CreatorProfileForm
from .models import CreatorProfile


#@login_required
def CreatorProfileView(request, pk):
    creator_profile = CreatorProfile.objects.get(pk=pk)
    return render(request, 'creator/creator_profile.html', {'creator_profile': creator_profile})

class CreateCreatorProfileView(CreateView):
    form_class = CreatorProfileForm
    template_name = 'creator/create_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
'''
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CreatorProfile, Project

@login_required
def create_profile(request):
    if request.method == 'POST':
        bio = request.POST['bio']
        website = request.FILES.get('website')
        avatar = request.FILES.get('avatar')
        creator_profile = CreatorProfile.objects.create(user=request.user, bio=bio, website=website, avatar=avatar)
        return redirect('profile_detail', profile_id=creator_profile.id)
    else:
        return render(request, 'create_profile.html')

@login_required
def create_project(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        project = Project.objects.create(name=name, description=description, creator=request.user.creatorprofile)
        return redirect('project_detail', project_id=project.id)
    else:
        return render(request, 'create_project.html')

def profile_detail(request, profile_id):
    profile = CreatorProfile.objects.get(id=profile_id)
    return render(request, 'profile_detail.html', {'profile': profile})

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'project_detail.html', {'project': project})
'''
'''
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CreatorProfile
from .forms import CreatorProfileForm


@login_required
def create_profile(request):
    if request.method == 'POST':
        form = CreatorProfileForm(request.POST, request.FILES)
        if form.is_valid():
            creator_profile = form.save(commit=False)
            creator_profile.user = request.user
            creator_profile.save()
            return redirect('creator_profile', pk=creator_profile.pk)
    else:
        form = CreatorProfileForm()
    return render(request, 'creator/create_profile.html', {'form': form})


def creator_profile(request, pk):
    creator_profile = CreatorProfile.objects.get(pk=pk)
    return render(request, 'creator/creator_profile.html', {'creator': creator_profile})
'''
