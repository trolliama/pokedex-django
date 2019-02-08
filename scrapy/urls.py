from django.urls import path

from .views import scrapy_view

app_name = "scrapy"
urlpatterns = [
    path('', scrapy_view, name="index"),
]
