from django.urls import path
from.import views
from django.views.generic import TemplateView
from shop.views import home

urlpatterns = [
    
    path('',views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>/', views.products_details, name='details'),
    path('search',views.searching,name='search'),
]

