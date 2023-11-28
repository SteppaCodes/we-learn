from django.shortcuts import render
from django.views import View
from .models import Course, Subject

#TODO: cREATA A COURSE OBJECTIVES THAT STUDENTS WILL TICK IF THEY ARE ABLE TO MEET THE OBJECTIVES

class HomeView(View):
    def get(self,request):
        courses = Course.objects.all()
        subjects= Subject.objects.all()
        context = {
            "courses":courses,
            "subjects":subjects,
        }

        return render(request, 'courses/home.html', context)