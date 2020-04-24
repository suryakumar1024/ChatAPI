from storyboard.models import Bot, Scenes
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class BotSerializer(ModelSerializer):

    class Meta:
        model = Bot
        fields = ['name', 'language']


class ScenesSerializer(ModelSerializer):

    class Meta:
        model = Scenes
        fields = ['name', 'description', 'status']

# class IntentSerializer(serializers.Serializer):
#