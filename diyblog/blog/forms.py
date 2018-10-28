from django import forms

class CommentFormat(forms.Form):
    content = forms.CharField(help_text='Please enter your comment')
    blogpost_id = forms.IntegerField()
    def clean_content(self):
        data = self.cleaned_data['content']
        return data
    def clean_blogpost_id(self):
        data = self.cleaned_data['blogpost_id']
        return data