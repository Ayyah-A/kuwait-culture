from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Announcement

# Create your views here.
def announcement_detail(request, id):
    announcement = get_object_or_404(Announcement, id=id)
    context = {
        'announcement': announcement
    }
    return render(request, 'announcements/announcement_detail.html', context)