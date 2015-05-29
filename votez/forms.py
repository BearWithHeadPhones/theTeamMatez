from django import forms
from .models import Vote




class VoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VoteForm, self).__init__(*args, **kwargs)
        self.fields['wordsOfAppreciation'].label = 'Express yourself?'
    class Meta:
        model = Vote
        fields = ['levelOfAppreciation', 'wordsOfAppreciation']

