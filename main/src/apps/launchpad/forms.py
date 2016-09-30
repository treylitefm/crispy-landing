from django import forms
from models import App,Page

class AppForm(forms.ModelForm):
    def clean_domain(self):
        data = self.cleaned_data['domain']
        if data.startswith('http://'):
            data = data.replace('http://', '')
        if data.startswith('https://'):
            data = data.replace('https://', '')
        return data
    class Meta:
        model = App
        fields = ('name', 'domain', 'protocol')
        labels = {
            'name': 'App Name',        
            'domain': 'Domain (Include port number if not running on ports 80/443)',        
            'protocol': 'Protocol'        
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'name': 'name', 'type': 'text'}),
            'domain': forms.TextInput(attrs={'class': 'form-control', 'name': 'domain', 'type': 'text'}),
            'protocol': forms.Select(attrs={'class': 'form-control'})
        }

class PageForm(forms.ModelForm):
    def clean_path(self):
        data = self.cleaned_data['path']
        if data[0] != '/':
            data = '/'+data
        data = data.replace(' ', '')
        return data
    class Meta:
        model = Page
        fields = ('path',)
        labels = {
            'path': 'Path'        
        }
        widgets = {
            'path': forms.TextInput(attrs={'placeholder': 'Path', 'class': 'path form-control', 'name': 'path', 'type': 'text'})
        }
