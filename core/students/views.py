from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CourseEnrollForm


# Create your views here.


class StudentRegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'students/student/registration.html'
    success_url = reverse_lazy('student_course_list')

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password1'])
        login(self.request, user)
        return result


class StudentEnrollCourseView(LoginRequiredMixin,
                              FormView):
    course = None
    form_class = CourseEnrollForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('student_course_detail',
                            args=[self.course.id])


