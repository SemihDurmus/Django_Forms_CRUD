from django import forms
from .models import Student

# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length=50, label="Your name")
#     last_name = forms.CharField(max_length=50, , label="Your surname")
#     number = forms.IntegerField()


class StudentForm(forms.ModelForm):
    # To overwrite a field
    first_name = forms.CharField(label="Enter your name")

    class Meta:
        model = Student
        #fields = ("first_name", "last_name")
        fields = '__all__'

    # Another method for overwriting
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].label = "Type your name"
