from django.shortcuts import render,redirect
from .models import Category,Product

# Create your views here.
def index(request) :
    categories = Category.objects.filter(isActive=1).order_by("name")
    return render(request,'pages/index.html',{
        'categories':categories
    })

def getProductByCategory(request, slug):
    try:
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.get(slug=slug)
        
        if not products.exists():  # Check if the queryset is empty
            return render(request, 'pages/non-category.html',{
                "category":category
            })

        return render(request, 'pages/detail.html', {
            'products': products,
            'category': category
        })
    except Category.DoesNotExist:
        # Handle the case where the category does not exist
        return render(request, 'pages/non-category.html')
    
def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        products = Product.objects.filter(isActive=1,name__icontains = q)
    else :
        return redirect("/")
    return render(request,'pages/search.html',{
        'products':products
    })
