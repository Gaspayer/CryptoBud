from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from .models import Conversation, Message

User = get_user_model()

class NewConversationForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Conversation
        fields = ('users',)

    def clean_users(self):
        users = self.cleaned_data.get('users')
        if self.instance.pk:
            users = users.exclude(pk__in=self.instance.users.all().values_list('pk', flat=True))
        if users.count() < 1:
            raise ValidationError('Select at least one user.')
        return users


class NewMessageForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))

    class Meta:
        model = Message
        fields = ('text',)

'''
from django import forms
from django.contrib.auth import get_user_model
from .models import Conversation

User = get_user_model()

class NewConversationForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Conversation
        fields = ('users',)
'''
