from django.contrib import admin
from django.utils.html import mark_safe

from courses.models import Course, Category
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Course
        fields = '__all__'
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'created_date', 'updated_date','active']
    search_fields = ['id','name']
    list_filter = ['created_date','name']
    readonly_fields = ['my_image']
    form = CourseForm

    def my_image(self, course):
        if course.image:
            return mark_safe(f"<img src='{course.image.url}'  width='200px' />")

admin.site.register(Category)
admin.site.register(Course,CourseAdmin)