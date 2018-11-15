from django.shortcuts import render,redirect,get_object_or_404
from .forms import FormularioOpinion
from .models import Opinion
# Create your views here.
def inicio(request):
	return render(request,'opiniones/index.html',{})

def listaOpiniones(request):
	opiniones = Opinion.objects.filter().order_by('curso')
	return render(request,'opiniones/listaOpiniones.html',{'opiniones':opiniones})
def comenzar(request):
	if request.method == 'POST':
		form = FormularioOpinion(request.POST)
		if  form.is_valid():
			opinion = form.save(commit=False)
			opinion.id_usuario = request.user
			#opinion.fechaPublicacion = timezone.now()
			opinion.save()
			
			return redirect('detalles',pk=opinion.pk)
	else:
		form = FormularioOpinion()
	return render(request, 'opiniones/nuevaOpinion.html',{'form':form})

def detalles(request,pk):
	opinion = get_object_or_404(Opinion,pk = pk)
	return render(request,'opiniones/detalles.html',{'opinion':opinion})

def modificar(request,pk):
	post = get_object_or_404(Opinion,pk=pk)
	if request.method == 'POST':
		form = FormularioOpinion(request.POST,instance=opinion)
		if  form.is_valid():
			opinion = form.save(commit=False)
			opinion.id_usuario = request.user
			opinion.save()
			return redirect('detalles',pk=opinion.pk)
	else:
		form = FormularioOpinion()
	
	return render(request, 'opiniones/editar.html',{'form':form})

