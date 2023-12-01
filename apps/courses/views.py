from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Course, Subject

from .mixins import OwnerCourseMixin, OwnerEditMixin, OwnerCourseEditMixin

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
    
class ManageCourseListView(OwnerCourseMixin, ListView):
   template_name = 'courses/mycourses.html'
   permission_required = 'course.view_course'


class CourseCreateView(OwnerCourseEditMixin, CreateView):
    permission_required = 'courses.add_course'


class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    permission_required= 'courses.change_course'


class CourseDeleteView(OwnerCourseMixin, DeleteView):
    template_name = 'courses/delete.html'
    permission_required= 'courses.delete_course'

class CourseDetailView():
    pass
