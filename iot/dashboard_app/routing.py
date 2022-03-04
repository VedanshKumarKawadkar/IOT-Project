import imp
from django.urls import path
from .consumers import GraphConsumer

ws_urlpatterns = [
    path("ws/graphs/", GraphConsumer.as_asgi())
]