from django.urls import path
from .views import NewListView, NewDetailView, NewCreateView
from . import views 

urlpatterns = [
    path('', NewListView.as_view(), name='website-index'),
    path('new/<int:pk>/', NewDetailView.as_view(), name='new-detail'),
    path('new/new/', NewCreateView.as_view(), name='new-create'),
    path('contact/', views.contact, name='website-contact'),
]