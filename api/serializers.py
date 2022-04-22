from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Column, Row, Task, Limit, User, TaskUser


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ['id', 'name', 'position', 'limit']


class RowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Row
        fields = ['id', 'name', 'position', 'limit']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'position', 'color', 'column', 'row']


class LimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Limit
        fields = ['id', 'limit', 'column', 'row']


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        required=True,
    )
    password2 = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
        )

        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class TaskUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskUser
        fields = ['id', 'task', 'user']


'''
class GroupTaskSerializer(serializers.ModelSerializer):
    task_set = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = ['id', 'name', 'limit', 'position', 'task_set']
'''
