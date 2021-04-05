from django.shortcuts import render
from .models import Research
from about.models import About


def researches(request):
    company = About.objects.all()
    all_research = Research.objects.all()

    context = {
        'all_research': all_research,
        'company': company
    }
    return render(request, 'researches/researches.html', context)
