from django.urls import path
from . import views
from .views import ReactAppView

urlpatterns = [
    path('api/orders/', views.submit_order, name='submit_order'),
    path('index/', views.index, name='index'),
    path("", ReactAppView.as_view()),
]