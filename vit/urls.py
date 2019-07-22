from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .import views
app_name = "users"


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='vit/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='vit/logout.html'), name="logout"),
    path('stud/', views.stud, name='stud'),
]
