from . models import Course
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.urls import reverse_lazy


#Get courses owned by current user
class OwnerMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


#Set owne of course to current user when creating course    
class OwnerEditMixin:
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


 #Return all th courses owned by the logged in user   
class OwnerCourseMixin(OwnerMixin):
    model = Course 
    fields = [ 'subject' ,'title','overview' ]
    success_url= reverse_lazy('mycourses')


class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin, LoginRequiredMixin, PermissionRequiredMixin):
    template_name = 'courses/manage/course/form.html'


