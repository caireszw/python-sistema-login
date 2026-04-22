temp = dict()
banco = list()

while True:
    print('\n1 -> Cadastrar o Usuario')
    print('2 -> Fazer Login')
    print('3 -> Listar Usuarios')
    print('4 -> Sair')

    resp = int(input('Digite a opção desejada: '))

    if resp == 1:
        usuario_novo = input('Digite o nome do usuário: ').strip()
        senha_nova = input('Digite a senha: ').strip()

        if usuario_novo == '' or senha_nova == '':
            print('ERRO: usuário e senha não podem ser vazios!')
            continue

        existe = False

        for u in banco:
            if usuario_novo.lower() == u['Usuario'].lower():
                existe = True
                break

        if existe:
            print('ERRO: esse usuário já está cadastrado!')
        else:
            temp['Usuario'] = usuario_novo
            temp['Senha'] = senha_nova
            banco.append(temp.copy())
            temp.clear()
            print('Usuário cadastrado com sucesso!')

    elif resp == 2:
        usuario = input('Digite o login: ').strip()
        senha = input('Digite a senha: ').strip()

        encontrado = False

        for u in banco:
            if usuario.lower() == u['Usuario'].lower():
                encontrado = True
                if senha == u['Senha']:
                    print('Login realizado com sucesso!')
                else:
                    print('Senha incorreta!')
                break

        if not encontrado:
            print('Usuário não encontrado!')

    elif resp == 3:
        if len(banco) == 0:
            print('Nenhum usuário cadastrado.')
        else:
            print('\nUsuários cadastrados:')
            for u in banco:
                print(f'- {u["Usuario"]}')

    elif resp == 4:
        print('Encerrando sistema...')
        break

    else:
        print('OPÇÃO INVÁLIDA!')