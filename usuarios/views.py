from django.shortcuts import render, redirect
from .models import Morador
from .forms import MoradorForm
import qrcode
from io import BytesIO
import base64

def cadastro(request):
    qr_code_base64 = None

    if request.method == "POST":
        form = MoradorForm(request.POST)
        if form.is_valid():
            morador = form.save()

            # Gerar QR Code
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(str(morador.token_qr))
            qr.make(fit=True)
            img = qr.make_image(fill="black", back_color="white")

            # Converter para base64
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            qr_code_base64 = base64.b64encode(buffer.getvalue()).decode()

            return render(request, "usuarios/cadastro_sucesso.html", {"qr_code": qr_code_base64})
    else:
        form = MoradorForm()

    return render(request, "usuarios/cadastro.html", {"form": form})

def login_qr(request):
    if request.method == 'POST':
        token = request.POST.get('token_qr')  # Token do QR
        try:
            morador = Morador.objects.get(token_qr=token)
            # Salvar dados do morador na sessão
            request.session['morador_id'] = morador.id
            request.session['morador_nome'] = morador.user.username
            request.session['morador_email'] = morador.user.email  # email para relatório
            return redirect('menu')  # substituir pelo menu da geladeira
        except Morador.DoesNotExist:
            return render(request, 'usuarios/login.html', {'erro': 'QR Code inválido'})
    return render(request, 'usuarios/login.html')