from django.urls import path
from Animatrix.views import AnimatrixConfig

urlpatterns = [
    path('', AnimatrixConfig),
]