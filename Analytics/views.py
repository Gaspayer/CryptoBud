'''
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import PageView, Event

@login_required
def dashboard(request):
    page_views = PageView.objects.filter(user=request.user)
    events = Event.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'page_views': page_views, 'events': events})
'''

'''
from django.shortcuts import render
from django.views import View
from django.views.generic.detail import DetailView
from .models import Event

class DashboardView(View):
    def get(self, request, *args, **kwargs):
        # Fetch data for the dashboard
        events = Event.objects.all()
        # Render the dashboard template with the data
        return render(request, 'analytics/dashboard.html', {'events': events})

class EventDetailView(DetailView):
    model = Event
    template_name = 'analytics/event_detail.html'
'''
from django.views.generic import TemplateView, DetailView
from .models import Event


class DashboardView(TemplateView):
    template_name = 'analytics/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.all()
        return context

class EventDetailView(DetailView):
    model = Event
    template_name = 'analytics/event_detail.html'
