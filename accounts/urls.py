from django.urls import path
from .views import SignupPageView

urlpattrns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
]