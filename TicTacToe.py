import random  
import os
from colorama import Fore, Back, Style
jogadas = 0 
quem_joga = 1 #um é o huamno 2 é a CPU 
max_jogadas = 9 
vit = False 

velha = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "],
]
def Matriz():
    global velha
    global jogadas
    os.system('cls')
    print ('    0   1   2   ')
    for i in range(0,3):
        print ("{}:  ".format(i) + velha[i][0] + " | " +velha[i][1] + " | " + velha[i][2])
        print("   -----------")

def player_move(): 
    global jogadas
    global quem_joga
    global vit
    global max_jogadas
    if (quem_joga == 1 and jogadas < max_jogadas):
        l = int(input('Linha: '))
        c = int(input('Coluna: ')) #agora tem que verificar se essa posição esta vazia 
        try:
            while (velha[l][c] != " "): #pq afinal ainda não ARMAZENAMOS a jogada na posição 
                l = int(input('Linha: '))
                c = int(input('Coluna: '))
            velha[l][c] ='X'
            quem_joga =2
            jogadas+=1
        except:
            print('Linha ou coluna invalidas! ')
            vit = false 
def cpu_move():
    global jogadas
    global quem_joga
    global vit
    global max_jogadas
    if (quem_joga == 2 and jogadas<max_jogadas):
        l = random.randrange(0,3)
        c = random.randrange(0,3)
        while (velha[l][c]!=" "):
            l = random.randrange(0,3)
            c = random.randrange(0,3)
        velha[l][c] ='O'
        quem_joga =1
        jogadas+=1
        
while True:
    Matriz()
    player_move()
    cpu_move()

        
    