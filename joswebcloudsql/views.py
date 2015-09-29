# Create your views here.
# Create your views here.
from __future__ import print_function

from django.shortcuts import render_to_response
from django.template.context import RequestContext


def landing_page(request):
    context = RequestContext(request,
                           {'request'   : request,
                            'user'      : request.user,
                            'page_name' : 'Landing'})
    return render_to_response('landing_page.html', context_instance=context)


def login(request):
    context = RequestContext(request,
                           {'request'   : request,
                            'user'      : request.user,
                            'page_name' : 'Login'})
    return render_to_response('login.html', context_instance=context)