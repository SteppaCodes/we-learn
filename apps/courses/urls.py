from django.urls import path
from .views import (HomeView, ManageCourseListView, 
                    CourseUpdateView, CourseCreateView,
                    CourseDeleteView
                    )

urlpatterns= [
    path('', HomeView.as_view(), name='home' ),
    path('mycourses/', ManageCourseListView.as_view(), name='mycourses'),
    path('create-course/', CourseCreateView.as_view(), name='create-course' ), 
]