from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.db.models import Q

from .models import Contact
from .forms import ContactForm

def contacts(request):
    data = Contact.objects.filter(user=request.user.id).order_by('last_name')
    return render(request, 'contacts.html', {'data':data})

def view(request, id):
    item = Contact.objects.get(id=id)
    return render(request, 'view.html', {'item':item})

def add(request):
    form=ContactForm(request.POST or None)
    form.instance.user = request.user
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/contacts')
    return render(request, 'add.html', {'form':form})

def delete(request, id):
    item = Contact.objects.get(id=id)
    item.delete()
    return redirect('contacts')

def search(request):
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Contact.objects.filter(
                Q(user=request.user.id) &
                (Q(first_name__icontains=query_name) |
                Q(last_name__icontains=query_name) |
                Q(phone_number__icontains=query_name) |
                Q(address__icontains=query_name))
                ).order_by('last_name')
            return render(request, 'search.html', {"results":results, 'query_name':query_name})
    return render(request, 'search.html')
