from django.shortcuts import render
from .models import Publications
from about.models import About


def publications(request):
    company = About.objects.all()
    all_publications = Publications.objects.all()

    context = {
        'all_publications': all_publications,
        'company': company
    }
    return render(request, 'publications/nashrlar.html', context)
