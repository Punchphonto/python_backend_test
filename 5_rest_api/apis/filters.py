import django_filters
from .models import *

# code here
class ClassRoomFilter(django_filters.FilterSet):
    school_id = django_filters.NumberFilter(field_name='school__id')
    school_name = django_filters.CharFilter(field_name='school__name')

    class Meta:
        model = ClassRoom
        fields = ['school_id', 'school_name']


class TeacherFilter(django_filters.FilterSet):
    school_id = django_filters.NumberFilter(field_name='school__id')
    school_name = django_filters.CharFilter(field_name='school__name')
    classroom_id = django_filters.NumberFilter(field_name='teacherclassroom__classroom__id')
    first_name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    last_name = django_filters.CharFilter(field_name='family_name', lookup_expr='icontains')
    gender = django_filters.CharFilter(field_name='gender__name', lookup_expr='iexact')

    class Meta:
        model = Teacher
        fields = ['school_id', 'school_name', 'classroom_id', 'first_name', 'last_name', 'gender']


class StudentFilter(django_filters.FilterSet):
    school_id = django_filters.NumberFilter(field_name='school__id')
    school_name = django_filters.CharFilter(field_name='school__name')
    classroom_id = django_filters.NumberFilter(field_name='class_room__id')
    first_name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    last_name = django_filters.CharFilter(field_name='family_name', lookup_expr='icontains')
    gender = django_filters.CharFilter(field_name='gender__name', lookup_expr='iexact')

    class Meta:
        model = Student
        fields = ['school_id', 'school_name', 'classroom_id', 'first_name', 'last_name', 'gender']