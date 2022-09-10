from django import forms

content_max_length = 1000

class PageForm(forms.Form):
    title = forms.CharField(label="Title",max_length=100)
    content = forms.CharField(label="Content", max_length=content_max_length)
    
class PageEditForm(forms.Form):
    title = forms.CharField(label="Title",max_length=100)
    content = forms.CharField(label="Content", max_length=content_max_length, widget=forms.Textarea)
    revision_number = forms.IntegerField(label="Revision_number")
    
class PageMoveForm(forms.Form):
    title_move_to = forms.CharField(label="Title", max_length=100)
    revision_number = forms.IntegerField(label="revision_number")
    content = forms.CharField(label="Content", max_length=content_max_length)