# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.


# index
def index(request):
    return render_to_response('so/index-code.html')