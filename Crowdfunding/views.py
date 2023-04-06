from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Fundraiser, Pledge

@login_required
def create_fundraiser(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        goal = request.POST['goal']
        crypto_address = request.POST['crypto_address']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        creator = request.user
        image = request.FILES['image']

        # Create a new Fundraiser object and save it to the database
        fundraiser = Fundraiser(
            title=title,
            description=description,
            goal=goal,
            crypto_address=crypto_address,
            start_date=start_date,
            end_date=end_date,
            creator=creator,
            image=image
        )
        fundraiser.save()

        return redirect('crowdfunding:fundraiser_detail', fundraiser_id=fundraiser.id)
    else:
        return render(request, 'create_fundraiser.html')

@login_required
def contribute(request, fundraiser_id):
    fundraiser = get_object_or_404(Campaign, id=fundraiser_id)
    if request.method == 'POST':
        amount = request.POST['amount']
        pledge = Pledge.objects.create(amount=amount, fundraiser=fundraiser, backer=request.user)
        return redirect('fundraiser_detail', fundraiser_id=fundraiser.id)
    else:
        return render(request, 'contribute.html', {'fundraiser': fundraiser})

def fundraiser_detail(request, fundraiser_id):
    fundraiser = get_object_or_404(Fundraiser, pk=fundraiser_id)
    return render(request, 'fundraiser_detail.html', {'fundraiser': fundraiser})

@login_required
def edit_fundraiser(request, fundraiser_id):
    fundraiser = get_object_or_404(Fundraiser, pk=fundraiser_id)

    if request.user != fundraiser.owner:
        return redirect('fundraiser_detail', fundraiser_id=fundraiser_id)

    if request.method == 'POST':
        field_name = request.POST.get('field_name')
        field_value = request.POST.get('field_value')

        if field_name in ['title', 'description', 'goal_amount', 'crypto_address', 'start_date', 'end_date']:
            setattr(fundraiser, field_name, field_value)
            fundraiser.save()
            return redirect('fundraiser_detail', fundraiser_id=fundraiser_id)

    # Render the form for editing the fundraiser, or handle this with AJAX - my comment: i dont think its necessary

@login_required
def my_fundraisers(request):
    fundraisers = Fundraiser.objects.filter(creator=request.user)
    return render(request, 'my_fundraisers.html', {'fundraisers': fundraisers})
