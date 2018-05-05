from . import views
from django.urls import path

urlpatterns = [
    path('', views.miroAPI.as_view(), name='revAPI'),
]