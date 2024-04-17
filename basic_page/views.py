from django.shortcuts import render
from .models import Page

# Create your views here.
def basic_page(request, tag=None, page=None):
    page_obj = None
    if tag is not None:
        page_obj = Page.objects.get(tag=tag, page=page)

    page_elements = {
        'objects': page_obj,
    }
    # Page from the theme
    return render(request, 'pages/basic_page.html', page_elements)
