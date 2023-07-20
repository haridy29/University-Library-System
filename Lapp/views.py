from django.shortcuts import render,redirect
from .models import *
from django.urls import reverse
# Create your views here.



def addBook(request):
    
    if request.method=='POST':
        ISBN=request.POST.get('isbn')
        Title=request.POST.get('title')
        author=request.POST.get('author')
        edition=request.POST.get('edition')
        publication=request.POST.get('publication')
        BorrowingPeriod=request.POST.get('Borrowing_period')
        Status=request.POST.get('status')
        imageBook=request.FILES['Image']
        
        if Status=='available':
            S=True
        else: 
            S=False    
        newBook=Book(ISBN=ISBN,Title=Title,Author=author,Edition=edition,Publication=publication,Borrowing_period=BorrowingPeriod,Status=S,ImageBook=imageBook)

        newBook.save()
       
        return redirect('Adminlist/')

    return render(request,'pages/addingBook.html')

def demo(request):
    return render(request,'pages/demo.html')





def Booklist(request):
    search=Book.objects.all()
    title=None
    if 'search' in request.GET:
        title=request.GET['search']
        if title:
            search=search.filter(Title=title)
    context={
        'books': search,
    }

    #if request.method=='POST':
     #   s=request.POST.get('ed')
      #  return redirect('/updateBook')

    return render(request,'pages/BookList_admin.html',context)


def userBooklist(request):
    search=Book.objects.all()
    title=None
    if 'search' in request.GET:
        title=request.GET['search']
        if title:
            search=search.filter(Title=title)
    context={
        'books': search,
    }


    return render(request,'pages/BookList_user.html',context)



def updateBook(request,id):
    Book_edit=Book.objects.get(id=id)
    Book2=Book.objects.get(id=id)
    context={
        'books':Book_edit
    }

    if request.method=='POST':
        ISBN=request.POST.get('isbn')
        Title=request.POST.get('title')
        Author=request.POST.get('author')
        Edition=request.POST.get('edition')
        Borrowing_period=request.POST.get('Borrowing_period')
        Status=request.POST.get('status')
        imageBook=request.FILES['Image']
        
        Book2.ISBN=ISBN
        Book2.Title=Title
        Book2.Author=Author
        Book2.Edition=Edition
        Book2.Borrowing_period=Borrowing_period
        Book2.ImageBook=imageBook

        if Status=='available':
             Book2.Status=True
        else:
             Book2.Status=False
        
        Book2.save()
        return redirect('/Adminlist')
    return render(request,'pages/updatingBook.html',context)
