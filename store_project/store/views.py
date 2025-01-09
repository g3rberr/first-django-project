from django.shortcuts import render
from store.models import *
from django.db.models import Q
from django.views.generic import ListView, DetailView
from .utils import CategoriesMixin

class HomeView(ListView, CategoriesMixin):
    model = Product
    
    
    def get_queryset(self):
        search_query = self.request.GET.get('search', None)
        if search_query:
            return Product.objects.filter(
                Q(title__icontains=search_query)
                |
                Q(info__icontains=search_query)
            )
        return Product.objects.all()


class ProductView(DetailView, CategoriesMixin):
    model = Product


class CategoryView(DetailView, CategoriesMixin):
    model = Category
    template_name = 'store/category.html'
    

    
    
def save_order(request):
    order = Order()
    order.name = request.POST['user_name']
    order.email = request.POST['user_email']
    order.product = Product.objects.get(
        pk=request.POST['product_id']
        )
    order.save()
    return render(
        request,
        'store/order.html',
        context={
            'order_name': order.name,
            'order_product': order.product,
        }
    )
    