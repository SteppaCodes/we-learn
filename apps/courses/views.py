from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import (ListView, CreateView,
                                   UpdateView, DeleteView)
from django.views.generic.base import TemplateResponseMixin
from .models import Course, Subject

from .mixins import OwnerCourseMixin, OwnerCourseEditMixin
from .forms import ModelForm

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


class CourseModuleUpdateVIew(TemplateResponseMixin, View):
    template_name = 'courses/modules/formset.html'
    course=None

    def get_formset(self,data=None):
        return ModelForm(instance=self.course, data=data)
    
    def dispatch(self, request, pk) :
        self.course = get_object_or_404(Course, id=pk, owner=request.user)
        return super().dispatch(request, pk)

    def get(self, request, *args, **Kwargs):
        formset = self.get_formset()
        return self.render_to_response({
            'formset':formset,
            'course': self.course
        })

    def post(self, request, *args, **Kwargs):
        formset = self.get_formset(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('mycourses')
        return self.render_to_response({
            'course':self.course,
            'formset':formset
        })
        
