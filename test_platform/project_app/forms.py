from django import forms
from .models import Project, Module

# class ProjectForm(forms.Form):
#
#     name = forms.CharField(label = '名称',max_length = 100)
#     describe = forms.CharField(label="描述", widget=forms.Textarea)
#     status = forms.BooleanField(label="状态",rquest = False)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'describe', 'status']   #需要展示的字段
        # exclude = ['create_time']                  #不需要展示的字段


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        exclude = ['create_time']