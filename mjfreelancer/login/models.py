from django.db import models
from django.utils import timezone
class Login(models.Model):
	login_email = models.CharField(verbose_name = "Email ", max_length = 50)
	login_senha = models.CharField(verbose_name = "Senha ",  max_length = 30)


class Contato(models.Model):

	

	Email = models.CharField(verbose_name = "Email ", max_length = 50)
	data = models.CharField(verbose_name = "Data ", max_length = 20)
	nome = models.CharField(verbose_name = "Nome ", max_length = 50)
	mensagem = models.CharField(verbose_name = "mensagem ", max_length=500)

# Create your models here.
class Cliente(models.Model):	
	Nome = models.CharField(max_length=70, blank=True)
	Email = models.EmailField(max_length=30, blank=True)
	Foto = models.CharField(max_length=100, null=True)
	Senha = models.CharField(max_length=30, blank=True)
	Telefone = models.IntegerField(blank=True,null=True)


class PessoaFisica(models.Model):
	CPF = models.IntegerField(blank=True, primary_key=True)
	fk_idCliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)

class PessoaJuridica(models.Model):
	CNPJ = models.IntegerField(blank=True, primary_key=True)
	Cliente =  models.ForeignKey('Cliente', on_delete=models.CASCADE)

class Freelancer(models.Model):
	Nome = models.CharField(max_length=70, blank=True)
	Email = models.EmailField(max_length=20, blank=True)
	Endereco = models.CharField(max_length=100, blank=True)
	Cidade = models.CharField(max_length=30, blank=True)
	Estado = models.CharField(max_length=20, blank=True)
	CPF = models.CharField(max_length=11, blank=True, unique=True)
	Agencia = models.CharField(max_length=6, blank=True)
	Banco = models.CharField(max_length=25, blank=True)
	Conta = models.CharField(max_length=10, blank=True)
	Telefone = models.CharField(max_length=10, blank=True)
	Senha = models.CharField(max_length=25, blank=True)
	Especialidade = models.CharField(max_length=150)
	SobreMim = models.CharField(max_length=150)
	NotaAvaliativa = models.IntegerField()
	Foto = models.CharField(max_length=100, null=True)

class Projeto(models.Model):
	Nome = models.CharField(max_length=70, blank=True)
	AreaProjeto =  models.CharField(max_length=70, blank=True)
	DataPublicacao = models.DateTimeField(blank=True, null=True)
	DataInicio = models.DateTimeField(blank=True, null=True)
	DataFim = models.DateTimeField(blank=True, null = True)
	Preco = models.FloatField(blank=True, null=True)
	Descricao = models.CharField(max_length=200, blank=True)
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,default=1)
	idFreelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE,default=1)

class Interessados_Projeto(object):
	fk_idFreelancer = models.ForeignKey('Freelancer', on_delete=models.CASCADE, primary_key=True,default=1)
	fk_idProjeto = models.ForeignKey('Projeto', on_delete=models.CASCADE, primary_key=True,default=1)

# Create your models here.
