"""
ASGI config for notification_system project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
import django
from channels.routing import ProtocolTypeRouter,URLRouter
django.setup()
from channels.auth import AuthMiddleware
from notification.routing import websocket_urlpatterns

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notification_system.settings')

application =ProtocolTypeRouter({ "http":get_asgi_application(),
"websocet":AuthMiddlewareStack(
    URLRouter(
    websocket_urlpatterns
    )
)
})
