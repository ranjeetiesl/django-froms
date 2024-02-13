from django.shortcuts import render

# Create your views here.
from django.views import View


class FromView(View):
    template_name = "form.html"
    def get(self, request):
        context = {}
        return render(request, self.template_name)

