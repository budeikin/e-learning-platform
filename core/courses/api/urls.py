from django.urls import path, include
from rest_framework import routers
from .views import SubjectListApiView, SubjectDetailApiView, CourseViewSet

router = routers.DefaultRouter()
router.register('courses', CourseViewSet)

app_name = 'courses'

urlpatterns = [
    path('subjects/', SubjectListApiView.as_view(), name='subject_list'),
    path('subjects/<int:pk>/', SubjectDetailApiView.as_view(), name='subject_detail'),
    path('', include(router.urls))

]
