from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm


# Create your views here.
# def show_contact(request):
#     contact = Contact.objects.get()

def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, "contacts/list_contacts.html",
                {"contacts": contacts})


def add_contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/add_contact.html", {"form": form})


def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'GET':
        form = ContactForm(instance=contact)
    else:
        form = ContactForm(data=request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/edit_contact.html", {
        "form": form,
        "contact": contact
    })


def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect(to='list_contacts')

    return render(request, "contacts/delete_contact.html",
                {"contact": contact})






#  THIS WAS FROM PAULS IN CLASS ===================================================================
# def add_note(request, contact_pk):
#     # get the associated contact
#     contact = get_object_or_404(Contact, pk=contact_pk)
#     # We need a form!

#     form = NoteForm(data=request.POST)
#     if form.is_valid():
#         note = form.save(
#             commit=False
#         )  # this step lets us save the object, but NOT to rhe database yet!
#         note.contact = contact  # that's so we can do THIS step, associating the note with the contact
#         note.save()  # here is where we save the note with the relationship to contact and everything!
#         return redirect(to="contact_detail", pk=contact.pk)

#     return render(
#         request, "contacts/contact_detail.html", {"note_form": form, "contact": contact}
#     )