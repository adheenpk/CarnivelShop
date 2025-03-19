from django.shortcuts import render,get_object_or_404
from . models import *
from shop.models import categ, products
from django.db.models import Q 
from django.core.paginator import Paginator,EmptyPage,InvalidPage



# Create your views here.
# def home(request):
#     ct=categ.objects.all()
#     prod=products.objects.all().select_related('category')
#     return render(request, 'index.html', {'pr': prod, 'ct': ct})


# def home(request, c_slug=None):
#     ct = categ.objects.all()  # Load all categories
#     prodt = products.objects.all().select_related('category')  # Default: Load all products

#     if c_slug !=None:
#         c_page = get_object_or_404(categ, slug=c_slug)  # Fetch category by slug
#         prodt = products.objects.filter(category=c_page, available=True)  # Filter products

#     return render(request, 'index.html', {'pr': prodt, 'ct': ct})




def home(request, c_slug=None):
    c_page = None
    prodt = None

    if c_slug is not None:
        c_page = get_object_or_404(categ, slug=c_slug)
        prodt = products.objects.filter(category=c_page, available=True)
    else:
        prodt = products.objects.filter(available=True)

    cat = categ.objects.all()
    
    # ✅ Rename variable to avoid conflict
    paginator = Paginator(prodt, 6)  

    # ✅ Ensure 'page' is an integer, defaulting to 1 if missing
    page = request.GET.get('page', '1')
    try:
        page = int(page)
    except ValueError:
        page = 1  # Default to first page if invalid

    try:
        pro = paginator.page(page)
    except (EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)  # Return last page if out of range

    return render(request, 'index.html', {'pr': prodt, 'ct': cat, 'pg': pro})


def products_details(request, c_slug, product_slug):
    try:
        prod = products.objects.get(category__slug=c_slug, slug=product_slug)
    except products.DoesNotExist:
        return render(request, '404.html', status=404)  # Handle missing products properly

    return render(request, 'item.html', {'pr': prod})


def searching(request):
    prod = None
    query = request.GET.get('q', '')  # Get search query
    if query:
        prod = products.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))  # ✅ Use Q correctly

    return render(request, 'search.html', {'qr': query, 'pr': prod})



