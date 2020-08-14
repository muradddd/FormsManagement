from django.urls import path
from core.views import HomePageView, FormDetailView, FormListView, ResponseListView

app_name = 'core'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]