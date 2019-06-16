# Django
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Local
from edms.models import Lesson, Exam, Other_Document, Requested_Documents
from users.models import User
from .forms import LessonForm


class LessonListView(ListView):
    model = Lesson
    template_name = 'edms/lesson/list.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            lessons = Lesson.objects.filter(
                Q(lesson_name_icontains=query) |
                Q(user__first_name__icontains=query) 
            ).distinct()
        
        paginator = Paginator(lessons, 2)
        page = self.request.GET.get('page')
        try:
            lessons = paginator.page(page)
        except PageNotAnInteger:
            lessons = paginator.page(1)
        except EmptyPage:
            lessons = paginator.page(paginator.num_pages)
        return render(self.request, 'edms/lesson/list.html', {'lessons' : lessons})

    def get(self, request):
        user = request.user
        if user.is_department_manager:
            documnets = Requested_Documents.objects.filter(
                lesson__user=user
            ).order_by("lesson")

            lessons = {}
            for lesson in Lesson.objects.all():
                lesson_id = str(lesson.id)
                lessons[lesson_id] = {
                        'lesson': lesson,
                        'docs': []
                    }

            for doc in documnets:
                lesson_id = str(doc.lesson.id)
                lessons[lesson_id]['docs'].append(doc)
            return render(request, self.template_name, {
                'lessons': lessons,
            })
        elif user.is_assistant_department_manager:
            documnets = Requested_Documents.objects.filter(
                lesson__user=user
            ).order_by("lesson")

            lessons = {}
            for lesson in Lesson.objects.all():
                lesson_id = str(lesson.id)
                lessons[lesson_id] = {
                        'lesson': lesson,
                        'docs': []
                    }

            for doc in documnets:
                lesson_id = str(doc.lesson.id)
                lessons[lesson_id]['docs'].append(doc)

            return render(request, self.template_name, {
                'lessons': lessons,
            })
        elif user.is_dean_manager:
            documnets = Requested_Documents.objects.filter(
                lesson__user=user
            ).order_by("lesson")

            lessons = {}
            for lesson in Lesson.objects.all():
                lesson_id = str(lesson.id)
                lessons[lesson_id] = {
                        'lesson': lesson,
                        'docs': []
                    }

            for doc in documnets:
                lesson_id = str(doc.lesson.id)
                lessons[lesson_id]['docs'].append(doc)

            return render(request, self.template_name, {
                'lessons': lessons,
            })
        elif user.is_academician:
            documnets = Requested_Documents.objects.filter(
                lesson__user=user
            ).order_by("lesson")

            lessons = {}
            for lesson in Lesson.objects.filter(user=user):
                lesson_id = str(lesson.id)
                lessons[lesson_id] = {
                        'lesson': lesson,
                        'docs': []
                    }

            for doc in documnets:
                lesson_id = str(doc.lesson.id)
                lessons[lesson_id]['docs'].append(doc)

            return render(request, self.template_name, {
                'lessons': lessons,
            })
        else:
            return redirect(reverse('edms:home'))


class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'edms/lesson/detail.html'


class LessonUpdateView(UpdateView):
    model = Lesson
    template_name = 'edms/lesson/update.html'
    fields = [
        'lesson_content', 'lesson_content_file',
        'lesson_notes', 'lesson_notes_file'
    ]
    success_url = "/lessons"


class ExamUpdateView(UpdateView):
    model = Exam
    template_name = 'edms/exam/update.html'
    fields = ['exam_type', 'exam_information', 'exam_file', 'exam_answer_file']
    success_url = "/lessons"


class OtherDocumentUpdateView(UpdateView):
    model = Other_Document
    template_name = 'edms/other/update.html'
    fields = [
        'course_evaluation_form', 'course_survey', 'exam_note_list_midterm',
        'exam_note_list_end_of_term', 'exam_note_list_Integrated'
    ]
    success_url = "/lessons"


class RequstedDocumentsUpdateView(UpdateView):
    model = Requested_Documents
    template_name = 'edms/requested/update.html'
    fields = ['d_bool', ]
    success_url = "/lessons"
