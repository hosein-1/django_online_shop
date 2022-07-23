from django.views import generic


class HomePageView(generic.TemplateView):
    template_name = 'home.html'


class AboutUsView(generic.TemplateView):
    template_name = 'pages/about_us.html'
