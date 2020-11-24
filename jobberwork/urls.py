from django.urls import path
from .views import *

urlpatterns = [
    path('task/new/', NewTaskView.as_view()),
    path('task/all/', AllTaskView.as_view()),
    path('task/all/me/', UserAllTaskView.as_view()),
    path('task/me/<int:id>/', UserIndividualTaskView.as_view()),
    path('task/<int:id>/', IndividualTaskView.as_view()),
    path('task/edit/<int:id>/', UserEditIndividualTaskView.as_view()),
    path('task/accept/', AcceptedTaskView.as_view()),
    path('task/accept/view/', AcceptedViewTaskView.as_view()),

]