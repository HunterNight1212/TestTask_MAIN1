from django import forms
from .models import DataDDS, Category, Subcategory, Tipe


# основная форма для работы с Update и Create
class DataDDSForm(forms.ModelForm):
    class Meta:
        model = DataDDS
        fields = [
            'status',
            'tipe',
            'category',
            'subcategory',
            'summ',
            'comment',
        ]
