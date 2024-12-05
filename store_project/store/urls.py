from django.urls import path
from .views import product_list, product_detail

urlpatterns = [
    path('store/', product_list),
    path('detail/', product_detail, name='detail')
]
