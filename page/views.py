from django.http import HttpResponse
from django.shortcuts import render
from .models import Page, Revision
from .forms import PageForm, PageEditForm, PageMoveForm
from .parser.wikimarkup import Parser

def index(request):
    print(request.GET.get('action', None))
    return HttpResponse("hello page")

def page_all(request):
    return render(request, "page_all.html", {'pages': Page.objects.all()})

def page_view(request, page_id):
    page = Page.objects.filter(pk=page_id)[0]
    parser = Parser(page.current_revision.content)
    html_content = parser.parse()
    return render(request, "page_view.html", {
        'page': page,
        'page_id': page.pk,
        'html_content': html_content,
    })

def page_revisions_view(request, page_id):
    revisions = Revision.objects.filter(page__pk=page_id)
    return render(request, 'page_revisions_view.html', {
        'revisions': revisions,
        'page_id': page_id,
    })

def page_create(request):
    if request.method=="POST":
        form = PageForm(request.POST)
        if form.is_valid():
            page = Page(title=form.cleaned_data['title'])
            revision = Revision.objects.create(content=form.cleaned_data['content'], revision_number=1)
            page.current_revision = revision
            page.save()
            revision.page = page
            revision.save()
    else:
        form = PageForm()
    return render(request, "page_create.html", {'form':form})

def page_edit(request, page_id):
    if request.method=="POST":
        form = PageEditForm(request.POST)
        if form.is_valid():
            page = Page.objects.filter(pk=page_id)[0]
            revision = Revision.objects.create(content=form.cleaned_data['content'], revision_number=form.cleaned_data['revision_number']+1, page=page)
            page.current_revision = revision
            page.save()
    else:
        page = Page.objects.filter(pk=page_id)[0]
        form = PageEditForm({
            'title': page.title,
            'content': page.current_revision.content,
            'revision_number': page.current_revision.revision_number,
            })
    return render(request, "page_edit.html", {
        'form':form, 
        'page_id': page.pk
    })

def page_move(request, page_id):
    if request.method=="POST":
        form = PageMoveForm(request.POST)
        if form.is_valid():
            # page_move_from
            page_move_from = Page.objects.filter(pk=page_id)[0]
            revision_move_from = Revision.objects.create(content=None, revision_number=form.cleaned_data['revision_number']+1)
            page_move_from.current_revision = revision_move_from
            page_move_from.save()
            revision_move_from.page = page_move_from
            revision_move_from.save()
            # page_move_to
            revision_move_to = Revision.objects.create(content=form.cleaned_data['content'], revision_number=1)
            page_move_to =  Page(title=form.cleaned_data['title_move_to'])
            page_move_to.current_revision = revision_move_to
            page_move_to.save()
            revision_move_to.page = page_move_to
            revision_move_to.save()
                
    else:
        page_move_from = Page.objects.filter(pk=page_id)[0]
        form = PageMoveForm({
            'revision_number': page_move_from.current_revision.revision_number,
            'content': page_move_from.current_revision.content,
        })
    return render(request, "page_move.html", {
        'form': form,
        'page_id': page_move_from.pk
    })