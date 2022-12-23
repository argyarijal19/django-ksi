from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'judul',
            'body',
            'category',
        ]

        labels = {
            'author': 'Penulis',
        }

        widgets = {
            'judul': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'isi dengan judul artikel', }
            ),

            'author': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'nama penulis', }
            ),


            'body': forms.Textarea(
                attrs={
                    'class': 'form-control', }
            ),


            'category': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
