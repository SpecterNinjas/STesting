from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Video
from about.models import About

company = About.objects.all()


def videos(request):
    all_video = Video.objects.all()
    video_paginator = Paginator(all_video, 1)
    num = request.GET.get('page')
    page = video_paginator.get_page(num)

    context = {
        'all_video': all_video,
        'company': company,
        'page': page
    }
    return render(request, 'videos/videos.html', context)


def student_videos(request):
    all_video = Video.objects.filter(video_type='students')
    video_paginator = Paginator(all_video, 2)
    num = request.GET.get('page')
    page = video_paginator.get_page(num)

    context = {
        'all_video': all_video,
        'company': company,
        'page': page
    }
    return render(request, 'videos/student_videos.html', context)


def teacher_videos(request):
    all_video = Video.objects.filter(video_type='teachers')
    video_paginator = Paginator(all_video, 2)
    num = request.GET.get('page')
    page = video_paginator.get_page(num)

    context = {
        'all_video': all_video,
        'company': company,
        'page': page
    }
    return render(request, 'videos/teacher_videos.html', context)


def parents_videos(request):
    all_video = Video.objects.filter(video_type='parents')
    video_paginator = Paginator(all_video, 2)
    num = request.GET.get('page')
    page = video_paginator.get_page(num)

    context = {
        'all_video': all_video,
        'company': company,
        'page': page
    }
    return render(request, 'videos/parents_videos.html', context)
