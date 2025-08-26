from .models import Message

def mensajes_no_leidos(request):
    if request.user.is_authenticated:
        count = Message.objects.filter(recipient=request.user, read=False).count()
        return {'mensajes_no_leidos': count}
    return {}