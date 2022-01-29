from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Category

def index(request):
	categories = Category.objects.values().all()
	print('Here i am')
	print(categories[0]['image'])


	return render(request, 'categories/index.html', {'categories':categories})

def detail(request, category_id):
	category_detail = get_object_or_404(Category,pk=category_id)
	return render(request, 'categories/detail.html', {'category':category_detail})
