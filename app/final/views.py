from django.shortcuts import redirect,render,get_object_or_404
from django.views.generic import View
from django.template import loader
from django.http import HttpResponse
from .models import Book,Branch,Inventory

class HomePageView(View):
    def get(self,request):
        
        template  = loader.get_template('final/home.html')

        context = {
            'title':'Henry Bookstore'
        }
        return HttpResponse(template.render(context,request))
   
class BookView(View):
    def get(self, request):
        template = loader.get_template('final/books.html')
        books = Book.objects.all()

        context = {
        'title': 'Henry Bookstore - Books',
        'books': books,

        }

        return HttpResponse(template.render(context, request))
    

class BranchView(View):
    def get(self, request):
        template = loader.get_template('final/branches.html')
        branches = Branch.objects.all()

        context = {
        'title': 'Henry Bookstore - Branches',
        'books': branches,

        }

        return HttpResponse(template.render(context, request))
    
class BranchInventoryView(View):
    def get(self, request, id):
        template = loader.get_template('final/branch_inventory.html')
        #branch .= Branch.objects.filter(id=id)
        branch = get_object_or_404(Branch, id = id)
        inventory = Inventory.objects.filter(branch_id=id)
        #books .= Book.objects.filter(branch_id=id)

        context = {
        'title': 'Henry Bookstore - Branch',
        'branch': branch.name,
        'inventory': inventory,

        }

        return HttpResponse(template.render(context, request))