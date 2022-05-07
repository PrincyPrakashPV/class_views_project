from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Task
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

# Create your views here.
class TaskCreateView(CreateView):
    model = Task
    fields = ['name','priority','date']
    template_name = 'add_task.html'
    success_url = reverse_lazy('list')



class TaskListView(ListView):
    model = Task
    template_name = 'task_view.html'
    context_object_name = 'obj'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'ed'
    fields = ['name','priority','date']

    def get_success_url(self):
        return reverse_lazy('detail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('list')