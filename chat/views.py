from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User


@login_required
def chat_page(request):
    if request.user.is_staff:
        return redirect('index')
    sent_messages = Message.objects.filter(is_active=True, sender_user=request.user).order_by('created_date')
    # TODO: Choose a limit for sending messages
    if len(sent_messages) > 10:
        messages.error(
            request,
            "You've reached the limitation of sending messages! Please try again later."
        )
        form = MessageForm()
    elif request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            sent_messages = form.save(commit=False)
            sent_messages.sender_user = request.user
            sent_messages.respond_text = ''
            sent_messages.is_responded = False
            sent_messages.is_active = True
            sent_messages.save()
            return redirect('chat_page')
    else:
        form = MessageForm()

    return render(request, "chat.html", {"form": form, "sent_messages": sent_messages})


def error_page(request):
    return render(request, 'error.html')


@login_required
def messages_received(request):
    if request.user.is_staff:
        ids = Message.objects.filter(
            Q(responder_user=request.user) | Q(responder_user=None)
        ).values('sender_user')
        users = User.objects.filter(id__in=ids)

        return render(request, 'available_messages.html', {'users': users})

