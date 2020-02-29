from rest_framework.serializers import ModelSerializer
from players.models import Player


class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'achievements')
