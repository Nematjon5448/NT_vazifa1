from rest_framework import serializers

from .models import Teacher, Class, Student

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'
        read_only_fields = ["class_id"]

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ["class_id"]

class ClassSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True)
    students = StudentSerializer(many=True)

    class Meta:
        model = Class
        fields = '__all__'

    def create(self, validated_data):
        teachers = validated_data.pop("teachers")
        students = validated_data.pop("students")
        clas = Class.objects.create(**validated_data)

        for teacher_data in teachers:
            teacher = Teacher.objects.create(**teacher_data)
            teacher.class_id.set([clas])

        for student_data in students:
            Student.objects.create(class_id=clas, **student_data)

        return clas

    def update(self, instance, validated_data):
        teachers_data = validated_data.pop("teachers", None)
        students_data = validated_data.pop("students", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if teachers_data is not None:
            instance.teachers.all().delete()
            for teachers_data in teachers_data:
                teacher = Teacher.objects.create(**teachers_data)
                teacher.class_id.set([instance])

        if students_data is not None:
            instance.students.all().delete()
            for students_data in students_data:
                Student.objects.create(class_id=instance, **students_data)

        return instance



