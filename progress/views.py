from django.shortcuts import render

from django.views import View


class Progress(View):
    def get(self, request):
        return render(request, "progress.html")
