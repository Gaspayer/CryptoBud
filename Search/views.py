from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import SearchResult, SearchQuery

@login_required
def search(request):
    query = request.GET.get('q')
    if query:
        SearchQuery.objects.create(query=query, user=request.user)
        search_results = SearchResult.objects.filter(query__query=query)
    else:
        search_results = None
    return render(request, 'search_results.html', {'search_results': search_results, 'query': query})
