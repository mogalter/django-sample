from django.shortcuts import render
from basicapp import forms
# Create your views here.


def index(request):
    return render(request, 'basicapp/index.html')


def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)  # pass in form information
        if form.is_valid():
            # DO SOMETHING CODE
            print("Validation success!")
            print(form.cleaned_data)
    return render(request, "basicapp/forms.html", {'form': form})