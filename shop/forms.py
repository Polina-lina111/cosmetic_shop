from django import forms


class ReviewForm(forms.Form):

    username = forms.CharField(
        max_length=100,
        label="Ім'я"
    )

    message = forms.CharField(
        widget=forms.Textarea,
        label="Відгук"
    )

    rating = forms.IntegerField(
        min_value=1,
        max_value=5,
        label="Оцінка"
    )

    def clean_message(self):

        message = self.cleaned_data["message"]

        if len(message) < 5:
            raise forms.ValidationError(
                "Відгук занадто короткий"
            )

        return message