from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import contatoForm
from .forms import LoginForm
from .forms import FreelancerForm
from .models import Login
from .models import Contato
from .models import Freelancer
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from django.template import Context, loader
####
#class Session():
#	def __init__ (self):
#		self.ativo= False
##	def setAtivo(self, ativo):
#		self.ativo = ativo
#	def getAtivo(self):
#		return self.ativo

def freelancer_home(request):

	if(True):
		context = {
			"nome": "Wildyson"
		}
		return render(request,'login/freelancer.html', context)
	return redirect('home')

def cadastro(request):
	
	context = {
		"nome": "aloo"
	}
	
	form = FreelancerForm(request.POST) 
	
	if(request.method == 'POST'):
		
		if form.is_valid():
			instance = form.save(commit=False)
			instance.NotaAvaliativa = 0
			print(instance.Email)
			instance.save()

			print("valido")
			return HttpResponse(" DADOS CADASTRADOS")
		else:
			print form.errors, len(form.errors)
			print("invalido")

	return render(request,'login/cadastro.html', context)

def contato(request):
	form = contatoForm(request.POST)
	if(request.method == 'POST'):
		if form.is_valid():  
			form.save()
			return HttpResponse("THANKS")
		else:
			print("Formulario nao e valido")
	return render(request,'login/contato.html', {})
	
def home(request):
	title = ""
	login= Login.objects.all()

	form = LoginForm(request.POST)
	context = {
		"form": form,
		"title": title
	}
	if(request.method == 'POST'):	
		if form.is_valid():
			instance = form.save(commit=False)
			for lg in login:
				#print(lg.login_email)
				if ((instance.login_email == lg.login_email) and (instance.login_senha == lg.login_senha)):
					#instance.save()
					context = {
						"title": "Login Efetuado"
					}
					
					return redirect('freelancer_home')
			context = {
				"form": form,
				"title": "Login Invalido"
			}
	return render(request,'login/index.html', context )

# Create your views here.
