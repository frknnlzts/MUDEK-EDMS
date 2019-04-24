# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
import datetime
from django.utils import timezone


def set_user_files_upload_path(instance, filename):
    return '/'.join([
        'users', 'files', filename
    ])


class Lesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson_name = models.CharField(verbose_name=_('Ders Adı'), max_length=150)
    lesson_content = models.TextField(verbose_name=_('Ders İçeriği'), blank=True)
    lesson_content_file = models.FileField(
        verbose_name=_('Ders İçeriği Dosya'),
        upload_to=set_user_files_upload_path, blank=True, null=True
    )
    lesson_notes = models.TextField(verbose_name=_('Ders Notu'), blank=True)
    lesson_notes_file = models.FileField(
        verbose_name=_('Ders Notu Dosya'),
        upload_to=set_user_files_upload_path,
        blank=True, null=True
    )

    def __str__(self):
        return '{lesson_name}'.format(
            lesson_name=self.lesson_name
        )

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lesson'


class Exam(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    exam_type = models.CharField(verbose_name=_('Sınav Türü'), max_length=50)
    exam_information = models.TextField(
        verbose_name=_('Sınav Hakkında Bilgi'), max_length=500)
    exam_file = models.FileField(
        verbose_name=_('Sınav Kağıdı Dosya'),
        upload_to=set_user_files_upload_path, blank=True, null=True
    )
    exam_answer_file = models.FileField(
        verbose_name=_('Cevap Anahtarı Dosya'),
        upload_to=set_user_files_upload_path, blank=True, null=True
    )

    def __str__(self):
        return '{lesson} - {exam_type}'.format(
            lesson=self.lesson.lesson_name,
            exam_type=self.exam_type
        )

    class Meta:
        verbose_name = 'Exam'
        verbose_name_plural = 'Exam'


class Other_Document(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    course_evaluation_form = models.FileField(
        verbose_name=_('Ders Değerlendirme Formu'),
        upload_to=set_user_files_upload_path
    )
    course_survey = models.FileField(verbose_name=_('Ders Anketi'))
    exam_note_list_midterm = models.FileField(
        verbose_name=_('Arasınav Sınav Not Listesi'),
        upload_to=set_user_files_upload_path,
        blank=True, null=True
    )
    exam_note_list_end_of_term = models.FileField(
        verbose_name=_('Dönem Sonu Sınav Not Listesi'),
        upload_to=set_user_files_upload_path,
        blank=True, null=True
    )
    exam_note_list_Integrated = models.FileField(
        verbose_name=_('Bütünleme Sınav Not Listesi'),
        upload_to=set_user_files_upload_path,
        blank=True, null=True
    )

    def __str__(self):
        return '{lesson}'.format(
            lesson=self.lesson.lesson_name
        )

    class Meta:
        verbose_name = 'Other Document'
        verbose_name_plural = 'Other Document'

class Requested_Documents(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    d_name = models.CharField(verbose_name=_('İstenilen Belge Adı'), max_length=100)
    d_bool = models.BooleanField(verbose_name=_('İstenilen Belge Yüklü mü ?'), default=False)

    def __str__(self):
        return '{lesson}'.format(
            lesson=self.lesson.lesson_name
        )

    class Meta:
        verbose_name = 'Requested Documents'
        verbose_name_plural = 'Requested Documents'