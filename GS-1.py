import random

usuarios = {}

def voltar():
    input(f'Clique ENTER para voltar: ')

def voltar_r():
    print("""
Se quiser fazer mais registros digite 1
Se quiser voltar para o menu digite 2
""")
    opcao2 = int(input('Escolha uma opção: '))
    match opcao2:
        case 1:
            registro()
        case 2:
            menu()
        case _:
            print('\nOpção invalida')
            voltar()

def voltar_m():
    input(f'Clique ENTER para continuar: ')
    menu()

def continuar():
    input(f'Clique ENTER para continuar: ')
    main()

# --------------------------------------------------------------------------------------

def temperatura(temperatura):
    print("\n----------------------------------------------------\n")
    if temperatura < 15:
        print("Dicas de Pesca em Água Fria (Menor que 15°C):\n"
                "- Nessas águas você encontrará espécies como trutas e salmões.\n"
                "- Use anzóis sem farpa para reduzir lesões nos peixes.\n"
                "- Pratique o pesque e solte para manter as populações de peixes.\n"
                "- Fique atento às temporadas de desova e evite pescar nesses períodos.\n")
    elif 15 <= temperatura <= 21:
        print("Dicas de Pesca em Água Fresca (Entre 15°C e 21°C):\n"
                "- Nessas águas você encontrará espécies como o achigã e o walleye.\n"
                "- Use iscas e equipamentos sustentáveis para minimizar o impacto ambiental.\n"
                "- Siga as regulamentações e limites locais de pesca para evitar a sobrepesca.\n"
                "- Evite usar equipamentos de pesca à base de chumbo para prevenir a poluição da água.\n")
    elif 21 < temperatura <= 27:
        print("Dicas de Pesca em Água Morna (Entre 21°C e 27°C):\n"
                "- Nessas águas você encontrará espécies como o achigã e o bagre.\n"
                "- Pesque durante as partes mais frescas do dia para reduzir o estresse nos peixes.\n"
                "- Considere a saúde da população de peixes e pratique o pesque e solte.\n"
                "- Use equipamentos de pesca ecológicos e evite iscas de plástico.\n")
    elif temperatura > 50:
        print("Água acima de 50 GRAUS CELSIUS ??? \n")
    else:
        print("Dicas de Pesca em Água Tropical (Maior que 28°C):\n"
                "- Nessas águas você encontrará espécies como o tucunaré e o redfish.\n"
                "- Esteja ciente das áreas protegidas e evite pescar nessas zonas.\n"
                "- Apoie os esforços locais de conservação e participe de práticas de pesca sustentável.\n"
                "- Eduque os outros sobre a importância de preservar os ecossistemas marinhos.\n")
    # usuarios[usuario_atual]['temperatura'] = temperatura
    voltar()

# --------------------------------------------------------------------------------------

def quiz():
    perguntas = [
        ("\nQual é uma prática recomendada para pesca sustentável?\n", "a", ["a) Usar anzóis sem farpa", "b) Pescar durante a desova", "c) Usar equipamentos de chumbo\n"]),
        ("\nQual é a temperatura ideal para pescar trutas?\n", "c", ["a) Acima de 27 graus Celsius", "b) Entre 15 e 21 graus Celsius", "c) Abaixo de 15 graus Celsius\n"]),
        ("\nO que é pesque e solte?\n", "b", ["a) Capturar e cozinhar os peixes", "b) Prática de soltar os peixes após capturá-los", "c) Pescar sem anzóis\n"]),
        ("\nQual é a importância das reservas marinhas?\n", "a", ["a) Proteger habitats e espécies", "b) Aumentar a pesca comercial", "c) Reduzir a poluição das praias\n"]),
        ("\nQual é uma técnica sustentável de pesca?\n", "c", ["a) Pesca de arrasto", "b) Uso de redes de deriva", "c) Uso de armadilhas seletivas\n"]),
        ("\nPor que é importante conhecer a temperatura da água ao pescar?\n", "b", ["a) Para ajustar a isca", "b) Porque diferentes peixes preferem diferentes temperaturas", "c) Para saber quando é seguro nadar\n"]),
        ("\nQual é a consequência da sobrepesca?\n", "a", ["a) Diminuição das populações de peixes", "b) Aumento da biodiversidade", "c) Melhoria na qualidade da água\n"]),
        ("\nQual é uma prática de pesca que deve ser evitada para proteger a vida marinha?\n", "b", ["a) Pesca esportiva", "b) Pesca com explosivos", "c) Pesca com mosca\n"])
    ]

    random.shuffle(perguntas)    
    pontuacao = 0

    for pergunta, resposta_correta, opcoes in perguntas:
        print(f"\n----------------------------------------------------\n{pergunta}")
        for opcao in opcoes:
            print(opcao)
        resposta = input("Escolha a resposta correta: ")
        if resposta == resposta_correta:
            pontuacao += 1
    print(f"\nSua pontuação no quiz educativo foi: {pontuacao}/{len(perguntas)}\n")
    usuarios[usuario_atual]['pontuacao'] = pontuacao
    voltar()

