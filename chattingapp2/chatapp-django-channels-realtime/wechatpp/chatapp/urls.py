from django.urls import path

from . import views


urlpatterns = [
    path("", views.rooms, name="rooms"),
    path("<str:slug>", views.room, name="room"),
    #path("<str:slug>", views.room, name="japri"),
    path('create_personal_chat/<int:user_id>/', views.create_personal_chat, name='create_personal_chat'),
    path('personal_chat/<int:room_id>/', views.personal_chat_room, name='personal_chat_room'),
    
]