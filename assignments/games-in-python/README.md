
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Construir um jogo da forca em Python para praticar o uso de strings, listas, laços de repetição e condicionais. O aluno deverá criar uma experiência interativa em que o jogador tenta adivinhar uma palavra secreta antes de esgotar as tentativas.

## 📝 Tarefas

### 🛠️ Seleção da Palavra Secreta

#### Descrição
Crie uma lista com palavras predefinidas e escolha uma delas aleatoriamente para iniciar o jogo.

#### Requisitos
O programa concluído deve:

- Armazenar pelo menos 5 palavras em uma lista.
- Selecionar uma palavra aleatória no início de cada partida.
- Guardar a palavra escolhida para uso durante o jogo.

### 🛠️ Entrada de Letras e Atualização do Progresso

#### Descrição
Permita que o jogador insira letras e mostre o estado atual da palavra em construção.

#### Requisitos
O programa concluído deve:

- Solicitar uma letra ao jogador por meio de `input()`.
- Verificar se a letra pertence à palavra secreta.
- Mostrar o progresso em formato como `_ _ _ _` conforme as letras forem acertadas.
- Evitar que a mesma letra seja contabilizada mais de uma vez.

### 🛠️ Controle de Tentativas e Fim de Jogo

#### Descrição
Implemente a lógica de vitória, derrota e contagem de erros para finalizar a partida corretamente.

#### Requisitos
O programa concluído deve:

- Definir um número limitado de tentativas para o jogador.
- Registrar letras erradas e reduzir as tentativas restantes.
- Exibir uma mensagem de vitória quando a palavra for completamente revelada.
- Exibir uma mensagem de derrota quando o número de tentativas acabar.
- Encerrar o jogo de forma clara após o resultado final.