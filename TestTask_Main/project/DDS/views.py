from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from .models import *
from .filters import DataDDSFilter
from .forms import DataDDSForm


# представления образующие логику приложения

# представления для работы с записями
class DataDDSList(ListView):
    model = DataDDS
    ordering = '-date_create'
    template_name = 'data_list.html'
    context_object_name = 'datas'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = DataDDSFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class DataDDSDetail(DetailView):
    model = DataDDS
    template_name = 'data_detail.html'
    context_object_name = 'data'


class DataDDSCreate(CreateView):
    model = DataDDS
    template_name = 'data_create.html'
    form_class = DataDDSForm
    success_url = '/'


class DataDDSUpdate(UpdateView):
    model = DataDDS
    template_name = 'data_create.html'
    form_class = DataDDSForm
    success_url = '/'


class DataDDSDelete(DeleteView):
    model = DataDDS
    template_name = 'data_delete.html'
    success_url = '/'


# для работы со статусом
class StatusList(ListView):
    model = Status
    template_name = 'status/status_list.html'
    context_object_name = 'status'


class StatusCreate(CreateView):
    model = Status
    template_name = 'status/status_create.html'
    fields = ['name']
    success_url = '/'


class StatusUpdate(UpdateView):
    model = Status
    template_name = 'status/status_create.html'
    fields = ['name']
    success_url = '/'


class StatusDelete(DeleteView):
    model = Status
    template_name = 'status/status_delete.html'
    success_url = '/'


# для работы с типами
class TipeList(ListView):
    model = Tipe
    template_name = 'tipe/tipe_list.html'
    context_object_name = 'tipes'


class TipeCreate(CreateView):
    model = Tipe
    template_name = 'tipe/tipe_create.html'
    fields = ['name', 'category']
    success_url = '/'


class TipeUpdate(UpdateView):
    model = Tipe
    template_name = 'tipe/tipe_create.html'
    fields = ['name', 'category']
    success_url = '/'


class TipeDelete(DeleteView):
    model = Tipe
    template_name = 'tipe/tipe_delete.html'
    success_url = '/'


# для работы с категориями
class CategoryList(ListView):
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'categories'


class CategoryCreate(CreateView):
    model = Category
    template_name = 'category/category_create.html'
    fields = ['name', 'subcategory']
    success_url = '/'


class CategoryUpdate(UpdateView):
    model = Category
    template_name = 'category/category_create.html'
    fields = ['name', 'subcategory']
    success_url = '/'


class CategoryDelete(DeleteView):
    model = Category
    template_name = 'category/category_delete.html'
    success_url = '/'


# для работы с подкатегориями
class SubCategoryList(ListView):
    model = Subcategory
    template_name = 'subcategory/subcategory_list.html'
    context_object_name = 'subcategories'


class SubCategoryCreate(CreateView):
    model = Subcategory
    template_name = 'subcategory/subcategory_create.html'
    fields = ['name']
    success_url = '/'


class SubCategoryUpdate(UpdateView):
    model = Subcategory
    template_name = 'subcategory/subcategory_create.html'
    fields = ['name']
    success_url = '/'


class SubCategoryDelete(DeleteView):
    model = Subcategory
    template_name = 'subcategory/subcategory_delete.html'
    success_url = '/'
