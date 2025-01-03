from django.urls import path
from .views import HomeView, ProductView, category, save_order

urlpatterns = [
    path('', HomeView.as_view(), name='product_list_url'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_detail_url'),
    path('category/<int:pk>/', category, name='category_url'),
    path('save_order', save_order, name='save_order_url'),
]
    