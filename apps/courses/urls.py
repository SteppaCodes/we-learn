from django.urls import path
from .views import (HomeView, ManageCourseListView, 
                    CourseUpdateView, CourseCreateView,
                    CourseModuleUpdateVIew,
                    ContentCreateUpdateVIew, CourseModuleDetailView,
                    ModuleDetailView, ModuleOrderView
                    )

urlpatterns= [
    path('', HomeView.as_view(), name='home' ),
    path('mycourses/', ManageCourseListView.as_view(), name='mycourses'),
    path('create-course/', CourseCreateView.as_view(), name='create-course' ), 
    path('course/<pk>', CourseModuleDetailView.as_view(), name='course-detail' ),

    path('course/<pk>/module/<module_id>/', ModuleDetailView.as_view(), name='module-detail' ),
    path('<pk>/module/', CourseModuleUpdateVIew.as_view(), name='course_module_update'),
    path('module/order/', ModuleOrderView.as_view(), name='module_order'),

    path('module/<module_id>/content/<model_name>/create/', ContentCreateUpdateVIew.as_view(), name= 'content_create_update') 
]