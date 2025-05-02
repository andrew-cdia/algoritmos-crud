parafazer = []
fazendo = []
completo = []

while True:
    comando = input("Digite um comando (Adicionar, Excluir, Alterar, Ver, Sair): ").strip().lower()

    if comando == "adicionar":
        tarefa = input("Nome da tarefa: ").strip()
        tipo = input("Tipo (Para Fazer, Fazendo): ").strip().lower()

        if tipo == "para fazer":
            if tarefa in parafazer or tarefa in parafazer:
                print("Tarefa já existe")
                continue
            elif tarefa in completo:
                completo.remove(tarefa)
            parafazer.append(tarefa)
        elif tipo == "fazendo":
            if tarefa in fazendo or tarefa in parafazer:
                print("Tarefa já existe")
                continue
            elif tarefa in completo:
                completo.remove(tarefa)
            fazendo.append(tarefa)
        elif tipo == "completo":
            print("Não se pode inserir tarefas completas!")
        else:
            print("Tipo inválido")
    elif comando == "excluir":
        tarefa = input("Nome da tarefa: ").strip()

        if tarefa in parafazer:
            parafazer.remove(tarefa)
        elif tarefa in fazendo:
            fazendo.remove(tarefa)
        elif tarefa in completo:
            completo.remove(tarefa)
        else:
            print("Esta tarefa não foi encontrada!")
    elif comando == "alterar":
        operacao = input("Tipo de alteração (Fazer, Completar, Alterar): ").strip().lower()
        tarefa = input("Nome da tarefa: ").strip()

        if operacao == "fazer":
            if not tarefa in parafazer:
                print("Esta tarefa não está para fazer.")
                continue
            parafazer.remove(tarefa)
            fazendo.append(tarefa)

        elif operacao == "completar":
            if (not tarefa in parafazer) and (not tarefa in fazendo):
                print("Esta tarefa não está para fazer ou sendo feita.")
                continue
            parafazer.remove(tarefa) if tarefa in parafazer else fazendo.remove(tarefa)
            completo.append(tarefa)

        elif operacao == "alterar":
            if tarefa in parafazer:
                parafazer.insert(parafazer.index(tarefa), input("Novo nome: "))
            elif tarefa in fazendo:
                fazendo.insert(fazendo.index(tarefa), input("Novo nome: "))
            elif tarefa in completo:
                completo.insert(completo.index(tarefa), input("Novo nome: "))
            else:
                print("Esta tarefa não foi encontrada!")

        else:
            print("Operação inválida!")
        
    elif comando == "ver":
        listas = input("Quais listas deseja imprimir? (Para fazer, Fazendo, Completo): ").lower()

        if "para fazer" in listas:
            print("Para Fazer:")
            for indice, item in enumerate(parafazer):
                print(f"{indice + 1} - {item}")
            print()
        if "fazendo" in listas:
            print("Fazendo:")
            for indice, item in enumerate(fazendo):
                print(f"{indice + 1} - {item}")
            print()
        if "completo" in listas:
            print("Completo:")
            for indice, item in enumerate(completo):
                print(f"{indice + 1} - {item}")
            print()
        
    elif comando == "sair":
        break
    else:
        print("Comando inválido!")

