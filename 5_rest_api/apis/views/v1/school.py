from ...models import *
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from ...serializers import *
from rest_framework import generics
from django_filters import rest_framework as filters
from ...filters import *
from django_filters.rest_framework import DjangoFilterBackend

@permission_classes([AllowAny])
class SchoolCreateView(generics.CreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class SchoolFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = School
        fields = ['name']

@permission_classes([AllowAny])
class SchoolListView(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = SchoolFilter

@permission_classes([AllowAny])
class SchoolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolDetailSerializer

@permission_classes([AllowAny])
class ClasRoomCreateView(generics.CreateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer

@permission_classes([AllowAny])
class ClassRoomListView(generics.ListAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClassRoomFilter

@permission_classes([AllowAny])
class ClassRoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomDetailSerializer