from django import forms
from .models import Login
from .models import Contato
from .models import Freelancer
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
		
    		     