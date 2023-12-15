from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import (ListView, CreateView,
                                   UpdateView, DeleteView, DetailView)
from django.apps import apps
from django.forms.models import modelform_factory
from django.views.generic.base import TemplateResponseMixin
from .models import Course, Subject, Module, Content

from .mixins import OwnerCourseMixin, OwnerCourseEditMixin
from .forms import ModelForm

from braces.views import CsrfExemptMixin, JSONRequestResponseMixin

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
   template_name = 'courses/manage/course/mycourses.html'
   permission_required = 'course.view_course'


class CourseCreateView(OwnerCourseEditMixin, CreateView):
    permission_required = 'courses.add_course'


class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    permission_required= 'courses.change_course'


class CourseDeleteView(OwnerCourseMixin, DeleteView):
    template_name = 'courses/delete.html'
    permission_required= 'courses.delete_course'


class CourseModuleDetailView(TemplateResponseMixin, View):
    template_name='courses/manage/course/course_page.html'
    
    def get(self, request, pk):
        course = Course.objects.prefetch_related('modules').get(id=pk)

        return self.render_to_response({
            'course':course,

        })


class ModuleDetailView(TemplateResponseMixin, View):
    template_name='courses/manage/course/course_page.html'

    def get(self, request, pk ,module_id):
        course = Course.objects.get(id=pk)
        module = get_object_or_404(Module, id=module_id)

        return self.render_to_response({
            'course':course,
            "module":module

        })


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
        

class ContentCreateUpdateVIew(TemplateResponseMixin, View):
    model =None
    module = None
    obj = None
    template_name = 'courses/manage/content/form.html'

    def get_model(self, model_name):
        if model_name in ['text', 'image', 'file', 'video']:
            return apps.get_model(app_label='courses', model_name=model_name)
        return None
    
    def get_form(self, model , *args, **Kwargs):
        form = modelform_factory(model, exclude=[
            'owner',
            'created',
            'updated',
            'order',
        ])
        return form(*args, **Kwargs)
    
    def dispatch(self, request , model_name, module_id, id=None):
        self.module = get_object_or_404(Module, id=module_id, course__owner=request.user)
        self.model = self.get_model(model_name)
        if id:
            self.obj = get_object_or_404(self.model, id=id, owner=request.user)

        return super().dispatch(request, module_id, model_name, id)
    
    def get(self, request,  model_name, module_name,id=None):
        form = self.get_form(self.model, instance= self.obj)
        return self.render_to_response({
            'form':form,
            'object':self.obj
        })
    
    def post(self, request, model_name, module_name, id=None):
        form = self.get_form(
            self.model,
            instance = self.obj,
            data =request.POST,
            files=request.FILES
        )

        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()

            if not id:
                Content.objects.create(module=self.module, item=obj, owner=request.user)
                return redirect('module_content_list', self.module.id)
            return self.render_to_response({
                "form":form,
                "object": self.obj
            })

class ModuleOrderView(CsrfExemptMixin, JSONRequestResponseMixin, View):
    def post(self, request):
         for id, order in self.request_json.items():
             Module.objects.filter(id=id, course__owner=request.user).update(order=order)
             return self.render_json_response({'saved':"ok"})