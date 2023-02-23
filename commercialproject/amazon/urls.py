from django.urls import path
from . import views
app_name = 'amazon'
urlpatterns = [

    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:products_slug>/',views.proDetail,name='prodCatdetail')

]