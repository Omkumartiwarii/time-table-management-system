from django.contrib import admin
from .models import Department, Instructor, CourseName, Timetable, Venue


# --------------------
# DEPARTMENT ADMIN
# --------------------
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('DepartmentName', 'HeadOfDepartment', 'RegisteredDate')
    list_filter = ('HeadOfDepartment',)
    search_fields = ('DepartmentName', 'HeadOfDepartment')
    date_hierarchy = 'RegisteredDate'
    list_editable = ('HeadOfDepartment',)
    list_per_page = 10


# --------------------
# INSTRUCTOR ADMIN
# --------------------
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):

    list_display = (
        'username',
        'first_name',
        'last_name',
        'middle_name',
        'email',
        'department',
        'registered_date',
    )

    list_editable = (
        'first_name',
        'last_name',
        'middle_name',
        'email',
        'department',
    )

    list_filter = (
        'department',
        'registered_date',
    )

    search_fields = (
        'username',
        'first_name',
        'last_name',
        'email',
    )

    ordering = ('username',)
    date_hierarchy = 'registered_date'


# --------------------
# COURSE ADMIN
# --------------------
@admin.register(CourseName)
class CourseNameAdmin(admin.ModelAdmin):
    list_display = ('Course', 'CourseCode', 'CourseDescription')
    list_display_links = ('CourseCode',)
    list_editable = ('Course', 'CourseDescription')
    search_fields = ('Course', 'CourseCode', 'CourseDescription')
    list_per_page = 10
    date_hierarchy = 'RegisteredDate'


# --------------------
# TIMETABLE ADMIN
# --------------------
@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):

    list_display = (
    'id',
    'Day',
    'CourseName',
    'Instructor',
    'Venue',
    'TimeStart',
    'TimeEnd',
    'Programme',
    'Semester',
    'Department',
    'RegisteredDate',
)

    list_display_links = ('CourseName',)

    list_editable = (
        'Day',
        'Venue',
        'Programme',
    )

    list_filter = (
        'Day',
        'Programme',
        'Semester',
    )

    search_fields = (
        'Programme',
        'CourseName__Course',
        'Instructor__username',
        'Venue__VenueName',
    )

    date_hierarchy = 'RegisteredDate'
    list_per_page = 10


# --------------------
# VENUE ADMIN
# --------------------
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('VenueName', 'Capacity')
    search_fields = ('VenueName',)
    list_per_page = 10