from django.shortcuts import render
from .models import Course
# Create your views here.

def homeView(request):

    all_courses = Course.objects.filter(category__category='Web Development').order_by('-d_price')
    context = {
        'web_development': all_courses
    }
    return render(request, 'core/index.html', context)