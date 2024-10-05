from django import forms
from products.models import Product, LineOfBusiness

class ProductForm(forms.ModelForm):
    LOBID = forms.ModelChoiceField(queryset=LineOfBusiness.objects.all(),
                                   widget=forms.Select(attrs={
                                       'class': 'form-control py-4',
                                       'placeholder': 'Выберите линию бизнеса'
                                   }))
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите название продукта'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-label'}), required=False)
    name_for_str_metafield = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите название дополнительного строкового поля (необязательно)'}), required=False)
    str_value = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите значение дополнительного поля (необязательно)'}), required=False)
    name_for_numeric_metafield = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите название название дополнительного числового поля (необязательно)'}), required=False)
    numeric_value = forms.DecimalField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите значение дополнительного поля (необязательно)'}), required=False)
    name_for_date_metafield = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите название дополнительного значения дат (необязательно)'}), required=False)
    begin = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите дату начала (необязательно)'}), required=False)
    end = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите дату окончания (необязательно)'}), required=False)


    def clean_str(self):
        cleaned_data = super().clean()
        name_for_str_metafield = cleaned_data.get('name_for_str_metafield')
        str_value = cleaned_data.get('str_value')

        if name_for_str_metafield and not str_value or not name_for_str_metafield and str_value:
            raise forms.ValidationError("Пожалуйста, заполните оба поля.")
        return cleaned_data

    def clean_num(self):
        cleaned_data = super().clean()
        name_for_numeric_metafield = cleaned_data.get('name_for_numeric_metafield')
        numeric_value = cleaned_data.get('numeric_value')

        if name_for_numeric_metafield and not numeric_value or not name_for_numeric_metafield and numeric_value:
            raise forms.ValidationError("Пожалуйста, заполните оба поля.")
        return cleaned_data

    def clean_date(self):
        cleaned_data = super().clean()
        name_for_date_metafield = cleaned_data.get('name_for_date_metafield')
        begin = cleaned_data.get('begin')
        end = cleaned_data.get('end')

        if ((name_for_date_metafield and (begin and end) == False) or
                (not name_for_date_metafield and (begin and end) == True)):
            raise forms.ValidationError("Пожалуйста, заполните все 3 поля.")
        return cleaned_data

    class Meta:
        model = Product
        fields = ('name', 'LOBID', 'image', 'name_for_str_metafield',
                  'str_value', 'name_for_numeric_metafield', 'numeric_value',
                  'name_for_date_metafield', 'begin', 'end')


