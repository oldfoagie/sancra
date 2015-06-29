class codeUploadForm(forms.Form):

    file = forms.FileField()
    place = forms.ModelChoiceField(queryset=Incentive.objects.all())
