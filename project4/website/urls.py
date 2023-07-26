from django.urls import path
from .views import NewListView
from . import views 

urlpatterns = [
    path('', NewListView.as_view(), name='website-index'),
    path('contact/', views.contact, name='website-contact'),
]