from django.urls import path
from .views import SubjectListApiView, SubjectDetailApiView, CourseListView, CourseEnrollView

app_name = 'courses'

urlpatterns = [
    path('subjects/', SubjectListApiView.as_view(), name='subject_list'),
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('subjects/<int:pk>/', SubjectDetailApiView.as_view(), name='subject_detail'),
    path('courses/<pk>/enroll/', CourseEnrollView.as_view(), name='course_enroll')
]
