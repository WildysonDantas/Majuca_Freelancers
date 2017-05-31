from django import forms
from .models import Login
from .models import Contato
from .models import Freelancer
from .models import Cliente, PessoaFisica, PessoaJuridica
#forms.CharField(label="", widget = forms.passwordInput())
class LoginForm(forms.ModelForm):	
	class Meta:
		model = Login
		fields = ['login_email', 'login_senha']

class contatoForm(forms.ModelForm):	
	class Meta:
		model = Contato
		fields = ['nome','data','Email', 'mensagem']
class FreelancerForm(forms.ModelForm):

	class Meta:
		model = Freelancer
		fields = ['Nome','Email','CPF','Endereco','Cidade','Estado','Agencia','Banco','Conta','Telefone','Senha','Especialidade','SobreMim']

class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = ['Nome','Email','Senha','Telefone']
class PessoaFisicaForm(forms.ModelForm):
	class Meta:
		model = PessoaFisica
		fields = ['CPF']
class PessoaJuridicaForm(forms.ModelForm):
	class Meta:
		model = PessoaJuridica
		fields = ['CNPJ']
