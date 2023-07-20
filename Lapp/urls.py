from django.urls import path
from . import views


urlpatterns=[

    path('AddBook',views.addBook,name='AddBook'),
    
    path('Adminlist/',views.Booklist,name="list"),
    path('userlist/',views.userBooklist,name="userlist"),
  
  
    path('<int:id>/',views.updateBook,name="updatingBook"),

]