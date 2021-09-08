from django.urls import path

from .views import contacts, add, delete, search, view

urlpatterns = [
    path('', contacts, name='contacts'),
    path('add/', add, name='add'),
    path('delete/<int:id>/', delete, name='delete'),
    path('search/', search, name='search'),
    path('view/<int:id>/', view, name='view')
]