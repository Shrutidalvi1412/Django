from django.urls import include,path
from electronics import views
urlpatterns=[path('Product/',views.product_detail,name="product_detail")]
