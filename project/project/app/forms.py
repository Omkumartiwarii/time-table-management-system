from django import forms
from .models import Timetable

class TimePickerWidget(forms.TimeInput):
    template_name = 'widgets/timepicker.html'

class TimeTableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = '__all__'
        widgets = {
            'TimeStart': TimePickerWidget(),
            'TimeEnd': TimePickerWidget(),
        }
