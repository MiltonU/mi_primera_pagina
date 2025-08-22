from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Message
from .forms import MessageForm

class InboxView(LoginRequiredMixin, ListView):
    model = Message
    template_name = "messenger/inbox.html"
    context_object_name = "messages"

    def get_queryset(self):
        qs = Message.objects.filter(recipient=self.request.user).order_by("-sent_at")
        read = self.request.GET.get("read")
        sender = self.request.GET.get("sender")

        if read == "true":
            qs = qs.filter(read=True)
        elif read == "false":
            qs = qs.filter(read=False)

        if sender:
            qs = qs.filter(sender__username__icontains=sender)

        return qs

class SentView(LoginRequiredMixin, ListView):
    model = Message
    template_name = "messenger/sent.html"
    context_object_name = "sent_messages"

    def get_queryset(self):
        return Message.objects.filter(sender=self.request.user).order_by("-sent_at")

class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = "messenger/detail.html"
    context_object_name = "message"

    def get_object(self):
        message = super().get_object()
        if message.recipient == self.request.user and not message.read:
            message.read = True
            message.save()
        return message

class ComposeView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = "messenger/compose.html"
    success_url = reverse_lazy("messenger:sent")

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)

class ReplyView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = "messenger/reply.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["original_message"] = get_object_or_404(Message, pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        original = get_object_or_404(Message, pk=self.kwargs["pk"])
        form.instance.sender = self.request.user
        form.instance.recipient = original.sender
        form.instance.subject = f"Re: {original.subject}"
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("messenger:sent")