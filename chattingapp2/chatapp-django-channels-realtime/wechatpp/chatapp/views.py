from django.shortcuts import render,redirect, get_object_or_404
from .models import Room,Message,PersonalChat, PersonalChatRoom
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from .forms import PersonalChatForm

def rooms(request):
    rooms=Room.objects.all()
    personal_rooms = PersonalChatRoom.objects.filter(members=request.user)
    chat_users = User.objects.exclude(id=request.user.id)
    return render(request, 'rooms.html', {'rooms': rooms, 'personal_rooms': personal_rooms, 'chat_users': chat_users})

def room(request,slug):
    room_name=Room.objects.get(slug=slug).name
    messages=Message.objects.filter(room=Room.objects.get(slug=slug))
    
    return render(request, "room.html",{"room_name":room_name,"slug":slug,'messages':messages})

def create_personal_chat(request, user_id):
    user_to_chat = get_object_or_404(User, id=user_id)
    personal_room, created = PersonalChatRoom.objects.get_or_create(name=f"{request.user.username}_{user_to_chat.username}")
    personal_room.members.add(request.user, user_to_chat)

    if request.method == 'POST':
        form = PersonalChatForm(request.POST)
        if form.is_valid():
            message_text = form.cleaned_data['message']
            PersonalChat.objects.create(room=personal_room, user=request.user, message=message_text)
            return redirect('personal_chat_room', room_id=personal_room.id)
    else:
        form = PersonalChatForm()

    return render(request, 'create_personal_chat.html', {'form': form, 'personal_room': personal_room})

@login_required
def personal_chat_room(request, room_id):
    room = get_object_or_404(PersonalChatRoom, id=room_id)

    if request.user not in room.members.all():
        # Redirect to home if the user is not a member of the personal chat room
        return redirect('rooms')

    messages = PersonalChat.objects.filter(room=room)

    return render(request, 'personal_chat_room.html', {'room': room, 'messages': messages})