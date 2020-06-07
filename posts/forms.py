from django import forms
from .models import Post, Group


class PostForm(forms.ModelForm):
    text = forms.CharField(label='Пост', widget=forms.widgets.Textarea())
    group = forms.ModelChoiceField(label='Сообщество', queryset=Group.objects.all(), required=False)

    class Meta:
        model = Post
        fields = ('text', 'group')
        
        