from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def Inicio(request):
	print(request.user.username)
	if request.user.username == 'admin':
		return redirect('/agregarFeriante')
	else:
		return render(request,'start.html')


def  Administrador(request):
	return render(request, 'administrador.html')
