
from learning_users import views
from django.urls import path
app_name='learning_users'
urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login')
]