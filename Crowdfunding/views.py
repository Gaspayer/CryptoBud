from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Campaign, Pledge

@login_required
def create_campaign(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        goal = request.POST['goal']
        crypto_address = request.POST['crypto_address']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        creator = request.user
        image = request.FILES['image']

        # Create a new Campaign object and save it to the database
        campaign = Campaign(
            title=title,
            description=description,
            goal=goal,
            crypto_address=crypto_address,
            start_date=start_date,
            end_date=end_date,
            user=user,
            image=image
        )
        campaign.save()

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
