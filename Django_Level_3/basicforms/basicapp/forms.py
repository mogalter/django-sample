from django import forms
from django.core import validators


# def check_for_z(value):
#     if value[0].lower != 'z':
#         raise forms.ValidationError("Name needs to start with 'Z'")


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    comment = forms.CharField(widget=forms.Textarea)
    # call widget based on type we would get in HTML
    bot_checker = forms.CharField(required=False,
                                  widget=forms.HiddenInput)

    def clean(self):
        all_cleaned_data = super().clean()
        email = all_cleaned_data['email']
        verified_email = all_cleaned_data['verify_email']
        if email != verified_email:
            raise forms.ValidationError("Emails do not match!")
    # MaxLengthValidator takes in a max length.
    # specifying this is false because we don't want to show it on the page for user.
    # Hidden input will hide it from a human user
    # validators=[validators.MaxLengthValidator(0)
    # custom validator func name should be clean_<name>
    # def clean_bot_checker(self):
    #     bot_checker = self.cleaned_data['bot_checker']
    #     if len(bot_checker) > 0:
    #         # we know robot scraped the page.
    #         raise forms.ValidationError("Found a robot!")
    #     return bot_checker
