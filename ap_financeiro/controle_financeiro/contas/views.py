
from django.shortcuts import render, redirect, get_object_or_404
from .models import Transacao
from .forms import TransacaoForm
from django.contrib.auth.forms import UserCreationForm


def editar_transacao(request, pk):
    transacao = get_object_or_404(Transacao, pk=pk)
    if request.method == 'POST':
        form = TransacaoForm(request.POST, instance=transacao)
        if form.is_valid():
            form.save()
            return redirect('listar_transacoes')
    else:
        form = TransacaoForm(instance=transacao)
    return render(request, 'transacoes/editar.html', {'form': form, 'transacao': transacao})

def deletar_transacao(request, pk):
    transacao = get_object_or_404(Transacao, pk=pk)
    if request.method == 'POST':
        transacao.delete()
        return redirect('listar_transacoes')
    return render(request, 'transacoes/deletar.html', {'transacao': transacao})

def listar_transacoes(request):
    transacoes = Transacao.objects.filter(usuario=request.user)

    tipo = request.GET.get('tipo')
    categoria = request.GET.get('categoria')
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')

    if tipo:
        transacoes = transacoes.filter(tipo=tipo)
    if categoria:
        transacoes = transacoes.filter(categoria__icontains=categoria)
    if data_inicio and data_fim:
        transacoes = transacoes.filter(data__range=[data_inicio, data_fim])

    context = {
        'transacoes': transacoes,
        'filtros': {
            'tipo': tipo,
            'categoria': categoria,
            'data_inicio': data_inicio,
            'data_fim': data_fim
        }
    }
    return render(request, 'transacoes/listar.html', context)



def adicionar_transacao(request):
    if request.method == 'POST':
        form = TransacaoForm(request.POST)
        if form.is_valid():
            nova_transacao = form.save(commit=False)
            nova_transacao.usuario = request.user
            nova_transacao.save()
            return redirect('listar_transacoes')
    else:
        form = TransacaoForm()
    return render(request, 'transacoes/adicionar.html', {'form': form})

def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'transacoes/registrar.html', {'form': form})

