from django.urls import path

from .views import ClientListView, ClientDeleteView, ClientUpdateView, ClientAddView


urlpatterns = [
    path('list/', ClientListView.as_view(), name='client-list'),
    path('delete/<int:pk>/', ClientDeleteView.as_view(), name='delete-client'),
    path('edit/<int:pk>/', ClientUpdateView.as_view(), name='update-client'),
    path('add/', ClientAddView.as_view(), name='add-client')
]
