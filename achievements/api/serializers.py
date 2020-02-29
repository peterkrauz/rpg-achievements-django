from rest_framework.serializers import ModelSerializer
from achievements.models import Achievement


class AchievementSerializer(ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('id', 'title', 'description')
