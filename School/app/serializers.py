from rest_framework import serializers

from .models import Teacher, Class, Student, User, Admin

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'role']
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['role']

class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Admin
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        user = User.objects.create_user(**user_data, role='admin')
        user.set_password(password)
        user.save()

        admin = Admin.objects.create(user=user, **validated_data)
        return admin

    def update(self, instance, validated_data):
        user = instance.user
        user_data = validated_data.pop('user', {})
        for attr, value in user_data.items():
            if attr == 'password':
                user.set_password(value)
            else:
                setattr(user, attr, value)
        user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = '__all__'
        read_only_fields = ["class_id"]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        user = User.objects.create_user(**user_data, role='teacher')
        user.set_password(password)
        user.save()

        teacher = Teacher.objects.create(user=user, **validated_data)
        return teacher

    def update(self, instance, validated_data):
        user = instance.user
        user_data = validated_data.pop('user', {})
        for attr, value in user_data.items():
            if attr == 'password':
                user.set_password(value)
            else:
                setattr(user, attr, value)
        user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ["class_id"]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        user = User.objects.create_user(**user_data, role='student')
        user.set_password(password)
        user.save()

        student = Student.objects.create(user=user, **validated_data)
        return student

    def update(self, instance, validated_data):
        user = instance.user
        user_data = validated_data.pop('user', {})
        for attr, value in user_data.items():
            if attr == 'password':
                user.set_password(value)
            else:
                setattr(user, attr, value)
        user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance



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



