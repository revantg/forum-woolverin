from django import forms
from authenticate_app.models import thread, reply


class threadForm(forms.ModelForm):
    class Meta():
        model = thread
        fields = ('user_name', 'subject', 'description', 'post_body')


class replyForm(forms.ModelForm):
    class Meta():
        model = reply
        fields = ('user_name', 'reply_body', 'parent_post')
    # def save(self, parent_post_id):
    #     super().save(parent_post_id = parent_post_id)
