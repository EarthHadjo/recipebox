from django import forms
from news.models import Author

class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=30)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=30)
    instructions = forms.CharField(widget=forms.Textarea)

class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'name'
      ]