from rest_framework import viewsets

from apps.team.models import TeamMember
from apps.team.serializers import TeamMemberSerializer


class TeamMembersViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
