from django import forms #  import from
from .models import Python_Jun # here we create form for python_jun model so importting this model

class PythonForm(forms.ModelForm):
    class Meta:
        model = Python_Jun
        fields = '__all__'
     