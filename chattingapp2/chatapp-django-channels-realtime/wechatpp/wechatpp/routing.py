from django.urls import path , include,re_path,url
from .consumers import ChatConsumer,PersonalChatConsumer


websocket_urlpatterns = [
	path("<room_slug>" , ChatConsumer.as_asgi()) ,
    re_path(r'^ws/(?P<room_slug>[^/]+)/$', ChatConsumer.as_asgi()),
    path("<room_slug>" , PersonalChatConsumer.as_asgi()) ,
    re_path(r'^ws/(?P<room_slug>[^/]+)/$', PersonalChatConsumer.as_asgi()),
]
'''from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from .consumers import ChatConsumer

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            [
                path('ws/chat/<str:username>/', ChatConsumer.as_asgi()),
            ]
        )
    ),
})'''
