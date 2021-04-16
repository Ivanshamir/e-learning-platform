from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


# Create your views here.
@login_required
def course_chat_room(request, course_id):
    try:
        course = request.user.courses_joined.get(id=course_id)
    except:
        # user is not a student of the course or course does not exist
        return HttpResponseForbidden()
    return render(request, 'chat/room.html', {'course': course})
