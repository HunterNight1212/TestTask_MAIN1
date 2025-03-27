from django_filters import FilterSet, DateFilter, ModelChoiceFilter
from .models import DataDDS, Category, Subcategory
from django import forms


# класс/форма для фильтрации по дате, статусу, типу, категории и подкатегории
class DataDDSFilter(FilterSet):
    start_date = DateFilter(field_name='date_create', lookup_expr='date__gte',
                            widget=forms.DateInput(attrs={'type': 'date'}), label='от')
    end_date = DateFilter(field_name='date_create', lookup_expr='date__lte',
                          widget=forms.DateInput(attrs={'type': 'date'}), label='до')
    category = ModelChoiceFilter(queryset=Category.objects.all(), label='Category')
    subcategory = ModelChoiceFilter(queryset=Subcategory.objects.all(), label='Subcategory')

    class Meta:
        model = DataDDS
        fields = ['status', 'tipe', 'category', 'subcategory']
