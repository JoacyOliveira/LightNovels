from django.shortcuts import render,redirect, get_object_or_404
from .models import Novel
from .forms import NovelForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.

def listarnovels(request):
    termo_busca = request.GET.get('pesquisa', None)
    ordenar = request.GET.get('ordenar',None)

    if termo_busca:
         novels = Novel.objects.all().filter(name__icontains=termo_busca, user=request.user)
         paginator = Paginator(novels, 5)
         page = request.GET.get('page')
         novels = paginator.get_page(page)
    else:
        if (ordenar == "andamento") or (ordenar == "concluido"):
            novels = Novel.objects.all().filter(status__icontains=ordenar, user=request.user)
        elif ordenar == "todos":
            novels = Novel.objects.all().filter(user=request.user)
        elif ordenar:
            novels = Novel.objects.all().order_by(ordenar).filter(user=request.user)
        else:
            if request.user.is_authenticated:
                novels = Novel.objects.all().filter(user = request.user)
                paginator = Paginator(novels, 5)
                page = request.GET.get('page')
                novels = paginator.get_page(page)
            else:
                novels = Novel.objects.all()
                paginator = Paginator(novels, 5)
                page = request.GET.get('page')
                novels = paginator.get_page(page)



    return render(request, 'mainlist_novels.html', {'novel': novels})

@login_required
def tablenovels(request):
    termo_busca = request.GET.get('pesquisa',None)
    if termo_busca:
        novels = Novel.objects.all().filter(name__icontains=termo_busca, user=request.user)
        paginator = Paginator(novels,20)
        page = request.GET.get('page')
        novels = paginator.get_page(page)
    else:
        novels = Novel.objects.all().filter(user=request.user)
        paginator = Paginator(novels,20)
        page = request.GET.get('page')
        novels = paginator.get_page(page)
    return render(request, 'table_novels.html',{'novel':novels})

@login_required
def salvar_novel(request):
    form = NovelForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        form = NovelForm(request.POST, request.FILES)
        if form.is_valid():
            novel = form.save(commit=False)
            novel.user = request.user
            novel.save()
            return redirect('painel')
    return render(request,'create_novel.html',{'form':form})

@login_required
def delete_novel(request,id):
    novel = get_object_or_404(Novel,pk=id)
    if request.method == 'POST':
        novel.delete()
        return redirect('painel')
    return render(request,'delete_novel.html',{'novel':novel})

@login_required
def update_novels(request,id):
    novel = get_object_or_404(Novel,pk=id)
    form = NovelForm(request.POST or None,request.FILES or None, instance=novel)
    if request.method == 'POST':
        form.save()
        return redirect('painel')
    return render(request,'update_novel.html',{'form':form})
