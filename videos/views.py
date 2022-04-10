from multiprocessing import context
from django.shortcuts import redirect, render
import os
from videos.models import Video

from media_organizer.config import readConfig
# Create your views here.
def index(request):
    return render(request,template_name="videos/index.html")

def settings(request):
    if request.method == "POST":
        if request.POST["video-path"]:
            for path in request.POST["video-path"].split(","):
                for (dirpath, dirnames, filenames) in os.walk(path):
                    for file in filenames:
                        if file.endswith('.mp4'):
                            print(os.path.join(dirpath, file))
                            print(file)
            return redirect("settings")
            context = {
                "settings": readConfig()
            }
        
    return render(request, template_name="videos/settings.html", context=context)