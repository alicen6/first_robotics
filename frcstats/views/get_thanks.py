from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import View


def get_thanks(request):
    context = {}
    return render(request, 'thanks.html', context)
