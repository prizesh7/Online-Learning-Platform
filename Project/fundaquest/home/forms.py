from django import forms

class SearchForm(forms.Form):
	q = forms.CharField(
        max_length=2000,
        widget= forms.TextInput(attrs={'placeholder':'Search...', 'class':'mySearch'}),
		label=""
    )
