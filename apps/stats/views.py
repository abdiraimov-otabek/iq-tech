from rest_framework import viewsets

from apps.stats.models import Statistics
from apps.stats.serializers import StatisticsSerializer


class StatisticViewSet(viewsets.ModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer