from django.urls import path
from app1.views import *
from app1 import views
app_name='base1_app'

urlpatterns = [
    path('index/',views.index,name='index'),
    path('login_form/',views.login_form,name='login_form'),
    path('featured/',views.featured,name='featured'),
    
]
