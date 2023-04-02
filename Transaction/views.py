from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Wallet, Transaction

@login_required
def create_wallet(request):
    if request.method == 'POST':
        address = request.POST['address']
        wallet = Wallet.objects.create(user=request.user, address=address, balance=0)
        return redirect('wallet_detail', wallet_id=wallet.id)
    else:
        return render(request, 'create_wallet.html')

@login_required
def send_transaction(request, wallet_id):
    sender = get_object_or_404(Wallet, id=wallet_id)
    if request.method == 'POST':
        receiver_address = request.POST['receiver_address']
        amount = request.POST['amount']
        receiver = Wallet.objects.get(address=receiver_address)
        if sender.balance >= amount:
            sender.balance -= amount
            receiver.balance += amount
            sender.save()
            receiver.save()
            transaction = Transaction.objects.create(amount=amount, sender=sender, receiver=receiver)
            return redirect('transaction_detail', transaction_id=transaction.id)
        else:
            error_message = 'Insufficient balance'
            return render(request, 'send_transaction.html', {'sender': sender, 'error_message': error_message})
    else:
        return render(request, 'send_transaction.html', {'sender': sender})
