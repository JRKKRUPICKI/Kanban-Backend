from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('column/', views.ColumnView.as_view(), name=views.ColumnView.name),
    path('column/<int:pk>/', views.ColumnDetailView.as_view(), name=views.ColumnDetailView.name),
    path('row/', views.RowView.as_view(), name=views.RowView.name),
    path('row/<int:pk>/', views.RowDetailView.as_view(), name=views.RowDetailView.name),
    path('task/', views.TaskView.as_view(), name=views.TaskView.name),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name=views.TaskDetailView.name),
    path('limit/', views.LimitView.as_view(), name=views.LimitView.name),
    path('limit/<int:pk>/', views.LimitDetailView.as_view(), name=views.LimitDetailView.name),
    path('taskUser/', views.TaskUserView.as_view(), name=views.TaskUserView.name),
    path('taskUser/<int:pk>/', views.TaskUserDetailView.as_view(), name=views.TaskUserDetailView.name),

    path('user/', views.UserView.as_view(), name=views.UserView.name),
    path('user/<int:pk>/', views.UserDetailsView.as_view(), name=views.UserDetailsView.name),
    path('register/', views.RegisterView.as_view(), name=views.RegisterView.name),
]
