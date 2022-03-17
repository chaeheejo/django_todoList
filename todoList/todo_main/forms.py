from django import forms
from django.forms import ModelForm
from .models import *
from django.forms.widgets import NumberInput
from django.conf.global_settings import DATE_INPUT_FORMATS

class TaskForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '제목을 입력해주세요'}))
    summary = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '상세 설명을 입력해주세요'}))
    tag = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '태그를 등록해주세요'}))
    due_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = Task
        fields = '__all__'