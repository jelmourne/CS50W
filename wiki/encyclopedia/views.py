from django.shortcuts import render, redirect
from markdown2 import markdown
import random

from . import util, form

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, wiki_entry): 
    title = util.get_entry(wiki_entry)
    if title == None:
        return errorType(request, wiki_entry, "Unable to find any pages")

    return render(request, "encyclopedia/entries.html", {
        "wiki_entries": markdown(title),
        "title": wiki_entry
    })

def search(request):
    """
    1.If the query matches the name of an encyclopedia entry, 
    the user should be redirected to that entry's page.

    2.If the query does not match the name of an encyclopedia entry, 
    the user should instead be taken to a search results page that 
    displays a list of all encyclopedia entries that have the query as 
    a substring. For example, if the search query were ytho, then Python 
    should appear in the search results.

    3.Clicking on any of the entry names on the search results 
    page should take the user to that entry's page.
    """
    result = request.GET.get("q")
    entries = []
    for entry in util.list_entries():

        if result == entry:
            return redirect('entry', wiki_entry=entry)
        
        elif result.lower() in entry.lower():
            entries.append(entry)

    if not entries:
        return errorType(request, result, "Unable to find any results ")
    
    return render(request, "encyclopedia/index.html", {
        "entries":entries,
        "result":result
        })

def create(request):
    """
    1.Users should be able to enter a title for the page and, in a textarea, 
    should be able to enter the Markdown content for the page.

    2.Users should be able to click a button to save their new page.

    3.When the page is saved, if an encyclopedia entry already exists with 
    the provided title, the user should be presented with an error message.

    4.Otherwise, the encyclopedia entry should be saved to disk, and the user 
    should be taken to the new entry's page.
    """
    if request.POST: 
        forms = form.createEntry(request.POST)

        if forms.is_valid():
            title = forms.cleaned_data['title']
            content = forms.cleaned_data['content']

            wiki_page = util.get_entry(title)

            if wiki_page is not None:
                return errorType(request, title, "Page already exisits")

            util.save_entry(title, content)

        return redirect('entry', wiki_entry=title)
        
    return render(request, "encyclopedia/create.html", {
        "form": form.createEntry
    })

def rand(request):
    """    
    1.Clicking “Random Page” in the sidebar should take user to a random encyclopedia entry.
    """
    title = random.choice(util.list_entries())
    return redirect ('entry', wiki_entry=title)

def errorType(request, error, errorType):
    return render(request, "encyclopedia/error.html", {
        "error":error,
        "type": errorType
    })

def edit(request, wiki_entry):
    """
    1.The textarea should be pre-populated with the existing Markdown content of the page. 
    (i.e., the existing content should be the initial value of the textarea).

    2.The user should be able to click a button to save the changes made to the entry.

    3.Once the entry is saved, the user should be redirected back to that entry's page.
    """
    forms = form.editEntry(request.POST)

    if forms.is_valid():
        content = forms.cleaned_data["content"]
        util.save_entry(wiki_entry,content)

        return redirect('entry', wiki_entry=wiki_entry)

    return render(request, "encyclopedia/edit.html", {
        "form":form.editEntry(initial={'content':util.get_entry(wiki_entry)}),
        "title":wiki_entry
    })


