from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    return render(request, 'mysite/index.html')


def bedrooms(request):
    return render(request, 'mysite/bedrooms.html')


def gallery(request):
    return render(request, 'mysite/gallery.html')


def about(request):
    return render(request, 'mysite/about.html')


def contact(request):
    dados = {}
    if request.method == 'POST':
        dados['name'] = request.POST.get('name')
        dados['email'] = request.POST.get('email')
        dados['message'] = request.POST.get('message')

        send_mail(
            dados['name'],
            'Remetente: ' + dados['email'] + '\n\n' + dados['message'],
            '',
            [settings.EMAIL_HOST_USER],
            )

    return render(request, 'mysite/contact.html', dados)


def view_404(request, exception):
    return render(request, 'mysite/index.html')
