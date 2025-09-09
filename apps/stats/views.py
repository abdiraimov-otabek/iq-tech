from rest_framework import generics

from apps.stats.models import Statistics
from apps.stats.serializers import StatisticsSerializer


class StatisticViewList(generics.ListAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer