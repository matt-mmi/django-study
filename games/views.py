from django.shortcuts import render
from rest_framework import viewsets

from games.models import Game
from games.serializers import GameSerializer


class GameView(viewsets.ViewSet):
    def list(self, request):
        queryset = Game.objects.all()


# Create your views here.
