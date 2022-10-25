from django.shortcuts import render
from markdown2 import markdown
from . import util
import markdown


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
            return render(request,"encyclopedia/pageNotFound.html")
        else:
            return render(request, "encyclopedia/entry.html",{
                "title": searchTitle,
                "content": searchContent
        })
        
    