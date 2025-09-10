from rest_framework import generics

from apps.team.models import TeamMember
from apps.team.serializers import TeamMemberSerializer


class TeamMembersViewList(generics.ListAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class TeamMembersSlugView(generics.RetrieveAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    lookup_field = "slug"