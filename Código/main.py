def main_crud():
    parafazer = []
    fazendo = []
    completo = []

    while True:
        comando = input("Digite um comando (Adicionar, Excluir, Alterar, Ver, Sair): ").lstrip().lower()

        if comando == "adicionar":
            tarefa = input("Nome da tarefa: ").lstrip()
            tipo = input("Tipo (Para Fazer, Fazendo): ").lstrip().lower()

            if tipo == "para fazer":
                parafazer.append(tarefa)
            elif tipo == "fazendo":
                fazendo.append(tarefa)
            elif tipo == "completo":
                print("Não se pode inserir tarefas completas!")
            else:
                print("Tipo inválido")
        elif comando == "excluir":
            tarefa = input("Nome da tarefa: ").lstrip()

            if tarefa in parafazer:
                parafazer.remove(tarefa)
            elif tarefa in fazendo:
                fazendo.remove(tarefa)
            elif tarefa in completo:
                completo.remove(tarefa)
            else:
                print("Esta tarefa não foi encontrada!")
        elif comando == "alterar":
            tarefa = input("Nome da tarefa: ").lstrip()
            operacao = input("Tipo de alteração (Fazer, Completar, Alterar): ").lstrip().lower()

            if operacao == "fazer":
                if not tarefa in parafazer:
                    print("Esta tarefa não está para fazer.")
                    continue
                fazendo.append(parafazer.pop(tarefa))

            elif operacao == "completar":
                if not (tarefa in fazendo and tarefa in parafazer):
                    print("Esta tarefa não está para fazer ou sendo feita.")
                    continue
                completo.append(fazendo.pop(tarefa))

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
                print("Para Fazer:")
                for indice, item in enumerate(fazendo):
                    print(f"{indice + 1} - {item}")
                print()
            if "completo" in listas:
                print("Para Fazer:")
                for indice, item in enumerate(completo):
                    print(f"{indice + 1} - {item}")
                print()
            
        elif comando == "sair":
            break
        else:
            print("Comando inválido!")