# Gerenciador_de_eventos_hasing

## Objetivo
Criar um sistema que permita o gerenciamento de eventos organizados por categorias, utilizando uma estrutura de hash map para otimizar a busca e recuperação dos eventos.

## Funcionalidades
* Inserir Evento: O usuário pode inserir um novo evento, especificando a categoria do evento, o nome do evento e sua descrição.
* Remover Evento: O usuário pode visualizar todos os eventos de uma determinada categoria.
* Buscar Eventos por Categoria: O usuário pode visualizar todos os eventos de uma determinada categoria.
* Listar Todas as Categorias: O usuário pode listar todas as categorias de eventos disponível.

## Implementação
* Hash Map para Amazenamento: implemente uma tabela hash onde a chave será a categoria do evento e o valor será uma lista de eventos para essa categoria.
* Operações de Inserção e Remoção: Para inserção, calcule o hash da categoria e insira o evento na lista correspondente.
* Para remoção, encontre a categoria na tabela hash e remova o evento da lista.
* Operação de Listagem de Categorias: Percorra a tabela hash e liste todas as categorias disponíveis.
* Operação de Listagem de Categorias: Percorra a tabela hash e liste todas as categorias disponíveis.
* Redimensionamento da tabela hash: quando o fator de carga da tabela hash estiver entre 0,7 e 0,8 realize o redimensionamento da tabela que envolve aumentar o tamanho da tabela hash para um novo tamanho apropriado (número primo próximo ao dobro do tamanho original) e todos os elementos precisam ser rehashing e inseridos na nova tabela

## Realização

<b>PROBLEMAS</b>
* Tivemos um pouco de difculdade em ultilizar o Hashing em Python, já que ele foi criado em C.
* De inicio, fizemos o projeto utilizando funções prontas (code.py), em seguida, adaptamos criando nossas prórpias funções (main.py).

<b>COMENTÁRIOS:</b>
* Conseguimos realizar tudo o que foi proposto.

<b>PARTICIPANTES:</b>

* Antônio Alan Oliveira Farias / https://github.com/farias-alan
* André Filipe Gomes Rocha / https://github.com/Andrefgr24
* Péricles Andrade Feitoza / https://github.com/periclesanfe

<b>REFERÊNCIAS:</b>
