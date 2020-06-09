from django import forms
from .models import Post, Group


class PostForm(forms.ModelForm):
    text = forms.CharField(label='Пост', widget=forms.widgets.Textarea()) #Данное поле определил явно, так как в условии задания
    class Meta:                                                           #данное поле указано обязательным (как это реализовать через
        model = Post                                                      #Meta Class я не сообразил)
        required = {'text': True}
        fields = ('text', 'group') #Очень долго ломал голову, как реализовать 
        labels = {                 #выпадающий список групп, но с возможностью
            'text': 'Текст',       #создания новой группы
            'group': 'Сообщество'
            }
        help_text = {
            'text': 'Hапишите свой пост здесь',
            'group': 'Выберите сообщество'
            }
