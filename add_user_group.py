nome_do_usuario = str(input("Digite o nome do usuário a ser inserido no grupo: "))
nome_do_grupo = input("Digite o nome do grupo? ")
comando_adicionar_ao_grupo = "oc adm policy add-user "

if nome_do_usuario and nome_do_grupo:      
    comando_adicionar_ao_grupo += nome_do_grupo
    comando_adicionar_ao_grupo += " "
    comando_adicionar_ao_grupo += nome_do_usuario
          
    print("Usuário '{}' adicionado ao grupo '{}'.".format(nome_do_usuario,nome_do_grupo))        
                       
else:
    print("Script encerrado. Nome do grupo e nome do user não podem estar vazios")       




