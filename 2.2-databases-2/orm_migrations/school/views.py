from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def show_it(request):
    context = {}
    ordering = 'group'
    context['object_list'] = Student.objects.order_by(ordering).prefetch_related('teacher')
    return render(request, 'main.html', context)
