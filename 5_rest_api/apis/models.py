from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.name

class ClassRoom(models.Model):
    school_year = models.IntegerField( blank=True, null=True)
    room_number = models.IntegerField( blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="class_room")

    def __str__(self):
        return f"{self.school_year}/{self.room_number}"
    
class Gender(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    family_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name="teacher")
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="teacher")
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    family_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name="student")
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name="student")
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="student")
    def __str__(self):
        return self.name

class TeacherClassRoom(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('teacher', 'classroom')

    def __str__(self):
        return f"{self.teacher} {self.classroom}"




