from django.urls import path

from .views import index, about, contact, register, user_login, \
    check_user, custom_dashboard, seller_dashboard, user_logout, \
    edit_profile, change_password, add_product, my_products, \
    single_product, update_product, delete_product, allProducts, \
    sendEmail, forgot_password, reset_password

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('sign_up/', register, name='signUp'),
    path('user_login/', user_login, name='user_login'),
    path('check_user/', check_user, name='check_user'),
    path('custom_dashboard/', custom_dashboard, name='custom_dashboard'),
    path('seller_dashboard/', seller_dashboard, name='seller_dashboard'),
    path('user_logout/', user_logout, name='user_logout'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('change_password/', change_password, name='change_password'),
    path('add_product/', add_product, name='add_product'),
    path('my_products/', my_products, name='my_products'),
    path('single_product/', single_product, name='single_product'),
    path('update_product/', update_product, name='update_product'),
    path('delete_product/', delete_product, name='delete_product'),
    path('allProducts/', allProducts, name='allProducts'),
    path('sendEmail/', sendEmail, name='sendEmail'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('reset_password/', reset_password, name='reset_password'),
]
