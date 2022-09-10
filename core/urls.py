from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('signup/', views.signup, name='signup'),
  path('setting/', views.setting, name='setting'),
  path('signin/', views.signin, name='signin'),
  path('logout/', views.logout, name='logout'),
  path('contact/<int:pk>', views.contact, name='contact')

]