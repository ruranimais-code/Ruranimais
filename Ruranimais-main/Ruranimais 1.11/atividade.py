import time

while True:
    ###MENU###
    print ("")
    print ("oioi! quer ir pra qual questão?")
    opcao = int(input ("(coloque número de 1 a 18)"))
    while 1>opcao or opcao>18:
        print ("questao n existe :<")
        opcao = int(input ("(coloque número de 1 a 18)"))

    if opcao == 1:
    ###LIMPEZA E TRANSFORMÇÃO###
    #01. strip()
    #> SE = sem espaço
        #A) nome
        print ("")
        print ("#01. strip")
        print ("")
        nome = input ("digite seu nome :p")
        nomeSE = nome.strip()
        print (f"oi {nomeSE}!")

        #B) termo de busca
        print ("")
        time.sleep(1)
        termo = input (f"{nomeSE}, o que você procura?")
        termoSE = termo.strip()
        time.sleep(1)
        print (f"você procurou por {termoSE}...")
        print (f"mas o verdadeiro {termoSE} foram os amigos que fizemos no caminho!")
        time.sleep(2)
    
    elif opcao == 2:
    #02. lower()
    #> MIN = minúsculo
        #A) converter para letras minúsculas
        print ("")
        print ("02. lower")
        print ("")
        comando = input ("se desejar sair, digite (sair, Sair ou SAIR)")
        comandoMIN = comando.lower()
        if comandoMIN == "sair":
            print ("usuário deseja sair...")
            print ("tchau tchau ToT")
        else:
            print ("você não quer sair então??")
            time.sleep(1)
            print ("ebaa! vou cantar de felicidade :D")
            time.sleep(1)
            print ("lalalalalalalalalalalalalalala")
            time.sleep(1)
            print ("lalalalalalalala")
            time.sleep(2)
            print ("lala...")
            time.sleep(3)
            print ("cansei. tchau.")

        #B) email
        time.sleep(1)
        print ("mas espera! antes de você ir...")
        email = input ("me diz seu email por favor!")
        while "@" not in email or ".com" not in email:
            print ("isso não é um email!")
            email = input ("me diz seu email por favor!")
        if "@" in email and ".com" in email:
            emailMIN = email.lower()
            time.sleep(1)
            print (f"{emailMIN}...")
            print (f"nossa... {emailMIN}... que email lindo...")
            time.sleep(1)
            print ("agora sim, tchau :<")
            time.sleep(2)

    elif opcao == 3:
    #03. upper()
    #> MAI = maiúsculo
        #A) código de produto
        print ("")
        print ("03. upper")
        print ("")
        codigo = input ("digite código do produto !")
        codigoMAI = codigo.upper()
        print (f"código: {codigoMAI}")

        #B) estado
        print ("")
        estado = input ("agora que você disse o código, me diz um estado (sigla)")
        while len(estado) > 2 or len(estado) < 2:
            print ("isso não é uma sigla!")
            estado = input ("me diz um estado (sigla)")
        if len(estado) == 2:
            estadoMAI = estado.upper()
            print (f"seu produto ({codigoMAI}) será entregue em {estadoMAI} :D")
            time.sleep(2)

    elif opcao == 4:
    #04. title()
    #> comp = completo
    #> CAP = capitalizado
        #A) nome completo
        print ("")
        print ("04. title")
        print ("")
        print ("ei! você!")
        nomecomp = input ("me diz seu nome completo!")
        nomeCAP = nomecomp.title()
        print (f"{nomeCAP}! você recebeu a missão importantíssima de criar um evento!")

        #B) nome do evento
        evento = input ("me diz o nome do evento!")
        eventoCAP = evento.title()
        time.sleep(1)
        print (f"{eventoCAP}... perfeito!")
        time.sleep(1)
        print ("o convite está sendo enviado para todo o mundo...")
        time.sleep(1)
        print ("ele diz...")
        time.sleep(1)
        print (f"'{nomeCAP} lhe convida para participar de {eventoCAP}! vai ser o melhor evento da face da terra!'")
        time.sleep(2)

    elif opcao == 5:
    #05. replace()
    #> T = tratado
        #A) telefone
        print ("")
        print ("05. replace")
        print ("")
        print ("licença... o///o você... você me passaria seu telefone? >///<")
        cll = input ("seria bem legal se vc seguisse o formato (XXXXX-XXXX)...")
        while "-" not in cll:
            cll = input (">.< segue o formato por favor!")
        if "-" in cll:
            cllT = cll.replace ("-", "")
            time.sleep (1)
            print (f"{cllT}? 0///.///0 m-muito obrigado..!")
            time.sleep(2)

        #B) número com vírgula
        print (">///< aliás!")
        time.sleep(1)
        pao = input ("você saberia dizer o preço do pão? (ex:19,90)")
        while "," not in pao:
            print ("hmm... isso não parece certo :<")
            pao = input ("que tal seguir o exemplo?")
        if "," in pao:
            paoT = pao.replace (",", ".")
            print (f"nossa, {paoT}?! que caro!! O.o")
            time.sleep(2)

    elif opcao == 6:
    #06. split()
         #A) ler nome, cidade e idade e separar
         #> SEP = separados
         #> c_(x) = campo (x)
        print ("")
        print ("06. split")
        print ("")
        print ("espere! antes de ver o resto, preciso saber quem você é!")
        time.sleep(1)
        campos = input ("insira nome, idade e cidade (nessa ordem e separando com vírgula!)")
        while "," not in campos:
            print ("isso não tá certo!")
            campos = input ("insira nome, idade e cidade (nessa ordem e separando com vírgula!)")
        if "," in campos:
            camposSEP = campos.split (",")
            c_nome = camposSEP[0].strip()
            c_idade = camposSEP[1].strip()
            c_cidade = camposSEP[2].strip()
            print ("c_nome")
            print ("c_idade")
            print ("c_cidade")
            time.sleep(1)
            print (f"então você é {c_nome}, {c_idade}, de {c_cidade}?")
            time.sleep(1)
            print ("okay então :3")
            time.sleep(1)

        #B) ler dados e separar em lista de termos
        print ("agora que se identificou, você pode fazer uma lista :D")
        dados = input ("só lembre de separar por com vírgula!")
        while "," not in dados:
            print ("isso não tá certo!")
            dados = input ("separe com vírgula!)")
        if "," in dados:
            dadosSEP = dados.split (",")
            time.sleep(1)
            print (f"sua lista: {dadosSEP}")
            print (f"quantidade de items: {len(dadosSEP)}")
            time.sleep(2)

    elif opcao == 7:
    ###COMPOSIÇÂO, BUSCA E IDENTIFICAÇÃO###
    #07. join()
         #A) lista em uma linha só
         #> 7 = variável referente à questão 7
        print ("")
        print ("07. join")
        print ("")
        nomes7 = input ("digite os nomes dos integrantes da equipe (e separe com vírgula!)")
        while "," not in nomes7:
            print ("isso não tá certo!")
            nomes7 = input ("separe com vírgula!)")
        if "," in nomes7:
            nomes7T = nomes7.split(",")
            lista = ";    ".join(nomes7T)
            time.sleep(1)
            print (f"membros da equipe são: {lista}")
            time.sleep(1)

        #B) exibir caminho?
        entrada7 = input ("que caminho você andou (separe com vírgula!)?")
        while "," not in entrada7:
            print ("isso não tá certo!")
            entrada7 = input ("separe com vírgula!)")
        if "," in entrada7:
            entrada7T = entrada7.split(",")
            caminho7 = " > ".join(entrada7T)
            time.sleep(1)
            print (f"caminho percorrido: {caminho7}")
            time.sleep(2)


    elif opcao == 8:
    #08. count()
         #A) quantas letras "a" na frase
         #> QUANT = quantidade
        print ("")
        print ("08. count")
        print ("")
        print ("eiei, vamos conversar!")
        frase = input ("diz qualquer coisa! ^u^")
        fraseQUANT = frase.count ("a")
        time.sleep(1)
        print (f"você sabia?? você disse 'a' {fraseQUANT} vezes!! você sabia disso??")
        time.sleep(1)

        #B) quantas vezes "erro" aparece na frase
        print ("de novo! dessa vez eu vou contar uma palavra surpresa ;p")
        erro = input ("diz qualquer coisa de novo!!")
        erroQUANT = erro.count ("erro")
        time.sleep(1)
        print ("a palavra surpresa que eu tava contando era erro!!")
        time.sleep(1)
        print (f"parece que ela apareceu {erroQUANT} vezes na frase o.o")
        time.sleep(2)

    elif opcao == 9:
    #09. startswith()
         #A) verificar se input começa com "/"
        print ("")
        print ("09. startswith")
        print ("")
        print ("eiei, tenta digitar um comando do minecraft!")
        comando = input ("(dica, eles começam com '/'!)")
        while comando.startswith ("/") == False:
            print ("isso não parece um comando do minecraft...")
            comando = input ("que tal tentar novamente com '/' no início?")
        if comando.startswith ("/"):
            print ("uou!! como você é sabido!!")
            time.sleep(1)
            print ("eu nem sei o que isso faz :O")
            time.sleep(1)

        #B) verificar se input começa com "PROD"
        print ("dessa vez alguma coisa que começa com 'PROD'!")
        time.sleep (1)
        print ("por que?")
        time.sleep (1)
        print ("porque eu quero! :>>")
        time.sleep(1)
        comando2 = input ("agora tenta colocar alguma coisa que começa com 'PROD'!")
        while comando2.startswith ("PROD") == False:
            print ("seria muito legal se você fizesse oq eu pedisse...")
            time.sleep(1)
            print ("vamos tentar de novo!")
            comando2 = input ("diz qualquer coisa que começa com 'PROD' por favor ://")
        if comando2.startswith ("PROD"):
            print ("que legal!! eu não sei porque pedi pra você fazer isso :p")
            time.sleep(1)
            print ("byebyeeee :pppp")
            time.sleep(2)

    elif opcao == 10:
    #10. endswith()
         #A) verificar se arquivo termina com ".csv"
         #> AR = arquivo
         #> IN = institucional
        print ("")
        print ("10. endswith")
        print ("")
        print ("pss, me diz o nome de um arquivo!")
        nomeAR = input ("(mas tem que terminar com '.csv', ok?)")
        while nomeAR.endswith (".csv") == False:
            time.sleep(1)
            print ("ei!! tem que terminar com '.csv'!")
            time.sleep(1)
            print ("vou pedir de novo >:((")
            time.sleep(1)
            nomeAR = input ("nome do arquivo com '.csv' no final!")
        if nomeAR.endswith (".csv"):
            print ("ebaa!!")
            time.sleep(1)
            print (f"eu acho {nomeAR} um nome muito legal pra um arquivo :3")
            time.sleep(1)

        #B) verificar se email institucional termina com "@ufrpe.br"
        print ("que tal me dizer seu email institucional agora?")
        emailIN = input ("(dica: é o que termina com @ufrpe.br...)")
        while emailIN.endswith ("@ufrpe.br") == False:
            print ("grr...!! isso não é um email institucional!! >:ddd")
            time.sleep(1)
            emailIN = input ("pode não ser o seu, mas me diz um email institucional!!")
        if emailIN.endswith ("@ufrpe.br"):
            print ("hehehe... agora só preciso da senha pra fazer login no SIGAA >:D")
            time.sleep(2)

    elif opcao == 11:
    #11. find()
         #A) informar posição de "@"
         #> 11 = variável referente à questão 11
         #> PO = posição
        print ("")
        print ("11. find")
        print ("")
        email11 = input ("se você me disser um email, eu te conto um segredo...")
        while "@" not in email11 or ".com" not in email11:
            print ("pra eu te contar o segredo tem que ser um email de verdade :<")
            email11 = input ("vaivai, me diz um email!")
        if "@" in email11 or ".com" in email11:
            emailPO = email11.find ("@")
            time.sleep(1)
            print (f"o segredo é que '@' aparece na posição {emailPO} do seu email :DD")
            time.sleep(1)

        #B) informar posição de ":"
        print ("deixa eu te contar outro segredo...")
        segredo11 = input ("escreve alguma coisa, mas inclui ':'...")
        while ":" not in segredo11:
            time.sleep(1)
            segredo11 = input ("ei! eu te disse que precisa ter ':'! :<<")
        if ":" in segredo11:
            segredoPO = segredo11.find (":")
            print (f"o segundo segredo é que ':' aparece na posição {segredoPO} nisso ai :p")
            time.sleep(2)

    elif opcao == 12:
    #12. isalpha()
         #A) ler nome e verificar se tem apenas letras
         #> AL = alpha
        print ("")
        print ("12. isalpha")
        print ("")
        nomeAL = input ("oioi!! me diz seu nome!!")
        time.sleep(1)
        while nomeAL.isalpha == False:
            print ("esse não é seu nome, porque você mentiu?? :((")
            time.sleep (1)
            print ("a lei não permite caracteres especiais na certidão de nascimento! é considerado constrangedor/vexatório!")
            nomeAL = input ("eu só quero saber seu nome :<")
        if nomeAL.isalpha():
            print (f"prazer te conhecer {nomeAL}!!")
            print ("seu nome é muito bonito :D")
            time.sleep(1)

        #B) validar categoria
        categoriaAL = input (f"{nomeAL}, me diz alguma coisa que você gosta de fazer!")
        while categoriaAL.isalpha == False:
            print ("eu só consigo entender letras T^T")
            time.sleep(1)
            categoriaAL = input ("repete por favor?? :<")
        if categoriaAL.isalpha:
            print (f"nossa, {categoriaAL}? que legal!")
            print (f"{nomeAL}, eu nunca conheci alguém que gostava de {categoriaAL}...")
            time.sleep(2)
            print (f"{nomeAL}...")
            time.sleep(2)
            print ("foi muito bom falar com você, mas agora eu tenho que ir!! ToT")
            print (f"adeus, {nomeAL}!!")
            time.sleep(2)


    elif opcao == 13:
    ###VALIDAÇÃO E FORMATAÇÃO###
    #13. isdigit()
         #A) ler opção de menu e verificar se contém apenas dígitos/converter para inteiro
         #> 13 = variável referente à questão 13
         #> INT = inteiro
        print ("")
        print ("13. isdigit")
        print ("")
        print ("1. feijão")
        print ("2. arroz")
        print ("3. feijão")
        print ("4. prato")
        opcao13 = input ("?")
        while opcao13.isdigit == False:
            opcao13 = ("você tem que escolher um número!")
        if opcao13.isdigit():
            opcaoINT = int(opcao13)
            print (f"você disse opção {opcaoINT}??")
            time.sleep
            print ("1, 2 feijão com arroz!")
            time.sleep(1)
            print ("3, 4 feijão no prato!")
            time.sleep(1)
            print ("5, 6 falar inglês!")
            time.sleep(1)
            print ("7, 8 comer biscoito!")
            time.sleep
            print ("9, 10 comer pastéis!!! :DDDDD")
            time.sleep (1)

        #B) ler idade/validar se contém apenas números
            print ("eita!! esqueci de perguntar sua idade!")
            idade13 = input ("eai? me diz usando os dígitos dos números por favor o.o")
            while idade13.isdigit == False:
                print ("não!! eu não sei ler isso...")
                idade13 = input ("use algarismos por favor :<<")
                time.sleep (1)
                if idade13.isdigit():
                    if 100>idade13:
                        print (f"{idade13} aninhos?")
                        time.sleep(1)
                        print ("não sei por que perguntei isso, na verdade...")
                        time.sleep(1)
                        print ("hmm... tchauzinho então!" \
                        "time.sleep(2)")
                    elif idade13<100:
                        print ("nossa!!!!!")
                        time.sleep (1)
                        print ("então você tava lá com os dinossauros? :OO")
                        print ("fico com vergonha de falar com uma pessoa tão sênior! o///o tchau!!")
                        time.sleep(2)
                    elif idade13<-1:
                        print ("eu não sei como isso é possível e também não sei como me sinto sobre...")
                        time.sleep (1)
                        print ("vou dizer tchau antes de pensar demais sobre e sobreaquecer :p")
                        time.sleep(2)

    elif opcao == 14:
    #14. isalnum()
         #A) ler código de acesso/verificar se contém apenas letras e números
        print ("")
        print ("14. isalnum")
        print ("")
        print ("você devia criar uma senha...")
        senha = input ("só use letras e números por favor!")
        while senha.isalnum == False:
            print ("senha não pode conter espaços ou caracteres especiais :<")
            senha = input ("tente novamente por favor!")
        if senha.isalnum():
            print ("ebaaa! senha criada com sucesso :D")
            time.sleep(1)

        #B) ler identificador e aceitar somente se alfanumérico
        print ("hmm... parece que você tem uma encomenda a caminho?")
        time.sleep(1)
        print ("você tem algum identificador de produto?")
        identificador = input ("se sim, me diz que eu posso te ajudar com o rastreamento!")
        while identificador.isalnum == False:
            print ("um identificador só é válido se tiver apenas letras e números >.<")
            identificador = input ("tenta novamente sem espaços ou caracteres especiais!")
        if identificador.isalnum():
            time.sleep(1)
            print (f"{identificador}, é?")
            time.sleep(1)
            print ("hehehe... eu vou roubar a sua encomenda agora!! >:))")
            time.sleep(2)

    elif opcao == 15:
    #15. isspace()
         #A)
        print ("")
        print ("15. isspace")
        print ("")
        print ("oi!")
        time.sleep (1)
        print ("")
        print ("oioi, eu disse oi!")
        time.sleep (2)
        print ("")
        print ("...")
        time.sleep (3)
        print ("")
        print ("ei!! T.T")
        time.sleep (2)
        print ("")
        vazio = input ("para de me ignorar!! ToT")
        while vazio.isspace == False:
            print ("ufa!! pensei que você não ia me responder!!")
            time.sleep(2)
            print ("")
            vazio = input ("ei?? você ainda tá ai??? :<<<<<<")
        if vazio.isspace():

        #B) ler espaço e detectar se contém apenas espaços/tratar como vazia
            print ("vou te dar uma última chance de me responder!")
            vazio2 = input ("charlie charlie você está ai?")
            if vazio2.isspace == False:
                time.sleep(1)
                print ("")
                print ("também não ligo mais! agora eu que vou ignorar você!")
                time.sleep(2)
            elif vazio2.isspace():
                time.sleep(2)
                print ("")
                print ("você me machucou muito fazendo isso TToTT adeus!!")
                time.sleep(2)

    elif opcao == 16:
    #16. isupper()
         #A) ler sigla e verificar se letras são maiúsculas
         #> CAT = categoria
        print ("")
        print ("16. isupper")
        print ("")
        print ("insira uma sigla por favor :3")
        sigla = input ("(tem que ser em letras maiúsculas!)")
        while sigla.isupper == False:
            sigla = input ("faz o que eu pedi por favor :<")
        if sigla.isupper():
            time.sleep(1)
            print (f"ebaa! {sigla}!!")
            time.sleep(1)
            print ("que sigla legal :OO")
            time.sleep(1)

        #B) ler código (em letras maiúsculas) e informar se formato está certo
        print ("inclusive, isso me lembrou algo...")
        time.sleep(1)
        print ("você devia ter um código :p")
        codigoCAT = input ("me diz por favor (usando capslock)?")
        while codigoCAT.isupper == False:
            print ("grr! isso não foi o que eu pedi!")
            codigoCAT = input ("o código tem que estar todo em letras maiúsculas!!")
        if codigoCAT.isupper():
            print ("ebaa!! obrigado por seguir a formatação correta!! ^u^")
            time.sleep(1)
            print ("por conta de pessoas como você, o mundo é um lugar melhor...")
            time.sleep(2)

    elif opcao == 17:
    #17. islower()
         #A) ler comando em letras minúsculas e validar formato
         #> LOW = mesma coisa que MIN mas pra essa questão especificamente
        print ("")
        print ("17. islower")
        print ("")
        print ("você pode me dizer qualquer coisa,")
        coisa = input ("mas só pode usar lowercase, ok? :>")
        while coisa.islower == False:
            print ("eu disse só letras minúsculas T.T")
            coisa = input ("vou te dar outra chance.. pode me dizer qualquer coisa...")
        if coisa.islower():
            print (f"O.O nossa! {coisa}...")
            time.sleep(1)
            print ("vou pensar bastante nisso!")
            time.sleep(1)

        #B) ler nome e verificar se letras estão minúsculas
        print ("inclusive, gostaria de saber seu nome :3")
        nomeLOW = input ("poderia me dizer (em letras minúsculas)?")
        while nomeLOW.islower == False:
            print ("e-eu só consigo entender letras minúsculas!! :<<")
            nomeLOW = input ("pode reptir..?")
        if nomeLOW.islower():
            print (f"{nomeLOW}, foi um prazer conversar com você sobre {coisa}!")
            time.sleep(1)
            print ("até uma outra vez!!")
            time.sleep(2)

    elif opcao == 18:
    #18. zfill()
         #A) ler senha  e exibir sempre com 5 dígitos, completando com 0 à esquerda
        print ("")
        print ("18. zfill")
        print ("")
        print ("insira o número da sua senha de atendimento :p")
        atendimento = input ("usar apenas dígitos por favor!")
        senhaT = atendimento.zfill(5)
        print (f"okay, se sua senha é #{senhaT}...")
        time.sleep(1)

        #B) número de nota/pedido e exibir sempre com 8 dígitos, completando com 0 à esquerda
        print ("ah!")
        time.sleep(1)
        print ("parece que você tem alguns pedidos!")
        pedidos = input ("se quiser verificar algum, pode me dizer o código :3")
        pedidosT = pedidos.zfill(8)
        time.sleep(1)
        print ("deixa eu olhar...")
        time.sleep(2)
        print (f"parece que seu pedido #{pedidosT} está a caminho! ^.^")
        time.sleep(2)