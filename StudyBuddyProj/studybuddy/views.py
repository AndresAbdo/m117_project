from django.shortcuts import render
from .models import Student, StudyGroup, ChatMessage
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    studygroups_list = StudyGroup.objects.all()
    paginator = Paginator(studygroups_list, 10)

    page = request.GET.get('page');
    studygroups = paginator.get_page(page)
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'studybuddy/index.html',
        context={'studygroups':studygroups},
    )