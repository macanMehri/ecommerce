from django.shortcuts import render, redirect, get_object_or_404
from .models import Message, Connection
from .forms import UserMessageForm, AdminMessageForm
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
    if len(sent_messages) > 100:
        messages.error(
            request,
            "You've reached the limitation of sending messages! Please try again later."
        )
        form = UserMessageForm()
    elif request.method == "POST":
        form = UserMessageForm(request.POST)
        if form.is_valid():
            sent_messages = form.save(commit=False)
            sent_messages.sender_user = request.user
            sent_messages.respond_text = ''
            sent_messages.is_responded = False
            sent_messages.is_active = True
            sent_messages.save()
            # Search for the connection
            connection = Connection.objects.filter(user=request.user)
            # Create a connection for message
            if not connection:
                new_connection = Connection(admin=None, user=request.user)
                new_connection.save()
            return redirect('chat_page')
    else:
        form = UserMessageForm()

    return render(request, "chat.html", {"form": form, "sent_messages": sent_messages})


@login_required
def messages_received(request):
    if request.user.is_staff:
        ids = Connection.objects.filter(
            Q(admin=request.user) | Q(admin=None)
        ).values('user')
        users = User.objects.filter(id__in=ids)

        last_messages = Message.objects.filter(is_active=True, sender_user__in=ids)
        # Create a list for users with un answered messages
        unseen_users = list()
        for last_message in last_messages:
            if not last_message.is_responded:
                unseen_users.append(last_message.sender_user)

        return render(
            request, 'available_messages.html', {'users': users, 'unseen_users': unseen_users}
        )


@login_required
def create_connection(request, user_id):
    """When an admin clicks on a users message"""
    user = get_object_or_404(User, id=user_id)
    connection = get_object_or_404(Connection, user=user)
    if not connection.admin:
        connection.admin = request.user
        connection.is_active = True
        connection.save()

    sent_messages = Message.objects.filter(is_active=True, sender_user=user).order_by('created_date')
    last_message = sent_messages[len(sent_messages)-1]
    # The condition that admin wants to send two or more messages in a row
    if last_message.is_responded and request.method == 'POST':
        form = AdminMessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.sender_user = user
            new_message.sent_text = ''
            new_message.responder = request.user
            new_message.is_responded = True
            new_message.is_active = True
            new_message.save()
            return redirect('create_connection', user_id=user_id)

    elif request.method == 'POST':
        form = AdminMessageForm(request.POST, instance=last_message)
        set_messages_responded(sent_messages)
        if form.is_valid():
            last_message.responder_user = request.user
            last_message.is_responded = True
            last_message.is_active = True
            form.save()
            return redirect('create_connection', user_id=user_id)
    else:
        form = AdminMessageForm()
    return render(request, "chat_for_admin.html", {"form": form, "sent_messages": sent_messages})


def set_messages_responded(messages_list):
    for message in messages_list:
        message.is_responded = True
        message.save()
