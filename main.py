class HashTable:
    def __init__(self):
        self._tamanho = 10 #
        self.full = 0
        self._slots = [None] * self._tamanho
        self._valores = [None] * self._tamanho
        self._descricoes = [None] * self._tamanho
    
    def hashfunction(self,chave):
        total = 0
        for char in chave:
            total += ord(char)
        return total % self._tamanho
    
    def rehash(self,oldhash):
        return (oldhash+1) % self._tamanho
    
    def put(self,chave,valor, desc):
        if self.full == self._tamanho:
            self.redimensionar()
        valor_hash = self.hashfunction(chave)
        
        while self._slots[valor_hash] != None and self._slots[valor_hash] != chave:
            valor_hash = self.rehash(valor_hash)
            
        self._slots[valor_hash] = chave
        self._valores[valor_hash] = valor
        self._descricoes[valor_hash] = desc
        self.full += 1
                    
    def get(self,chave): # retorna a categoria do evento, por nome   
        valor_hash = self.hashfunction(chave)
        
        while self._slots[valor_hash] != None:
            if self._slots[valor_hash] == chave:
                return self._valores[valor_hash]
            valor_hash = self.rehash(valor_hash)
        
        return None
    
    def get_by_categoria(self, categoria):
        eventos = [f'\n{self._slots[i]} ({self._descricoes[i]})' for i in range(self._tamanho) if self._valores[i] == categoria]
        return eventos
    
    def remove(self,chave):
        valor_hash = self.hashfunction(chave)
        
        while self._slots[valor_hash] != None:
            if self._slots[valor_hash] == chave:
                self._slots[valor_hash] = None
                self._valores[valor_hash] = None
                self._descricoes[valor_hash] = None
                self.full -= 1
                return True
            valor_hash = self.rehash(valor_hash)
        
        return False
    
    def redimensionar(self):
        self._tamanho = self._tamanho * 2 + 1
        while not self.eh_primo(self._tamanho):
            self._tamanho += 1
        
        novo_slots = [None] * self._tamanho
        novo_valores = [None] * self._tamanho
        novo_descricoes = [None] * self._tamanho
        
        for i in range(self._tamanho):
            if self._slots[i] != None:
                novo_hash = self.hashfunction(self._slots[i]) % self._tamanho
                while novo_slots[novo_hash] != None:
                    novo_hash = self.rehash(novo_hash) % self._tamanho
                novo_slots[novo_hash] = self._slots[i]
                novo_valores[novo_hash] = self._valores[i]
                novo_descricoes[novo_hash] = self._descricoes[i]
        
        self._slots = novo_slots
        self._valores = novo_valores
        
    def eh_primo(self,numero):
        for i in range(2,numero**0.5):
            if numero % i == 0:
                return False
        return True
        

    def __str__(self):
        categorias = ""
        for categoria in self._valores:
            if categoria != None and categoria not in categorias:
                categorias += str(categoria) + " "
        return str(categorias)

def main():
    eventos = HashTable()
    
    while True:
        print("\nMenu:\n1. Adicionar Evento\n2. Listar Categorias\n3. Mostrar Eventos por Categoria\n4. Remover Evento\n5. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            nome = input("Digite o nome do evento: ")
            categoria = input("Digite a categoria do evento: ")
            descricao = input("Descreva o evento: ")
            eventos.put(nome,categoria, descricao)
            print("Evento adicionado com sucesso!")
        
        elif escolha == "2":
            print("\nCategorias disponíveis:")
            print(eventos)
            
        elif escolha == "3":
            print(eventos)
            categoria = input("Digite a categoria do evento: ")
            eventos_categoria = eventos.get_by_categoria(categoria)
            
            if not eventos_categoria:
                print(f"Nenhum evento encontrado na categoria '{categoria}'.")
            else:
                print(f"Eventos na categoria '{categoria}': {', '.join(eventos_categoria)}\n")


        elif escolha == "4":
            evento = input("Digite o nome do evento: ")
            if eventos.remove(evento):
                print("Evento removido com sucesso!")
            else:
                print("Evento não encontrado.")
        
        elif escolha == "5":
            print('Saindo...')
            break
        
        else:
            print("Opção inválida.")
        
if __name__ == "__main__":
    main()
            