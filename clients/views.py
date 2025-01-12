from django.views.generic import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django_filters.views import FilterView

from .models import Client
from .filter import ClientAllFilter


class ClientListView(FilterView):
    queryset = Client.objects.all()
    template_name = 'client-list.html'
    context_object_name = 'clients'
    filterset_class = ClientAllFilter


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'delete-confirm.html'
    success_url = reverse_lazy('client-list')


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'edit-client.html'
    fields = '__all__'
    success_url = reverse_lazy('client-list')


class ClientAddView(CreateView):
    model = Client
    template_name = 'add-client.html'
    fields = '__all__'
    success_url = reverse_lazy('client-list')
