from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("products/new/", views.product_create, name="product_create"),
    path("products/<int:pk>/edit/", views.product_update, name="product_update"),
    path("products/<int:pk>/delete/", views.product_delete, name="product_delete"),
    path("orders/new/", views.order_create, name="order_create"),
]