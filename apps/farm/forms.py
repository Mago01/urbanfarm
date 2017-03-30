from django import forms
# from uploads.core.models import Document

# class DocumentForm(forms.ModelForm):
#     class Meta:
#         model = Document
#         fields = ('description', 'document', )

class FarmImage(forms.Form):
    image = forms.ImageField(
        label='image'
    )
