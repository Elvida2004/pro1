from django import forms
from django.core.validators import RegexValidator
from cleaning.models import Order

class StyleFormMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class OrderCreateForm(StyleFormMixin, forms.ModelForm):
    phone = forms.CharField(
        max_length=17,
        validators=[RegexValidator(r'^\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}$', message="Формат: +7(XXX)-XXX-XX-XX")],
        label="Телефон",
        widget=forms.TextInput(attrs={'placeholder': '+7(XXX)-XXX-XX-XX'})
    )
    is_custom_service = forms.BooleanField(
        required=False,
        label="Иная услуга",
        widget=forms.CheckboxInput(attrs={}),  # без класса form-control
    )
    custom_service = forms.CharField(
        required=False,
        label="Описание иной услуги",
        widget=forms.Textarea(attrs={'placeholder': 'Опишите услугу', 'rows': 3})
    )

    class Meta:
        model = Order
        fields = [
            'address', 'phone', 'email', 'service',
            'is_custom_service', 'custom_service',
            'date_and_time', 'payment_type'
        ]
        widgets = {
            'date_and_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Удаляем класс form-control у чекбокса, чтобы он был стандартным квадратом с галочкой
        if 'is_custom_service' in self.fields:
            self.fields['is_custom_service'].widget.attrs.pop('class', None)

    def clean(self):
        cleaned_data = super().clean()
        is_custom_service = cleaned_data.get('is_custom_service')
        service = cleaned_data.get('service')

        if not is_custom_service and not service:
            self.add_error('service', 'Это поле обязательно, если не выбрана иная услуга.')

        return cleaned_data


class OrderUpdateForm(StyleFormMixin, forms.ModelForm):
    phone = forms.CharField(
        max_length=17,
        validators=[RegexValidator(r'^\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}$', message="Формат: +7(XXX)-XXX-XX-XX")],
        label="Телефон",
        widget=forms.TextInput(attrs={'placeholder': '+7(XXX)-XXX-XX-XX'})
    )
    is_custom_service = forms.BooleanField(
        required=False,
        label="Иная услуга",
        widget=forms.CheckboxInput(attrs={}),  # без класса form-control
    )
    custom_service = forms.CharField(
        required=False,
        label="Описание иной услуги",
        widget=forms.Textarea(attrs={'placeholder': 'Опишите услугу', 'rows': 3})
    )

    class Meta:
        model = Order
        fields = [
            'address', 'phone', 'email', 'service',
            'is_custom_service', 'custom_service',
            'date_and_time', 'payment_type'
        ]
        widgets = {
            'custom_service': forms.Textarea(attrs={'rows': 3}),
            'date_and_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Удаляем класс form-control у чекбокса, чтобы он был стандартным квадратом с галочкой
        if 'is_custom_service' in self.fields:
            self.fields['is_custom_service'].widget.attrs.pop('class', None)

    def clean(self):
        cleaned_data = super().clean()
        is_custom_service = cleaned_data.get('is_custom_service')
        service = cleaned_data.get('service')

        if not is_custom_service and not service:
            self.add_error('service', 'Это поле обязательно, если не выбрана иная услуга.')

        return cleaned_data
