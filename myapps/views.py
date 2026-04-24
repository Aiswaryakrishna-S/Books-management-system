from django.shortcuts import render,redirect,get_object_or_404
from .models import Books

def  home(request):
    books=Books.objects.all()
    return render(request,'home.html',{'books':books})

def add_book(request):
    if request.method=='POST':
        bookname=request.POST.get('book name')
        author=request.POST.get('author')
        category=request.POST.get('category')
        price=request.POST.get('price')
        Books.objects.create(
            bookname=bookname,
            author=author,
            category=category,
            price=price,
        )
        return redirect('home')
    return render(request,'add_book.html',{'book':Books})

def delete_book(request, id):
    Book=get_object_or_404(Books ,id=id)
    
    if request.method=="POST":
     Book.delete()
     return redirect('home')
    return render(request,'delete_book.html',{'book':Book})

def update_book(request ,id):

    Book=get_object_or_404(Books ,id=id)
    if request.method=='POST':
        Book.bookname=request.POST.get('bookname')
        Book.author=request.POST.get('author')
        Book.category=request.POST.get('category')
        Book.price=request.POST.get('price')
        Book.save()
        return redirect('home')
    return render(request,'update_book.html',{'book':Book})
