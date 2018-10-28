from django.urls import path
from django.conf.urls import url
from.import views

urlpatterns = [
    path('',views.Home, name = 'home'),

    path('<int:val>/', views.detail, name = 'detail'),

    path('add/', views.add_new, name = 'new_treasure'),
    
    path('<int:val/edit/>', views.treasure_edit, name= 'edit_treasure'),

    path('login/', views.LoginForm, name = 'login'),

    path ('logout/', views.LogoutForm, name = 'logout'), 
] 