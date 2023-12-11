from django.shortcuts import render


def room(request, room_name):
    """
    Представление для тестирования работы веб-сокета.
    Для этого был создан шаблон чат-комнаты.
    """
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

