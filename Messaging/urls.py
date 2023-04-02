from django.urls import path
from .views import ConversationListView, MessageListView, NewConversationView, NewMessageView

app_name = 'Messaging'

urlpatterns = [
    path('conversation/<int:pk>/', MessageListView.as_view(), name='conversation'),
    path('new_conversation/', NewConversationView.as_view(), name='new_conversation'),
    path('new_message/<int:pk>/', NewMessageView.as_view(), name='new_message'),
    path('', ConversationListView.as_view(), name='conversation_list'),
]

'''
from django.urls import path

from .views import ConversationListView, MessageListView, NewConversationView, NewMessageView

app_name = 'Messaging'

urlpatterns = [
    path('', ConversationListView.as_view(), name='conversation_list'),
    path('<int:pk>/', MessageListView.as_view(), name='message_list'),
    path('new/', NewConversationView.as_view(), name='new_conversation'),
    path('<int:pk>/new/', NewMessageView.as_view(), name='new_message'),
]
'''
