from django.shortcuts import render


def standard(request):
	return render(request, 'bedrooms/standard.html')


def higher(request):
	return render(request, 'bedrooms/higher.html')


def deluxe(request):
	return render(request, 'bedrooms/deluxe.html')
