from django import forms
from .models import Forum, ForumReply


class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = '__all__'
        exclude = ('forum_creator_id',)


class ForumReplyForm(forms.ModelForm):
    class Meta:
        model = ForumReply
        fields = '__all__'
        exclude = ('commentor_id', 'forum_id')
