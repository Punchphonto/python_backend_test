from rest_framework import serializers
from .models import *

# code here
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"


class SchoolDetailSerializer(serializers.ModelSerializer):
    class_room_count = serializers.SerializerMethodField()
    teacher_count = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ['id', 'name', 'code', 'address', 'class_room_count', 'teacher_count', 'student_count']

    def get_class_room_count(self, obj):
        return obj.class_room.count()

    def get_teacher_count(self, obj):
        return obj.teacher.count()

    def get_student_count(self, obj):
        return obj.student.count()


class ClassRoomSerializer(serializers.ModelSerializer):
    school_name = serializers.CharField(source='school.name', read_only=True)

    class Meta:
        model = ClassRoom
        fields = ['id', 'school_year', 'room_number', 'school','school_name']


class TeacherSerializer(serializers.ModelSerializer):
    gender_name = serializers.CharField(source='gender.name', read_only=True)
    school_name = serializers.CharField(source='school.name', read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'family_name', 'gender','gender_name', 'school','school_name']

class StudentSerializer(serializers.ModelSerializer):
    class_room_year_number = serializers.SerializerMethodField()

    def get_class_room_year_number(self, obj):
        class_room = ClassRoom.objects.filter(student=obj).first()
        return "{0}/{1}".format(class_room.school_year, class_room.room_number )

    class Meta:
        model = Student
        fields = ['id', 'name', 'family_name', 'gender', 'class_room', 'school', 'class_room_year_number']

class StudentDetailSerializer(serializers.ModelSerializer):
    class_room_year_number = serializers.SerializerMethodField()

    def get_class_room_year_number(self, obj):
        class_room = ClassRoom.objects.filter(student=obj).first()
        return "{0}/{1}".format(class_room.school_year, class_room.room_number )

    class Meta:
        model = Student
        fields = ['id', 'name', 'family_name', 'gender', 'class_room', 'school','class_room_year_number']


class ClassRoomDetailSerializer(serializers.ModelSerializer):
    teachers = serializers.SerializerMethodField()
    students = serializers.SerializerMethodField()

    class Meta:
        model = ClassRoom
        fields = ['id', 'school_year', 'room_number', 'school', 'teachers', 'students']

    def get_teachers(self, obj):
        teachers = Teacher.objects.filter(teacherclassroom__classroom=obj)
        return TeacherSerializer(teachers, many=True).data

    def get_students(self, obj):
        students = Student.objects.filter(class_room=obj)
        return StudentSerializer(students, many=True).data
    

class TeacherDetailSerializer(serializers.ModelSerializer):
    classrooms = serializers.SerializerMethodField()
    gender = serializers.CharField(source='gender.name', read_only=True)
    school = serializers.CharField(source='school.name', read_only=True)
    school_id = serializers.IntegerField(source='school.pk', read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'family_name', 'gender', 'school','school_id','classrooms']

    def get_classrooms(self, obj):
        classrooms = ClassRoom.objects.filter(teacherclassroom__teacher=obj)
        return ClassRoomSerializer(classrooms, many=True).data

