import json
from pathlib import Path
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
import os
from videos.models import Category, Channel, Star, Subsite, Tag, Video
import sys

sys.path.append("..")

from config import readConfig, saveConfig
# Create your views here.
def index(request):
    return render(request,template_name="videos/index.html")

def videos(request):
    videos = Video.objects.all()
    context = {
        "videos": videos
    }
    return render(request, template_name="videos/videos.html", context=context)

def video(request):
    return render(request, template_name="videos/video.html")

def stars(request):
    stars = Star.objects.all()
    paginator = Paginator(stars, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "stars": stars,
        "page_obj": page_obj
    }
    return render(request, template_name="videos/stars.html", context=context)

def star(request):
    return render(request, template_name="videos/star.html")

def channels(request):
    channels = Channel.objects.all()
    context = {
        "channels":channels
    }
    return render(request, template_name="videos/channels.html", context=context)

def channel(request):
    return render(request, template_name="videos/channel.html")

def categories(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, template_name="videos/categories.html", context=context)

def category(request):
    return render(request, template_name="videos/category.html")

def subsites(request):
    subsites = Subsite.objects.all()
    context = {
        "subsites":subsites
    }
    return render(request, template_name="videos/subsites.html", context=context)

def subsite(request):
    return render(request, template_name="videos/subsite.html")

def tags(request):
    tags = Tag.objects.all()
    context = {
        "tags":tags
    }
    return render(request, template_name="videos/tags.html", context=context)

def tag(request):
    return render(request, template_name="videos/tag.html")

def pending(request):
    return render(request, template_name="videos/pending.html")

def settings(request):
    if request.method == "POST":
        if "video-path" in request.POST:
            


            for path in request.POST["video-path"].split(","):
                if os.path.exists(path):
                    settings = readConfig()
                    if path not in settings["media_path"]:
                        settings["media_path"].append(path)
                    saveConfig(settings)

                for (dirpath, dirnames, filenames) in os.walk(path):
                    for file in filenames:
                        filename = Path(file).stem
                        if not Video.objects.filter(video_name = filename).exists():
                            if file.endswith('.mp4'):
                                video = Video(video_name=filename, video_path = os.path.join(dirpath, file))
                                video.save()
                                print(os.path.join(dirpath, file))
                                print(file)
                        else:
                            print("Already present in database", file)
            return redirect("settings")
    context = {
                "settings": readConfig()
            }
        
    return render(request, template_name="videos/settings.html", context=context)

def save_settings(request):
    if request.accepts('text/json'):
        data = json.loads(request.body.decode('utf-8'))
        settings = readConfig()
        if "1" == data["id"]:
            video_paths = data["settings"]
            for path in video_paths.split(','):
                if os.path.exists(path):
                    
                    if path not in settings["media_path"]:
                        settings["media_path"].append(path)
                        saveConfig(settings)
        elif "2" == data["id"]:
            if os.path.exists(data["settings"]) and data["settings"].split('/')[-1].endswith('.exe'):
                settings["chrome_driver_path"] = data["settings"]
                saveConfig(settings)


    settings = readConfig()
    return JsonResponse(settings)