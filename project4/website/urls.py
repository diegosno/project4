from django.urls import path
from .views import NewListView, NewDetailView, NewCreateView, NewUpdateView, NewDeleteView, UserNewListView
from . import views 

urlpatterns = [
    path('', NewListView.as_view(), name='website-index'),
    path('new/<int:pk>/', NewDetailView.as_view(), name='new-detail'),
    path('new/<int:pk>/update', NewUpdateView.as_view(), name='new-update'),
    path('new/<int:pk>/delete', NewDeleteView.as_view(), name='new-delete'),
    path('new/create/', NewCreateView.as_view(), name='new-create'),
    path('contact/', views.contact, name='website-contact'),
    path('user/<str:username>', UserNewListView.as_view(), name='user-news'),
]