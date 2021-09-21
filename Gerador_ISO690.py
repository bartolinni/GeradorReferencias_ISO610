#!/usr/bin/env python
# coding: utf-8

# # Programa sem GUI

# In[3]:


def autores():  # pede o nome dos autores e devolve no formato SOBRENOME1, I1. NM1., SOBRENOME2, I2. NM2
    numero_autores = int(input("Quantos autores? "))
    n = 1 # é a variável de contagem dos autores para o devido preenchimento pelo usuário
    #i = 1 # é o número de 'nomes' que o autor tem antes do sobrenome
    Autores_raw = []
    Autores_formatado = ''
    
    while n <= numero_autores:
        Autor = str(input(f'{n}º Autor: ')).lower()
        Autores_raw.append(Autor)
        n += 1

    for autor in Autores_raw:
        if autor == Autores_raw[-1] and numero_autores != 1: # Se o autor for o último da lista e houver mais de 1 autor
            Autores_formatado += '& '  # Adiciona '& ' antes do último autor

        Autores_formatado = Autores_formatado + (autor.split()[-1].upper()) + ', '  # Cria o sobrenome em maíusculo 'SOBRENOME, '
        
        for nome in autor.split():  # Varre os nomes do autor e separa as iniciais e as capitaliza
            if nome == autor.split()[-1]:  # Se o nome a ser transformado em inicial for o sobrenome, pula para a próxima iteração
                next
            elif nome == 'do' or nome == 'das' or nome == 'da' or nome == 'de' or nome == 'dos':  # Elimina estas partes do nome
                next  # Por alguma razão não consegui sucesso com: nome == ('do' or 'dos' or 'de' ...)
            else:  # Se não for, as iniciais são separadas e capitalizadas normalmente
                Autores_formatado = Autores_formatado + autor.split()[autor.split().index(nome)][0].upper() + '.'  # I1. I2. 
        
        if numero_autores != 1 and autor == Autores_raw[-2]: # Se houver mais de 1 autor e a iteração estiver no penúltimo autor
            Autores_formatado += ' ' # Apenas adiciona um espaço após mencionar o penúltimo autor
            next
        else:
            Autores_formatado += ', '  # Senão, adiciona uma vírgula de separação I1. I2.,
        
    return Autores_formatado  # Devolve a string 'SOBRENOME1, I11.I12., SOBRENOME2, I21.I22., ... & SOBRENOMEn, In1.In2.In3 '


# In[ ]:


#def citacao():  # Deve devolver a citação no formato correto para 1, 2, 3 ou mais autores
    # 1 autor: Sobrenome (ano) ou (Sobrenome, ano)
    # 2 auts:  Sobrenome1 e Sobrenome2 (ano)  ou  (Sobrenome1 e Sobrenome2, ano)
    # mais:    Sobrenome1 et al., (ano)  ou  (Sobrenome1 et al., ano)


# In[ ]:



print('''Bem vindo(a)
Este humilde programa foi criado para te ajudar a criar referências de acordo com a norma ISO 690/2010
Boa integradora''')

print('''         [1] Artigo
         [2] Livro
         [3] Capítulo de livro
         [4] Dissertação ou tese
         [5] Trabalho apresentado em evento
         [6] Documento eletrônico
         
         [0] Sair do programa''')

tipo_documento = 1

while tipo_documento != 0:
    
    tipo_documento = int(input("Digite o número referente ao tipo de documento que você quer referenciar: "))
# Artigo, Livro, Cap de livro, Dissertação ou tese, Trabalho apresentado em evento, documento eletrônico
    
    Autores_string = autores()
    titulo_trabalho = input('Título do artigo: ').lower().title()
    ano_trabalho = input('Ano do trabalho: ')
    
    if tipo_documento == 1:
        revista = input('Revista: ').lower()
        volume = input('Volume: ')
        numero = input('Número: ')
        pgi = input('Página inicial: ')
        pgf = input('Página final: ')
        DOI = input('Link do DOI: ')
        print(f'{Autores_string} {ano_trabalho}. {titulo_trabalho}. {revista}, vol. {volume}, no. {numero}, pp. {pgi}-{pgf}. {DOI}.')

    elif tipo_documento == 2:
        SEGUINTE

    elif tipo_documento == 3:
        SEGUINTE

    elif tipo_documento == 4:
        SEGUINTE

    elif tipo_documento == 5:
        SEGUINTE

    elif tipo_documento == 6:
        SEGUINTE

    else:
        print('Entrada inválida. Tente novamente')
    
    next
        
print("\n Você encerrou o programa. Até breve!")

