from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index_lage"),
    path('category/<slug:slug>',views.getProductByCategory,name="products_by_category"),
    path('search',views.search,name="search"),
]
