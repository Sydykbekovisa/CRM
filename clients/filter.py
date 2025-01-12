import django_filters

from .models import Client


class ClientAllFilter(django_filters.FilterSet):
    first_letter = django_filters.CharFilter(
        method='filter_by_first_letter', label='Фильтр по алфавиту'
    )

    class Meta:
        model = Client
        fields = {
            'name': ['icontains']
         }

    def filter_by_first_letter(self, queryset, name, value):
        if value:
            return queryset.filter(name__istartswith=value)
        return queryset
