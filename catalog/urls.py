from django.urls import path

from catalog.views import products_list, contacts, product_detail

urlpatterns = [
    path('', products_list),
    path('contacts/', contacts),
    path('product/<int:pk>', product_detail, name='product_detail' )
]
