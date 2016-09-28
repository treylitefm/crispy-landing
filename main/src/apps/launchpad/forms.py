from django import forms
from models import App,Page

class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ('name', 'domain', 'protocol')
        labels = {
            'name': 'App Name',        
            'domain': 'Domain',        
            'protocol': 'Protocol'        
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'name': 'name', 'type': 'text'}),
            'domain': forms.TextInput(attrs={'class': 'form-control', 'name': 'domain', 'type': 'text'}),
            'protocol': forms.Select(attrs={'class': 'form-control'})
        }

    '''
    def clean_name(self):
        #if fails a validation:
        #   rase ValidationError('Custom Error Message Here')
        return self.cleaned_data['name']
    '''

class PageForm(forms.Form):
    pass
