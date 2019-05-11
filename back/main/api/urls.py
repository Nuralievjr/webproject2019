from django.contrib import admin
from django.urls import path
from api import views


urlpatterns = [
    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>', views.CategoryDetail.as_view()),
    path('category/<int:pk>/products', views.CategoryProductList.as_view()),
    path('products/<int:pk>', views.ProductDetail.as_view()),
    path('products/', views.Products.as_view()),
    path('products/popular', views.ProductsPopular.as_view()),
    path('contact/us',views.Contact.as_view()),
    path('products/<int:pk>/ivisit',views.putLike),
    path('registration', views.CreateUser.as_view())

]


