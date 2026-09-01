import random

def jogo_adivinhacao():
    # Sorteia um número inteiro entre 1 e 10 (incluindo o 1 e o 10)
    numero_sorteado = random.randint(1, 10)
    
    try:
        # Pega o número digitado pelo usuário e converte para inteiro
        numero_usuario = int(input("Digite um número inteiro entre 1 e 10: "))
        
        # Valida se o número está dentro do intervalo permitido
        if numero_usuario < 1 or numero_usuario > 10:
            print("Por favor, digite um número estritamente entre 1 e 10.")
            return

        # Mostra o número que foi sorteado
        print(f"O número sorteado pelo computador foi: {numero_sorteado}")

        # Compara o número do usuário com o número sorteado
        if numero_usuario == numero_sorteado:
            print("Parabéns! Você acertou o número!")
        else:
            print("Que pena! Você errou o número. Tente novamente!")
            
    except ValueError:
        print("Entrada inválida! Por favor, digite apenas números inteiros.")

# Executa a função do jogo
if __name__ == "__main__":
    jogo_adivinhacao()