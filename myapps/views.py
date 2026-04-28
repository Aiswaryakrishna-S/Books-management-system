from django.shortcuts import render,redirect,get_object_or_404
from .models import Books


def  home(request):
    books=Books.objects.all()
    return render(request,'home.html',{'books':books})

def add_book(request):
    if request.method=='POST':
        bookname=request.POST.get('bookname')
        author=request.POST.get('author')
        category=request.POST.get('category')
        price=request.POST.get('price')
        photo=request.FILES.get('photo')


        Books.objects.create(
            bookname=bookname,
            author=author,
            category=category,
            price=price,
            photo=photo
        )
        return redirect('home')
    return render(request,'add_book.html')


def delete_book(request, id):
    book=get_object_or_404(Books ,id=id)
    
    if request.method=="POST":
     Books.delete()
     return redirect('home')
    return render(request,'delete_book.html',{'book':book})


def update_book(request ,id):

    Book=get_object_or_404(Books ,id=id)
    if request.method=='POST':
        Book.bookname=request.POST.get('bookname')
        Book.author=request.POST.get('author')
        Book.category=request.POST.get('category')
        Book.price=request.POST.get('price')
        photo=request.FILES.get('photo')

        if photo:
            Book.photo=photo
        
        Book.save()
        return redirect('home')
    return render(request,'update_book.html',{'book':Book})


