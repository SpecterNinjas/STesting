from django.shortcuts import render

from .models import Video
from about.models import About


def videos(request):
    company = About.objects.all()
    all_video = Video.objects.all()

    context = {
        'all_video': all_video,
        'company': company
    }
    return render(request, 'videos/videos.html', context)
