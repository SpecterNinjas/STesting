from django.shortcuts import render
from .models import Publications
from about.models import About
from django.core.paginator import Paginator

company = About.objects.all()


def publications(request):
    all_publications = Publications.objects.all()
    publication_paginator = Paginator(all_publications, 2)
    page_num = request.GET.get('page')
    page = publication_paginator.get_page(page_num)

    context = {
        'all_publications': all_publications,
        'company': company,
        'page': page
    }
    return render(request, 'publications/nashrlar.html', context)


def international_publications(request):
    all_publications = Publications.objects.filter(pub_type='international')
    publication_paginator = Paginator(all_publications, 2)
    page_num = request.GET.get('page')
    page = publication_paginator.get_page(page_num)

    context = {
        'all_publications': all_publications,
        'company': company,
        'page': page
    }
    return render(request, 'publications/international_nashr.html', context)


def national_publications(request):
    all_publications = Publications.objects.filter(pub_type='national')
    publication_paginator = Paginator(all_publications, 2)
    page_num = request.GET.get('page')
    page = publication_paginator.get_page(page_num)

    context = {
        'all_publications': all_publications,
        'company': company,
        'page': page
    }
    return render(request, 'publications/national_nashr.html', context)
