'''
from django.urls import path
from .views import (
    WalletDetailView,
    CreateWalletView,
    SendTransactionView,
)

urlpatterns = [
    path('wallet/<int:pk>/', WalletDetailView.as_view(), name='wallet_detail'),
    path('wallet/create/', CreateWalletView.as_view(), name='create_wallet'),
    path('transaction/send/', SendTransactionView.as_view(), name='send_transaction'),
]
'''
