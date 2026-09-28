'''
Desenvolver um programa em Python utilizando a estrutura de repetição para coletar e exibir o retorno de uma pesquisa de atendimento ao cliente.
O programa deve solicitar a digitação do nome, idade e opinião do entrevistado sobre o atendimento prestado, sendo:
1: EXCELENTE
2: BOM
3: RUIM
A pesquisa deve ser feita com 50 entrevistados.
Ao final, o programa deverá exibir na tela:
a) Quantidade de respostas “EXCELENTE”
b) Quantidade de respostas “RUIM”
Utilize estruturas de decisão para verificar a opinião do entrevistado.
Realize testes com 10 entrevistados para validar o funcionamento do programa.
Compartilhe o projeto completo junto com os prints de tela do código e da execução no seu repositório Github, informe o link do repositório no ambiente virtual
'''

total_entrevistados = 50

qtdd_execelente =0 
qtdd_ruim=0
qtdd_bom=0
contador =1

while contador <= total_entrevistados:
    nome = input("digte seu nome: ")
    idade = int(input("Digite sua idade: "))
    opniao = int(input("digite sua opnião sobre o antendimento prestado: \n 1- Excelente \n 2- Bom \n 3- Ruim \n "))

    if opniao == 1:
        qtdd_execelente += 1
        contador += 1
    elif opniao == 2:
        qtdd_bom += 1
        contador += 1
    elif opniao == 3:
        qtdd_ruim += 1
        contador += 1
    else:
        print("Opção inválida, digite novamente")
       

print("="*30)
print("Quantidade de respostas EXCELENTE: ", qtdd_execelente)
print("Quantidade de respostas RUIM: ", qtdd_ruim)  

    
