from django.urls import path

from . import views


urlpatterns = [
    path("", views.rooms, name="rooms"),
    path("<str:slug>", views.room, name="room"),
   
    path('create_personal_chat/<int:user_id>/', views.create_personal_chat, name='create_personal_chat'),
    path('personal_chat/<str:room_slug>/', views.personal_chat, name='personal_chat'),
   
    
]