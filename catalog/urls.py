from django.urls import path

from catalog.views import products_list, contacts

urlpatterns = [
    path('', products_list),
    path('contacts/', contacts)
]
