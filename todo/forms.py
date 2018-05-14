from django import forms
from .models import Quest, Choice

class QuestForm(forms.ModelForm):

    class Meta:
        model = Quest
        fields = ['quest_name', 'quest_text', 'levels']

    def __init__(self, *args, **kwargs):
        super(QuestForm, self).__init__(*args, **kwargs)
        self.fields['quest_name'].widget.attrs.update({
            'class': 'form-control',
            'name': 'quest_name'})
        self.fields['quest_text'].widget.attrs.update({
            'class': 'form-control',
            'name': 'quest_text'})



class LogForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields = ['choice_text']

    def __init__(self, *args, **kwargs):
        super(LogForm, self).__init__(*args, **kwargs)
        self.fields['choice_text'].widget.attrs.update({
            'class': 'form-control',
            'name': 'choice_text'})
