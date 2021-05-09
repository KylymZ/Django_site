from django.urls import path
from . import views

app_name='mysite'
urlpatterns = [
    path('',views.reg),
    path('site',views.site),
    path('register/',views.Register,name='register'),
    path('login/',views.UserLogin,name='login'),
    path('logout/',views.UserLogout,name='login'),
    path('site2',views.st),
    path('site3',views.st2, name='new'),
]

