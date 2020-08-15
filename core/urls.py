from django.urls import path,include
from core.views import HomePageView, FormDetailView, FormListView, ResponseListView

app_name = 'core'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('form/<int:pk>', FormDetailView.as_view(), name='form-detail'),
    path('form/', FormListView.as_view(), name='form-list'),
    path('response/', ResponseListView.as_view(), name='response-list'),

]