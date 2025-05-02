## Planejamento

Estes são os requisitos do sistema:

### Requisitos da atividade

1. O sistema deve usar a linguagem Python.
2. O sistema deve usar apenas estruturas condicionais, de repetição e sequências.

### Requisitos funcionais

1. O sistema deve permitir a operações de criação, leitura, atualização e remoção de tarefas.
2. As tarefas serão categorizadas em "Completo", "Em andamento" e "Para fazer".
3. Para cada tipo de tarefa, será implementado uma lista.
4. Não podem ser inseridas tarefas completas, apenas "Para fazer" ou "Fazendo".
5. Deve ser implementado uma funcionalidade para completar tarefas.
6. Deve ser implementado uma funcionalidade para colocar tarefas "Para fazer" em "Fazendo".
6. Tarefas com o mesmo nome não podem existir em listas diferentes, apenas no caso de ela estar completa e a nova tarefa estar para fazer. Nesse caso, a tarefa completa irá ser deletada. (Requisito necessário para o caso de tarefas cíclicas, rotineiras)

## Funcionamento

O sistema será implementado em um só loop, que, enquanto o usuário não digitar "sair", continuará perguntando por instruções. Dentro desse loop, são implementas condicionais que irão realizar uma operação caso sejam condizentes com o comando de entrada. 

1. Para o caso de inserção, o usuário deverá prover um nome e um tipo de tarefa e a inserção só irá ocorrer após uma validação destes dados.
2. Para o caso de atualização, o usuário deverá prover um nome e a atualização ocorrerá após uma validação das condições dos requisitos.
3. Para o caso de leitura, o usuário pode escolher quais listas ele quer imprimir na tela por meio de um input que será validado.
4. Para o caso de deleção, será pedido do usuário um nome, e a deleção ocorrerá após esse nome ser validado.
5. Para o caso de compleção ou de execução de uma tarefa, o procedimento será o mesmo de uma alteração.
