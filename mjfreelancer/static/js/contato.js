function validar(){

				var verificaData = /^[0-9]{2}\/[0-9]{2}\/[0-9]{4}$/;

				if(document.cad.tNome.value == "" && document.cad.tEmail.value == "" && document.cad.dData.value == "" && document.cad.mensagem.value == ""){
					alert("Os campos de texto não podem estar vazios!");
					document.cad.tNome.focus();
					return false;
				}
				else if(document.cad.tNome.value == ""){
					alert("O campo de nome não pode ser vazio!");
					document.cad.tNome.focus();
					return false;
				}
				else if(document.cad.tEmail.value == ""){
					alert("O campo de email não pode ser vazio!");
					document.cad.tEmail.focus();
					return false;
				}
				else if(document.cad.dData.value == ""){
					alert("O campo para data de nascimento não pode ser vazio!");
					document.cad.dData.focus();
					return false;
				}
				else if(document.cad.mensagem.value == ""){
					alert("O campo de mensagem não pode ser vazio!");
					document.cad.mensagem.focus();
					return false;

				} else if(!verificaData.test(document.cad.dData.value)){
    				alert("Digite a data no formato Dia/Mês/Ano");
					document.cad.dData.focus();
				    return false;
				
				} else {
					alert("Dados enviados com sucesso! Em no máximo 48 horas você receberá uma resposta.");
					return true;
				}
			}
