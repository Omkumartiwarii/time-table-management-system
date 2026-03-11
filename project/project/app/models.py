from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError



# --------------------
# CHOICES
# --------------------

DAY_CHOICES = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
]

SESSION_CHOICES = [
    ('Tutorial', 'Tutorial'),
    ('Lecture', 'Lecture'),
    ('Practical', 'Practical'),
    ('Lab', 'Lab'),
    ('Discussion', 'Discussion'),
    ('Seminar', 'Seminar'),
    ('Presentation', 'Presentation'),
]

YEAR_OF_STUDY = [
    ('FY', 'First Year'),
    ('SY', 'Second Year'),
    ('TY', 'Third Year'),
    ('LY', 'Final Year'),
]

SEMESTER = [
    ('1', 'Semester 1'),
    ('2', 'Semester 2'),
    ('3', 'Semester 3'),
    ('4', 'Semester 4'),
    ('5', 'Semester 5'),
    ('6', 'Semester 6'),
    ('7', 'Semester 7'),
    ('8', 'Semester 8'),
]


# --------------------
# DEPARTMENT
# --------------------

class Department(models.Model):
    DepartmentName = models.CharField(max_length=100, primary_key=True)
    HeadOfDepartment = models.CharField(max_length=100)
    RegisteredDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.DepartmentName


# --------------------
# INSTRUCTOR (CUSTOM USER)
# --------------------

class Instructor(AbstractUser):

    middle_name = models.CharField(max_length=100, null=True, blank=True)

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    max_hours_per_week = models.IntegerField(default=20)

    registered_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Instructor"
        verbose_name_plural = "Instructors"

    def __str__(self):
        return self.username


# --------------------
# COURSE
# --------------------

class CourseName(models.Model):

    Course = models.CharField(max_length=100)
    CourseCode = models.CharField(max_length=20, primary_key=True)
    CourseDescription = models.CharField(max_length=200)

    RegisteredDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return f"{self.Course} ({self.CourseCode})"


# --------------------
# VENUE (CLASSROOM / LAB)
# --------------------

class Venue(models.Model):

    VenueName = models.CharField(max_length=100, primary_key=True)
    Capacity = models.IntegerField()

    def __str__(self):
        return self.VenueName


# --------------------
# SECTION (CLASS GROUP)
# --------------------

class Section(models.Model):

    name = models.CharField(max_length=10)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


# --------------------
# TIME SLOT
# --------------------

class TimeSlot(models.Model):

    start_time = models.TimeField()
    end_time = models.TimeField()

    def clean(self):

        if self.end_time <= self.start_time:
            raise ValidationError("End time must be after start time")

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"


# --------------------
# TIMETABLE
# --------------------

class Timetable(models.Model):

    CourseName = models.ForeignKey(
        CourseName,
        on_delete=models.CASCADE
    )

    Instructor = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE
    )

    Department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    Section = models.ForeignKey(
        Section,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    Venue = models.ForeignKey(
        Venue,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    TimeStart = models.TimeField()
    TimeEnd = models.TimeField()

    Programme = models.CharField(max_length=100)

    YearOfStudy = models.CharField(
        max_length=2,
        choices=YEAR_OF_STUDY
    )

    Semester = models.CharField(
        max_length=1,
        choices=SEMESTER
    )

    Session = models.CharField(
        max_length=20,
        choices=SESSION_CHOICES,
        default='Lecture'
    )

    Day = models.CharField(
        max_length=10,
        choices=DAY_CHOICES
    )

    RegisteredDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Timetable"
        verbose_name_plural = "Timetables"

        unique_together = (
            'Day',
            'TimeStart',
            'Venue'
        )

        ordering = ['Day']

    def __str__(self):
        return f"{self.Programme} | {self.CourseName} | {self.Day}"