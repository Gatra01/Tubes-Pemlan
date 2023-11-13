from django.urls import path , include,re_path
from .consumers import ChatConsumer, PersonalChatConsumer  # Import the consumers module



websocket_urlpatterns = [
	path("ws/<room_slug>/" , ChatConsumer.as_asgi) ,
    #re_path(r'^ws/(?P<room_slug>[^/]+)/$', ChatConsumer.as_asgi()),
    path("ws/personal_chat/<str:room_slug>/" , PersonalChatConsumer.as_asgi) ,
    #e_path(r'^ws/personal/(?P<room_slug>[^/]+)/$', PersonalChatConsumer.as_asgi()),
    #re_path(r'^ws/(?P<room_slug>[^/]+)/$', PersonalChatConsumer.as_asgi()),
]