## COMMON.FORMS.PY

from django import forms

from petstagram.common.models import Comment






# Comment form for the Class-Based-View
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)



#################################
# # V1 for comment PET - standard form
#################################
# class CommentForm(forms.Form):
#     text = forms.CharField(
#         widget=forms.Textarea(attrs={
#             'class': 'form-control rounded-2',
#
#         }
#         ),
#     )


#################################
# # V2 FOR COMMENT PET - model form
###############################
from petstagram.pets.models import Pet
# pet_pk = forms.IntegerField(
#     widget=forms.HiddenInput()
# )
#
# class Meta:
#     model = Comment
#     fields = ('comment', 'pet_pk')
#
# def save(self, commit=True):
#     pet_pk = self.cleaned_data['pet_pk']
#     pet = Pet.objects.get(pk=pet_pk)
#     comment = Comment(
#         comment=self.cleaned_data['comment'],
#         pet=pet,
#     )
#     if commit:
#         comment.save()
#     return comment









