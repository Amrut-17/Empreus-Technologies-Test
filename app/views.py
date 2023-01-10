from django.shortcuts import render, redirect
from .models import Event
from datetime import timedelta
# Create your views here.


def homepage(request):
    events = Event.objects.all().order_by("-id")
    for event in events:
        hr = event.duration.seconds//3600
        mn = (event.duration.seconds//60) % 60
        event.duration = {"hours": hr, "minutes": mn}
    return render(request, 'app/index.html', {'events': events})


def create(request):
    return render(request, 'app/addEvent.html')


def add_event(request):
    if request.method == "POST" and request.FILES['personPhoto']:
        title = request.POST['title']
        speaker_name = request.POST['personName']
        speakers_avatar = request.FILES['personPhoto']
        date_select = request.POST['dateSelect']
        duration = request.POST['duration'].split(":")
        start_time = request.POST['startTime']
        end_time = request.POST['endTime']
        time_duration = timedelta(hours=float(duration[0]), minutes=float(duration[1]))

        event = Event(
            title=title,
            speaker_name=speaker_name,
            speakers_avatar=speakers_avatar,
            date_select=date_select,
            duration=time_duration,
            start_time=start_time,
            end_time=end_time,
        )

        event.save()
        return redirect('home')
    else:
        return redirect('create')
