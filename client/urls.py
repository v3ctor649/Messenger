from django.urls import path
from .import views

urlpatterns = [
    path('login', views.MyLoginView.as_view(),name = 'login'),
    path('', views.main_page, name='chat'),
    path('json/',views.get_data),
]
