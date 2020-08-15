from django.urls import path,include
from accounts.views import change_password,RegisterView,CustomLoginView,Logout


app_name='accounts'

urlpatterns = [
    path('change_password/',change_password,name='change_password'),
    path('login/', CustomLoginView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('logout/',Logout.as_view(),name='logout'), 
]
