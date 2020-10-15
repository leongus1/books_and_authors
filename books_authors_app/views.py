from django.shortcuts import render, redirect, HttpResponse
from .models import books, authors

# Create your views here.
def index(request):
    context = {
        'all_books' : books.objects.all()
    }
    return render(request, 'index.html', context)

def author_index(request):
    context={
        'all_authors': authors.objects.all()
    }
    return render(request, 'authors.html', context)

def authors_list(request, id_num):
    context={
        'this_name': f'{authors.objects.get(id=id_num).first_name} {authors.objects.get(id=id_num).last_name}',
        'id': id_num,
        'Desc_or_Notes': "Notes",
        'desc': authors.objects.get(id=id_num).notes,
        'this_list': authors.objects.get(id=id_num).books.all(),
        'list': books.objects.all(),
        'is_books': False,
    }
    return render(request, 'details.html', context)

def add_author(request):
    authors.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'] )
    return redirect('/authors')

def book_list(request, id_num):
    context={
        'this_name': books.objects.get(id=id_num).title,
        'id': id_num,
        'Desc_or_Notes': "Description",
        'desc': books.objects.get(id=id_num).desc,
        'this_list': books.objects.get(id=id_num).authors.all(),
        'list': authors.objects.all(),
        'is_books': True,
    }
    return render(request, 'details.html', context)

def add_book(request):
    books.objects.create(title = request.POST['title'], desc = request.POST['desc'])
    return redirect('/')


def book_add_auth(request, id_num):
    this_book = books.objects.get(id=id_num)
    auth_add = authors.objects.get(id=request.POST['to_add'])
    print(auth_add)
    this_book.authors.add(auth_add)
    # this_book.save()
    return redirect(f'/books/{id_num}')

def auth_add_book(request, id_num):
    this_auth = authors.objects.get(id=id_num)
    book_add = books.objects.get(id=request.POST['to_add'])
    # print(auth_add)
    this_auth.books.add(book_add)
    # this_book.save()
    return redirect(f'/authors/{id_num}')