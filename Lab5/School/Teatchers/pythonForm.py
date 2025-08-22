from django import forms

class TeacherForm(forms.Form):
    name = forms.CharField(max_length=100, label="الاسم")
    experience_years = forms.IntegerField(label="سنوات الخبرة", min_value=0)
    salary = forms.DecimalField(label="الراتب", max_digits=10, decimal_places=2)
    notes = forms.CharField(
        label="ملاحظات",
        widget=forms.Textarea,
        required=False
    )
    is_active = forms.BooleanField(label="مازال يدرس؟", required=False, initial=True)
    hire_date = forms.DateField(label="تاريخ التوظيف", widget=forms.DateInput(attrs={'type': 'date'}))
    start_time = forms.TimeField(label="وقت البداية", widget=forms.TimeInput(attrs={'type': 'time'}))
