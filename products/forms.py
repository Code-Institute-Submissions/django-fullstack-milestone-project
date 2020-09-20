from django import forms
from .models import Product, Category, Metal, Theme


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

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
