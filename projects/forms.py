from django.forms import ModelForm
from django import forms
from .models import Project

class ProjectFrom(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image' , 'description', 'demo_link', 'source_code', 'tags']

        widgets = {
            'tags' : forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *arg, **kwarg):
        super(ProjectFrom, self).__init__(*arg, **kwarg)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


        # self.fields['title'].widget.attrs.update({'class': 'input',  'placeholder': 'Add title'})
        # self.fields['description'].widget.attrs.update({'class': 'input'})
        # self.fields['demo_link'].widget.attrs.update({'class': 'input'})
        # self.fields['source_code'].widget.attrs.update({'class': 'input'})