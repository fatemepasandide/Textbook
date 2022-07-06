from django.shortcuts import render
from .forms import ContactUsForm
from django.shortcuts import redirect
from django.contrib import messages


def contactUs(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            #form = form.save(commit=False)
            form.save()
            messages.success(request, 'Your message sended successfully!')
            return redirect('/contactus')
        else:
            print('form is not valid')
    else:
        form = ContactUsForm()
    return render(request,'contactus.html',{'form': form})


