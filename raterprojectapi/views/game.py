"""View module for handling requests about games"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models import Game, Player, Category

class GameView(ViewSet):
    """Level up games view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game
        """
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game)
            return Response(serializer.data)
        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    def list (self, request):
        """Handle GET requests to get all games

        Returns:
            Response -- JSON serialized list of games
        """
        games = Game.objects.all()

        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized game instance
        """
        player = Player.objects.get(user=request.auth.user)

        game = Game.objects.create(
            title=request.data["title"],
            designer=request.data["designer"],
            year_released=request.data["year_released"],
            number_of_players=request.data["number_of_players"],
            estimated_time_to_play=request.data["estimated_time_to_play"],
            age_recommendation=request.data["age_recommendation"],
            player=player
        )

        game.game_categories.add(request.data["categories"])
        serializer = GameSerializer(game)
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
                'number_of_players',
                'estimated_time_to_play',
                'age_recommendation',
                'player')
        depth = 1
        