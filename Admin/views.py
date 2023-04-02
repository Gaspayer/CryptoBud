from django.contrib.admin.models import LogEntry
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.contenttypes.models import ContentType
from django.views.generic import TemplateView, ListView, DetailView
from django.utils.decorators import method_decorator


#@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'admin/admin_dashboard.html'

@method_decorator(permission_required('admin.view_logentry'), name='dispatch')
class LogEntryListView(ListView):
    model = LogEntry
    template_name = 'admin/log_entry_list.html'
    paginate_by = 10

@method_decorator(permission_required('admin.view_logentry'), name='dispatch')
class LogEntryDetailView(DetailView):
    model = LogEntry
    template_name = 'admin/log_entry_detail.html'

@method_decorator(permission_required('contenttypes.view_contenttype'), name='dispatch')
class ContentTypeListView(ListView):
    model = ContentType
    template_name = 'admin/content_type_list.html'

@method_decorator(permission_required('contenttypes.view_contenttype'), name='dispatch')
class ContentTypeDetailView(DetailView):
    model = ContentType
    template_name = 'admin/content_type_detail.html'

@method_decorator(permission_required('auth.view_permission'), name='dispatch')
class PermissionListView(ListView):
    #queryset = Permission.objects.select_related('content_type')
    template_name = 'admin/permission_list.html'
'''
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.contrib.admin.utils import quote

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('home')
    log_entries = LogEntry.objects.all().order_by('-action_time')[:10]
    content_types = ContentType.objects.all()
    permissions = Permission.objects.all()
    return render(request, 'admin_dashboard.html', {'log_entries': log_entries, 'content_types': content_types, 'permissions': permissions})

@login_required
def view_log_entry(request, log_entry_id):
    if not request.user.is_staff:
        return redirect('home')
    log_entry = get_object_or_404(LogEntry, id=log_entry_id)
    object_id = log_entry.object_id
    content_type_id = log_entry.content_type_id
    try:
        content_type = ContentType.objects.get(id=content_type_id)
        model_class = content_type.model_class()
        object_instance = model_class.objects.get(id=object_id)
    except:
        object_instance = None
    return render(request, 'log_entry_detail.html', {'log_entry': log_entry, 'object_instance': object_instance, 'content_type_id': content_type_id, 'object_id': object_id})
'''
