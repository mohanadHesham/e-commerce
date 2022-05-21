from django.urls import path ,include
from . import views
urlpatterns = [
  path('',views.home,name='home'),
  path('category.html',views.category,name='category'),
  path('men',views.men,name='men'),
  path('women',views.women,name='women'),
  path('child',views.child,name='child'),
  path('product/<int:productid>',views.product,name="product"),
  path('newArrival/',views.newArrival,name="newArrival"),

]
