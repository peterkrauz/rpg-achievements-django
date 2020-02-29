from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rpgs.models import Rpg
from rpgs.api.serializers import RpgSerializer
from achievements.models import Achievement
from achievements.api.serializers import AchievementSerializer


class RpgViewSet(ModelViewSet):
    queryset = Rpg.objects.all()
    serializer_class = RpgSerializer

    @action(detail=True)
    def achievements(self, request, pk=None):
        achievements = Achievement.objects.filter(rpg_id=pk)

        context = {
            'request': request
        }

        achievement_serializer = AchievementSerializer(achievements, many=True, context=context)
        return Response(achievement_serializer.data)
