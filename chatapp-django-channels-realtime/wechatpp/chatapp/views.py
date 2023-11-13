from django.shortcuts import render,redirect, get_object_or_404
from .models import Room,Message,PersonalChatMessage, PersonalChatRoom
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def rooms(request):
    rooms=Room.objects.all()
    #personal_rooms = PersonalChatRoom.objects.filter(user=request.user)
    chat_users = User.objects.exclude(id=request.user.id)
    return render(request, 'rooms.html', {'rooms': rooms,  'chat_users': chat_users})

def room(request,slug):
    room_name=Room.objects.get(slug=slug).name
    messages=Message.objects.filter(room=Room.objects.get(slug=slug))
    
    return render(request, "room.html",{"room_name":room_name,"slug":slug,'messages':messages})
    
def create_personal_chat(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    room_name = f"{min(request.user.username, other_user.username)}_{max(request.user.username, other_user.username)}"

    existing_room = PersonalChatRoom.objects.filter(name=room_name).first()
    if existing_room:
        return redirect('personal_chat', room_slug=existing_room.name)

    new_room = PersonalChatRoom.objects.create(name=room_name)
    return redirect('personal_chat', room_slug=new_room.name)

@login_required
def personal_chat(request, room_slug):
    room = get_object_or_404(PersonalChatRoom, name=room_slug)
    messages = PersonalChatMessage.objects.filter(room=room)
    return render(request, 'personal_chat.html', {'room': room, 'messages': messages})
    