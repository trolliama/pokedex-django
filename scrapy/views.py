from django.shortcuts import render

# Create your views here.

def scrapy_view(request):
    return render(request, 'scrapy/scrapy_view.html', {})
