from django.shortcuts import render
from .models import Research
from about.models import About
from django.core.paginator import Paginator

company = About.objects.all()


def researches(request):
    all_research = Research.objects.all()
    research_paginator = Paginator(all_research, 2)
    page_num = request.GET.get('page')
    page = research_paginator.get_page(page_num)
    context = {
        'all_research': all_research,
        'page': page,
        'company': company
    }
    return render(request, 'researches/researches.html', context)


def inter_researches(request):

    all_research = Research.objects.filter(research_type='international')
    research_paginator = Paginator(all_research, 2)
    page_num = request.GET.get('page')
    page = research_paginator.get_page(page_num)
    context = {
        'all_research': all_research,
        'page': page,
        'company': company
    }
    return render(request, 'researches/inter_research.html', context)


def national_researches(request):

    all_research = Research.objects.filter(research_type='national')
    research_paginator = Paginator(all_research, 2)
    page_num = request.GET.get('page')
    page = research_paginator.get_page(page_num)
    context = {
        'all_research': all_research,
        'page': page,
        'company': company
    }
    return render(request, 'researches/national_research.html', context)
