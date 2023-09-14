from django import forms

class Orderform(forms.Form):
    name = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={"class":"css_input form-control"}))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"css_input form-control"}))



