from django.shortcuts import render
from rest_framework import generics, status
from .models import Column, Row, Task, Limit, User, TaskUser
from .serializers import ColumnSerializer, RowSerializer, TaskSerializer, LimitSerializer, \
    TaskUserSerializer, RegisterSerializer, UserSerializer
from django.http import HttpResponse


class ColumnView(generics.ListCreateAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    name = 'Column-list'


class RowView(generics.ListCreateAPIView):
    queryset = Row.objects.all()
    serializer_class = RowSerializer
    name = 'Row-list'


class TaskView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    name = 'Task-list'


class LimitView(generics.ListCreateAPIView):
    queryset = Limit.objects.all()
    serializer_class = LimitSerializer
    name = 'Limit-list'


class ColumnDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    name = 'Column-detail'


class RowDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Row.objects.all()
    serializer_class = RowSerializer
    name = 'Row-detail'


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    name = 'Task-detail'


class LimitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Limit.objects.all()
    serializer_class = LimitSerializer
    name = 'Limit-detail'


class TaskUserView(generics.ListCreateAPIView):
    queryset = TaskUser.objects.all()
    serializer_class = TaskUserSerializer
    name = 'TaskUser-list'


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    name = 'register-user'


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class TaskUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskUser.objects.all()
    serializer_class = TaskUserSerializer
    name = 'TaskUser-detail'


'''
class GroupTaskView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupTaskSerializer
'''
