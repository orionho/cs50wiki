import re
from django.shortcuts import render
from markdown2 import markdown
from . import util
import markdown
from audioop import reverse
from django.http import HttpResponseRedirect
from django.urls import is_valid_path
from django import forms
from django.db import models


class newEntry(models.Model):
        title = models.CharField(max_length=255)
        content = models.TextField()

class newEntryForm(forms.ModelForm):
    class Meta:
        model = newEntry
        fields = ('title', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

    
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def conversionMDtoHTML(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def displayEntry(request, title):
    content = conversionMDtoHTML(title)
    if content == None:
        return render(request,"encyclopedia/pageNotFound.html")
    else:
        return render(request, "encyclopedia/entry.html",{
            "title": title,
            "content": content
        })

def search(request):
    if request.method == "POST":
        searchTitle = request.POST['input']
        searchContent = conversionMDtoHTML(searchTitle)
        if searchContent == None:
            listEntries = util.list_entries()
            possibleEntries = []
            for entry in listEntries:
                if searchTitle.lower() in entry.lower():
                    possibleEntries.append(entry)
            return render(request, "encyclopedia/searchNotFound.html",{
                "possibleEntries": possibleEntries
            })           
        else:
            return render(request, "encyclopedia/entry.html",{
                "title": searchTitle,
                "content": searchContent
        })

def newPage(request):
    if request.method == "POST":
        form = newEntryForm(request.POST)
        util.save_entry(request.POST['title'],request.POST['content'])
         

    return render(request, "encyclopedia/addEntry.html", {
        "form": newEntryForm()
    })
    