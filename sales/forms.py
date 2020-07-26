from django import forms

from .models import Cuboid


# creating a form
class CuboidForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CuboidForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['createdby'].widget.attrs['readonly'] = True

    def clean_sku(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.createdby
        else:
            return self.cleaned_data['createdby']
    # create meta class
    class Meta:
        # specify model to be used
        model = Cuboid

        # specify fields to be used
        fields = [
            "length",
            "breadth",
            "height",
            "createdby",
            "createdtime"
        ]

