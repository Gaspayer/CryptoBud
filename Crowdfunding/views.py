from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Campaign, Pledge

@login_required
def create_campaign(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        goal = request.POST['goal']
        end_date = request.POST['end_date']
        campaign = Campaign.objects.create(name=name, description=description, goal=goal, end_date=end_date, creator=request.user)
        return redirect('campaign_detail', campaign_id=campaign.id)
    else:
        return render(request, 'create_campaign.html')

@login_required
def contribute(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    if request.method == 'POST':
        amount = request.POST['amount']
        pledge = Pledge.objects.create(amount=amount, campaign=campaign, backer=request.user)
        return redirect('campaign_detail', campaign_id=campaign.id)
    else:
        return render(request, 'contribute.html', {'campaign': campaign})
