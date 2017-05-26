from django.contrib import admin
from mjfreelancer.login.models import Login
from mjfreelancer.login.models import Cliente, PessoaFisica, PessoaJuridica, Freelancer, Projeto, Interessados_Projeto
# Register your models here.
class LoginAdmin(admin.ModelAdmin):
	model = Login
	list_display = ['login_email', 'login_senha']
	search_fields = ['login_email']
	save_on_top = True
admin.site.register(Login, LoginAdmin)
admin.site.register(Cliente)
admin.site.register(PessoaJuridica)
admin.site.register(PessoaFisica)
admin.site.register(Freelancer)
admin.site.register(Projeto)
#admin.site.register(Interessados_Projeto)