# --------------------------------------------------------------------------------------

def registro():
    print("\n\n>>> Registro <<<")
    while True:
        usuario = input("\nDigite um nome de usuário: ").strip()
        if usuario in usuarios:
            print("\nEsse nome já foi cadastrado. Tente outro.\n")
        else:
            break
    senha = input("\nDigite uma senha: ").strip()
    usuarios[usuario] = {'senha': senha, 'temperatura': None, 'pontuacao': None}
    print(f"\nUsuário {usuario} registrado com sucesso!\n")
    voltar_r()

def login():
    global usuario_atual
    print("\n\n>>> Login <<<")
    usuario = input("\nDigite seu nome de usuário: ").strip()
    if usuario not in usuarios:
        print("\nNome de usuário não encontrado.\n")
        voltar()
        return False
    
    senha = input("\nDigite sua senha: ").strip()
    if usuarios[usuario]['senha'] == senha:
        usuario_atual = usuario
        print(f"\nBem-vindo, {usuario}!\n")
        continuar()
        return True
    else:
        print("\nSenha incorreta.\n")
        voltar()
        return False

# --------------------------------------------------------------------------------------

def conta():
    print("\n>>> MINHA CONTA <<<")
    usuario = usuario_atual
    senha = usuarios[usuario_atual]['senha']
    temperatura = usuarios[usuario_atual]['temperatura']
    pontuacao = usuarios[usuario_atual]['pontuacao']

    # Exibir informações da conta
    print(f"\nUsuário: {usuario}")
    print(f"Senha: {'*' * len(senha)}")
    print(f"\nTemperatura da sua Água: {temperatura}°C" if temperatura is not None else "Temperatura da sua Água: Nenhuma")
    print(f"Última Pontuação do Super Quiz: {pontuacao}/8\n" if pontuacao is not None else "Última Pontuação do Super Quiz: Nenhuma\n")
    
    voltar()

# --------------------------------------------------------------------------------------

def menu():
    while True:
        print("""

>>> MENU RÁPIDO <<<
              
- Digite o número do sistema que você deseja acessar!
            
1 - Registro
2 - Login
3 - Finalizar Programa
""")
        opcao = int(input('Escolha uma opção: '))
        match opcao:
            case 1:
                registro()
            case 2:
                if login():
                    main()
            case 3:
                print("""
Programa Finalizado
""")
                break
            case _:
                print('\nOpção invalida')

# --------------------------------------------------------------------------------------

def main():
    while True:
        print("""

----------------------------------------------------

>>> MENU COMPLETO <<<

- Tudo oque você fizer aqui ficará
salvo na sua conta :)
              
- Digite o número do sistema que 
você deseja acessar!
              
________________________________________________________
1 - SUPER QUIZ
________________________________________________________
2 - Dicas de Pesca
  ↳ receba dicas de acordo com a temperatura da água 
________________________________________________________
3 - Minha Conta
  ↳ veja informações relevantes sobre a sua conta
________________________________________________________
4 - Logout
________________________________________________________
""")
        opcao = int(input('Escolha uma opção: '))
        match opcao:
            case 1:
                quiz()
            case 2:
                n = int(input('\nTemperatura da Água em °C: '))
                if n > 50:
                    temperatura(n)
                    break
                print("\n>>> Essa é a temperatura da água em que você costuma pescar?\n"
                      "\nDigite 1 para SIM"
                      "\nDigite 2 para NÃO\n")
                opcao2 = int(input('Escolha uma opção: '))
                match opcao2:
                    case 1:
                        usuarios[usuario_atual]['temperatura'] = n
                    case 2:
                        temperatura(n)
                        break
                temperatura(n)
            case 3:
                conta()
            case 4:
                print("""
Você saiu da sua conta.
""")
                voltar_m()
                break
            case _:
                print('opção invalida')

menu()
