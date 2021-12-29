from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import  DetailView
from django.views.generic.edit import UpdateView, DeleteView

from .forms import Tudoforms
from .models import Task, Tim
# Create your views here.
#
# def home(request):
#
#     return render(request,'home.html')
#



def result(request):
    obj1=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        obj=Task(name=name,priority=priority,date=date)
        obj.save()
    return render(request,'index.html',{"obj1":obj1})

class Taskviewe(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'obj1'
class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'

class Taskupdate(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')
    def get_success_url(self):
        return reverse_lazy('TaskDetailView',kwargs={ 'pk':self.object.id})
class Taskdelete(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('listview')


def delete(request,taskid):
    obj=Task.objects.get(id=taskid)
    if request.method=='POST':
        obj.delete()
        return redirect('/')
    return render(request,'delete.html',{'obj':obj})

def update(request,taskid):
    task=Task.objects.get(id=taskid)
    forms=Tudoforms(request.POST or None,instance=task)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'forms':forms})




def time(request):
    if request.method=='POST':
        days=request.POST.get('days')
        temp=days
        years=days//365
        days=days%365
        month=days//30
        day=days%30
        week=days//7
        days=days%7
        hr=(temp*24)
        mt=hr*60
        sec=mt*60
        # print("years : ",years)

        # print("month : ",month)
        # print("week : ",week)
        # print("days : ",days)
        # print("totel hr : ",hr)
        # print("totel minut : ",mt)
        # print("totel sec : ",sec)
       


    # return render(request,'time.html',{"obj2":obj2})
    return HttpResponse(request,'time.html',{years,month,day,week})