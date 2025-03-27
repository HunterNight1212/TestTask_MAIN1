from django.urls import path
from .views import *
# пути связывающие view, html шаблоны
urlpatterns = [
    path('', DataDDSList.as_view(), name='dataDDS_list'),
    path('<int:pk>', DataDDSDetail.as_view(), name='dataDDS_detail'),
    path('create/', DataDDSCreate.as_view(), name='data_create'),
    path('<int:pk>/update/', DataDDSUpdate.as_view(), name='data_update'),
    path('<int:pk>/delete/', DataDDSDelete.as_view(), name='data_delete'),
    path('status/', StatusList.as_view(), name='status_list'),
    path('create/status', StatusCreate.as_view(), name='status_create'),
    path('<int:pk>/update/status', StatusUpdate.as_view(), name='status_update'),
    path('<int:pk>/delete/status', StatusDelete.as_view(), name='status_delete'),
    path('tipe/', TipeList.as_view(), name='tipe_list'),
    path('create/tipe', TipeCreate.as_view(), name='tipe_create'),
    path('<int:pk>/update/tipe', TipeUpdate.as_view(), name='tipe_update'),
    path('<int:pk>/delete/tipe', TipeDelete.as_view(), name='tipe_delete'),
    path('category/', CategoryList.as_view(), name='category_list'),
    path('create/category', CategoryCreate.as_view(), name='category_create'),
    path('<int:pk>/update/category', CategoryUpdate.as_view(), name='category_update'),
    path('<int:pk>/delete/category', CategoryDelete.as_view(), name='category_delete'),
    path('subcategory/', SubCategoryList.as_view(), name='subcategory_list'),
    path('create/subcategory', SubCategoryCreate.as_view(), name='subcategory_create'),
    path('<int:pk>/update/subcategory', SubCategoryUpdate.as_view(), name='subcategory_update'),
    path('<int:pk>/delete/subcategory', SubCategoryDelete.as_view(), name='subcategory_delete'),











]