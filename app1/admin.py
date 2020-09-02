from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from .models import User, Student, Teacher


# Register your models here.

class BaseUserAdmin(UserAdmin):
    list_display = ['email', 'is_admin', ]
    search_fields = ("email", 'sap_id', 'is_admin', )
    readonly_fields = (
        'date_joined',
        'last_login',
    )

    filter_horizontal =()
    list_filter = ()
    fieldsets = ()

class StudentAdmin(UserAdmin):
    list_display = ('email','sap_id', 'year')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class TeacherAdmin(UserAdmin):
    list_display = ('email', 'qualification', )
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class StudentDisplayAdmin(UserAdmin):
    list_display = ['email', 'sap_id', ]
    ordering = ['email']
    search_fields = ['email']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.unregister(Group)
admin.site.register(User, BaseUserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
