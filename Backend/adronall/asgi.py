"""
ASGI config for adronall project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application
# from channels.routing import protocolTypeRoute,URLRouter 
# from home.consumers import *
# from django.urls import path

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "adronall.settings")
# application = get_asgi_application()

# ws_patterns=[
#     path('ws/test/',TestConsumer)
# ]
# application=protocolTypeRoute({
#     'websocket': URLRouter(ws_patterns),
#     "http": application,
# })

import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adronall.settings')
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    
    # Just HTTP for now. (We can add other protocols later.)
})