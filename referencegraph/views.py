# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from referencegraph.forms import PMIDForm


def home_page(request):
    if request.method == 'POST':
        form = PMIDForm(request.POST)
        
        if form.is_valid():
            return HttpResponseRedirect('/article/{}'.format(form.cleaned_data['pmid']))
    else:
        form = PMIDForm()
    return render(request, 'pages/home.html', {'form': form})

def display_article(request, article_id):
    return render(request, 'pages/article.html')