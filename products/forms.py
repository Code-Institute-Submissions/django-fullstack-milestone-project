from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Metal, Theme, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        metals = Metal.objects.all()
        friendly_names_m = [(m.id, m.get_friendly_name()) for m in metals]

        themes = Theme.objects.all()
        friendly_names_t = [(t.id, t.get_friendly_name()) for t in themes]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        self.fields['metal'].choices = friendly_names_m
        for field_name_m, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        self.fields['theme'].choices = friendly_names_t
        for field_name_t, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'rating',
            'description'
            )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'rating': 'Rating',
            'description': 'Review',
        }

        self.fields['rating'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # field.widget.attrs['class'] = 'border-black rounded-0'
