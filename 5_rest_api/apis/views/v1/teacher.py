from rest_framework import generics
from ...models import Teacher
from ...serializers import TeacherSerializer, TeacherDetailSerializer
from ...filters import TeacherFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

@permission_classes([AllowAny])
class TeacherListView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TeacherFilter

@permission_classes([AllowAny])
class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherDetailSerializer

@permission_classes([AllowAny])
class TeacherCreateView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer