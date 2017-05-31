from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import contatoForm, LoginForm, FreelancerForm, PessoaFisicaForm, PessoaJuridicaForm, ClienteForm
from .models import Login, Contato, Freelancer, PessoaFisica, PessoaJuridica, Cliente
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
	
	if(request.method == 'POST'):
		if(request.POST.get('selectbasic', False) == "1"):
			form = FreelancerForm(request.POST) 
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
		else:
			form = ClienteForm(request.POST)
			if form.is_valid():
				instance = form.save(commit=False)
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
			return HttpResponse("Mensagem Enviada")
		else:
			print("Formulario nao e valido")
			print form.errors, len(form.errors)
	return render(request,'login/contato.html', {})
	
def home(request):
	title = ""
	freelancer= Freelancer.objects.all()

	form = LoginForm(request.POST)
	context = {
		"form": form,
		"title": title
	}
	if(request.method == 'POST'):	
		if form.is_valid():
			instance = form.save(commit=False)
			for f in freelancer:
				#print(lg.login_email)
				if ((instance.login_email == f.Email) and (instance.login_senha == f.Senha)):
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
