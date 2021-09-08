from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from contacts.views import contacts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', include('contacts.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', contacts, name='contacts'),
]
