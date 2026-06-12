from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),

    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),

    path('logout/', views.logout_page, name='logout'),
    path('add-product/', views.add_product, name='add_product'),
    path('checkout/<int:id>/', views.checkout, name='checkout'),
    path('orders/', views.orders, name='orders'),
    path('delete/<int:id>/', views.delete_product, name='delete'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('cancel-order/<int:id>/', views.cancel_order, name='cancel_order'),
]