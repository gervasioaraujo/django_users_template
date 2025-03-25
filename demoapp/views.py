from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse


@login_required
def index(request):
    template = 'demoapp/index.html'
    return render(request, template, {})
    # return HttpResponse("Hello, world. You're at the demoapp index.")


