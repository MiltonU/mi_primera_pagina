from django.views.generic import TemplateView


class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'


class InboxView(TemplateView):
    template_name = 'accounts/inbox.html'