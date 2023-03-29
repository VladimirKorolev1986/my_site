from django.urls import path
from . import views


urlpatterns = [
    path('<int:number_posts>', views.go_by_number),
    path('<str:string_posts>', views.go_by_string),
    path('', views.main_page),
]