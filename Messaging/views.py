from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from django.http import Http404
from .models import Conversation, Message
from .forms import NewConversationForm, NewMessageForm


User = get_user_model()


@method_decorator(login_required, name='dispatch')
class ConversationListView(ListView):
    template_name = 'Messaging/conversation_list.html'
    context_object_name = 'conversations'

    def get_queryset(self):
        return Conversation.objects.filter(users=self.request.user)


@method_decorator(login_required, name='dispatch')
class MessageListView(ListView):
    template_name = 'Messaging/message_list.html'
    context_object_name = 'messages'

    def get_queryset(self):
        conversation_id = self.kwargs.get('conversation_id')
        conversation = Conversation.objects.filter(users=self.request.user, id=conversation_id).first()
        if conversation is None:
            raise Http404('Conversation not found.')
        return Message.objects.filter(conversation=conversation).order_by('-timestamp')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['conversation_id'] = self.kwargs.get('conversation_id')
        return context


@method_decorator(login_required, name='dispatch')
class NewConversationView(CreateView):
    template_name = 'Messaging/new_conversation.html'
    form_class = NewConversationForm
    success_url = reverse_lazy('Messaging:conversation_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


@method_decorator(login_required, name='dispatch')
class NewMessageView(CreateView):
    template_name = 'Messaging/new_message.html'
    form_class = NewMessageForm

    def form_valid(self, form):
        conversation_id = self.kwargs.get('conversation_id')
        conversation = Conversation.objects.filter(users=self.request.user, id=conversation_id).first()
        if conversation is None:
            raise Http404('Conversation not found.')
        message = form.save(commit=False)
        message.sender = self.request.user
        message.conversation = conversation
        message.save()
        return redirect('Messaging:message_list', conversation_id=conversation_id)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

'''
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib.auth import get_user_model

from .models import Conversation, Message
from .forms import NewConversationForm

User = get_user_model()

@login_required
def conversations(request):
    """Display a list of user's conversations"""
    conversations = Conversation.objects.filter(users=request.user).order_by('-last_updated')
    context = {'conversations': conversations}
    return render(request, 'messaging/conversations.html', context)

@login_required
def conversation_detail(request, conversation_id):
    """Display a conversation with messages"""
    conversation = Conversation.objects.get(id=conversation_id)
    if request.user not in conversation.users.all():
        return redirect('messaging:conversations')

    messages = conversation.messages.order_by('timestamp')
    context = {'conversation': conversation, 'messages': messages}
    return render(request, 'messaging/conversation_detail.html', context)

@login_required
def new_conversation(request):
    """Create a new conversation with another user"""
    if request.method == 'POST':
        form = NewConversationForm(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data['recipient']
            if recipient == request.user:
                form.add_error('recipient', "You can't start a conversation with yourself.")
            else:
                conversation = Conversation.objects.create()
                conversation.users.add(request.user, recipient)
                return redirect('messaging:conversation_detail', conversation_id=conversation.id)
    else:
        form = NewConversationForm()

    context = {'form': form}
    return render(request, 'messaging/new_conversation.html', context)

@login_required
@require_POST
def send_message(request, conversation_id):
    """Send a new message to a conversation"""
    conversation = Conversation.objects.get(id=conversation_id)
    if request.user not in conversation.users.all():
        return JsonResponse({'error': 'You are not authorized to access this conversation.'}, status=403)

    message_content = request.POST.get('message')
    if not message_content:
        return JsonResponse({'error': 'Message cannot be empty.'}, status=400)

    message = Message.objects.create(conversation=conversation, sender=request.user, content=message_content)
    response_data = {'success': True, 'message_id': message.id, 'timestamp': message.timestamp.strftime('%b %d, %Y, %I:%M %p')}
    return JsonResponse(response_data)
    '''

'''
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Conversation, Message

@login_required
def create_conversation(request):
    if request.method == 'POST':
        users = request.POST.getlist('users')
        conversation = Conversation.objects.create()
        conversation.users.add(request.user)
        for user_id in users:
            user = User.objects.get(id=user_id)
            conversation.users.add(user)
        return redirect('conversation_detail', conversation_id=conversation.id)
    else:
        users = User.objects.exclude(id=request.user.id)
        return render(request, 'create_conversation.html', {'users': users})

@login_required
def conversation_detail(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id, users=request.user)
    messages = conversation.message_set.all().order_by('timestamp')
    if request.method == 'POST':
        text = request.POST['text']
        message = Message.objects.create(text=text, sender=request.user, conversation=conversation)
        return redirect('conversation_detail', conversation_id=conversation.id)
    else:
        return render(request, 'conversation_detail.html', {'conversation': conversation, 'messages': messages})
'''
