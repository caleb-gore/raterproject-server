"""View module for handling requests about games"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models import Game

class GameView(ViewSet):
    """Level up games view"""

    def list (self, request):
        """Handle GET requests to get all games

        Returns:
            Response -- JSON serialized list of games
        """
        games = Game.objects.all()
        
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
    
class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    """
    class Meta: 
        model = Game
        fields = ('id',
                'title',
                'description',
                'designer',
                'year_released',
                'number of players',
                'estimated_time_to_play',
                'age_recommendation',
                'player')
        depth = 1