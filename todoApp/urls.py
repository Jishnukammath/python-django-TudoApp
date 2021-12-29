from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.result,name="result"),
    path('delete/<int:taskid>',views.delete,name="delete"),
    path('update/<int:taskid>', views.update, name="update"),
    path('listview/', views.Taskviewe.as_view(), name="listview"),
    path('TaskDetailView/<int:pk>', views.TaskDetailView.as_view(), name="TaskDetailView"),
    path('Taskupdate/<int:pk>', views.Taskupdate.as_view(), name="Taskupdate"),
    path('Taskdelete/<int:pk>', views.Taskdelete.as_view(), name="Taskdelete"),
    path('time/',views.time,name='time' )
]
