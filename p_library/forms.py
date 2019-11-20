from django import forms
from p_library.models import Author, Book, Tag

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

    def save(self):
        new_tag = Tag.objects.create(title=self.cleaned_data['title'])
        return new_tag