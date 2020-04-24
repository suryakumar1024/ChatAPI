from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from storyboard.models import Bot, Scenes
from storyboard.serializers import BotSerializer, ScenesSerializer
# Create your views here.


class BotView(ModelViewSet):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer


class ScenesView(ModelViewSet):
    queryset = Scenes.objects.all()
    serializer_class = ScenesSerializer
