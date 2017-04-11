from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

	class Meta:
		model = Article
		fields = ['title','content']

class EmailPostForm(forms.Form):

	name = forms.CharField(max_length=25)
	email = forms.EmailField()
	to = forms.EmailField()
	comments = forms.CharField(required=False,widget=forms.Textarea)