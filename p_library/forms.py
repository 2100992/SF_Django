from django import forms
from p_library.models import Author, Book, Tag, UserProfile
from django.core.exceptions import ValidationError

class AuthorForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput)
    
    class Meta:
        model = Author
        fields = '__all__'

class BookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput)
    class Meta:
        model = Book
        fields = '__all__'

class TagForm(forms.Form):
    title = forms.CharField(max_length=50)

    title.widget.attrs.update({'class':'form-control'})

    def clean_title(self):
        new_title = self.cleaned_data['title']

        if Tag.objects.filter(title=new_title).count():
            raise ValidationError('Title must be unique.')
        return new_title


    def save(self):
        new_tag = Tag.objects.create(title=self.cleaned_data['title'])
        return new_tag

class ProfileCreationForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['birth_date']