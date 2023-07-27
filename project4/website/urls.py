from django.urls import path
from .views import NewListView, NewDetailView
from . import views 

urlpatterns = [
    path('', NewListView.as_view(), name='website-index'),
    path('new/<int:pk>/', NewDetailView.as_view(), name='new-detail'),
    path('contact/', views.contact, name='website-contact'),
]