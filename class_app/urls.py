from django.urls import path
from . import views


urlpatterns = [
    path('list',views.TaskListView.as_view(),name='list'),
    path('',views.TaskCreateView.as_view(),name='create'),
    path('detail/<int:pk>',views.TaskDetailView.as_view(),name='detail'),
    path('update/<int:pk>',views.TaskUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',views.TaskDeleteView.as_view(),name='delete')
]