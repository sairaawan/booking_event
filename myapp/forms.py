from django import forms
from .models import Artist, Event


from django.core.exceptions import ValidationError

class ArtistForm(forms.ModelForm):
    Name=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Type your Name',

        }))
    Telephone=forms.IntegerField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Type your contact Number',
        }))
    Members=forms.IntegerField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'No of Members',
        }))
    email=forms.EmailField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Type your Email',
        }))
    Additional_details=forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Write additional details',

        }))
    genre=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Type your genre',

        }))



    class Meta:
      
        model = Artist
        fields = ('Name', 'Telephone', 'Members','email', 'genre', 'Select_event', 'Additional_details')
        widgets={'Select_event':forms.Select(attrs={'class':'form-control'})}
        def clean_email(self):
            email = self.cleaned_data.get('email')
            if  Artist.objects.filter(email=email).exists():
                raise forms.ValidationError('This email address is already in use.')
            return email
        def __init__(self, *args, **kwargs):
            super(ArtistForm, self).__init__(*args, **kwargs)
            self.fields['Select_event'].widget = forms.RadioSelect




