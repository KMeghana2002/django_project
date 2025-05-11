from django.urls import path
from app1.views import *
from app2 import views
app_name='base2_app'

urlpatterns = [
    path('arrivals/',views.arrivals,name='arrivals'),
    path('blogs/',views.blogs,name='blogs'),
    path('reviews/',views.reviews,name='reviews'),
    
]