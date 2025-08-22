from django.views.generic import TemplateView

class InboxView(TemplateView):
    template_name = 'accounts/inbox.html'