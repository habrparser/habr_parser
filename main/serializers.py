from distutils.command.upload import upload
from turtle import update
from rest_framework import serializers

class ParsingSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=500)
    themes = serializers.CharField(max_length=1000)
    image = serializers.CharField()
    text = serializers.CharField()
    created_at = serializers.CharField()
    author = serializers.CharField()