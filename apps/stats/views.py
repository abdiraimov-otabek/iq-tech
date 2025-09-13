from rest_framework import generics

from apps.stats.models import Statistics, Reviews
from apps.stats.serializers import StatisticsSerializer, ReviewSerializer


class StatisticViewList(generics.ListAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer

class ReviewViewList(generics.ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer