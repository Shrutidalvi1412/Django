from django.urls import include,path
from electronics import views
urlpatterns=[
    path('Product/',views.product_detail,name="product_detail"),
    path('update/<int:id>/',views.update_product,name='update_product'),
    path('delete_product/<int:id>',views.delete_product,name='delete_product')
    
    ]
