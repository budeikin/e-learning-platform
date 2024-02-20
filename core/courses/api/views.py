from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import SubjectSerializer, CourseSerializer
from courses.models import Subject, Course


class SubjectListApiView(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailApiView(RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CourseListView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
