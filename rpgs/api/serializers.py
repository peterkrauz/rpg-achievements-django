from rest_framework.serializers import ModelSerializer
from rpgs.models import Rpg


class RpgSerializer(ModelSerializer):
    class Meta:
        model = Rpg
        fields = ('id', 'title', 'description', 'created_at')
