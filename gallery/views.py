from django.shortcuts import render, get_object_or_404

from .models import Photo


def index(request):
    photos = Photo.objects.all()

    context = {
        'photos': photos,
    }

    return render(request, 'gallery/index.html', context)


def detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    context = {
        'photo': photo,
    }

    return render(request, 'gallery/detail.html', context)
