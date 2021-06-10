from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from search.models import Search

# Create your views here.
@login_required
def index(request):
    search_history_list = Search.objects.filter(user_id=request.user.id).order_by('user_id')
    return render(request, 'search_history/index.html', context={'search_history_list': search_history_list})
