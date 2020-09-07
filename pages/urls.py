from django.urls import path
from .views import WallPageView, HomePageView, MessagePageView, ThanksPageView

urlpatterns = [
    path('', HomePageView, name='home'),
    path('wall/', WallPageView, name='wall'),
    path('message/', MessagePageView.as_view(), name='message'),
    path('thanks/', ThanksPageView.as_view(), name='thanks'),
]