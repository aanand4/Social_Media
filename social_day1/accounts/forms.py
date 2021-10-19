from django import forms
from .models  import Comment
from emoji_picker.widgets import EmojiPickerTextInputAdmin, EmojiPickerTextareaAdmin


class CommentForm(forms.ModelForm):
	comment = forms.CharField()
	class Meta:
		model = Comment
		fields = ['comment',]