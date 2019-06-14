# Django
from django.urls import path
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView,
    PasswordChangeView, PasswordChangeDoneView
)
from django.contrib.auth import views as auth_views

# Local
from edms.views import *

app_name = 'edms'

urlpatterns = [
    # Lesson Links
    path('lessons', LessonListView.as_view(), name='lesson-list'),
    # path('complete/', complete, name='complete'),
    path('lessons/<int:pk>', LessonDetailView.as_view(), name='lesson-detail'),
    path(
        'lessons/<int:pk>/update',
        LessonUpdateView.as_view(),
        name='lesson-update'
    ),
    
    # Exam Links
    path('exam/<int:pk>/update', ExamUpdateView.as_view(), name='exam-update'),

    # Other Document Links
    path(
        'other_document/<int:pk>/update',
        OtherDocumentUpdateView.as_view(),
        name='other-document-update'
    ),

    # Requsted Document Links
    path(
        'requsted_documents/<int:pk>/update',
        RequstedDocumentsUpdateView.as_view(),
        name='requsted-update'
    ),
    # User İnteraction
    path('login/', LoginView.as_view(), {
        'template_name': 'registration/login.html'},
        name='login'
    ),
    path('logout/', LogoutView.as_view(), {
        'template_name': 'registration/logout.html'},
        name='logout'
    ),
    path(
        'password_change/',
        PasswordChangeView.as_view(),
        name='password_change'
    ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(),
        name='password_change_done'
    ),
]