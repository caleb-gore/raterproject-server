"""View module for handling requests about reviews"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models import Review, Player, Game

class ReviewView(ViewSet):
    """Level up review view"""
    
    def list (self, request):
        """Handle GET requests to get all reviews

        Returns:
            Response -- JSON serialized list of reviews
        """
        reviews = Review.objects.all()

        game = request.query_params.get('game', None)
        if game is not None:
            
            reviews = reviews.filter(game_id=game)

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    
    def create(self, request):
        """Handle POST operations
        
        Returns
            Response -- JSON serialized event instance
        """
        player = Player.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data["game"])
        
        review = Review.objects.create(
            game = game,
            player = player,
            review = request.data["review"]
        )
        
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

class ReviewSerializer(serializers.ModelSerializer):
        """JSON serializer for reviews
        """

        class Meta:
            model = Review
            fields = ('id','game','player','review')
            depth = 1