# Bloc: groupe de 9 cases. Comptés de gauche à droite de haut en bas (de 0 à 8)

# lrow : ensemble des valeurs utilisées sur une ligne
# lcol : ensemble des valeurs utilisées dans une colonne
# l_u : ensemble des valeurs utilisées au sein d'un bloc


# _____fonction_____

# div_euc(a,b) : renvoie le résultat de la division euclidienne de a par b sous la forme [q,mod]

#affiche(tab) : affiche chaque ligne d'un tableau

#bloc(num) : renvoie le numéro de chaque case d'un bloc

# pos_bloc(x,y) : renvoie le numéro de position d'un bloc en fonction de sa position en x et y

# val_poss_bloc(tab,num) : renvoie les valeurs possibles d'une case en fonction des valeurs de son bloc

#val_poss_row(tab,x,y) : renvoie les valeurs possibles d'une case en fonction des valeurs de sa ligne

#val_poss_col(tab,x,y) : renvoie les valeurs possibles d'une case en fonction des valeurs de sa ligne

#valeurs_possible(tab,x,y) : renvoie les valeurs possibles d'une case en fonction des valeurs de sa ligne,colonne et bloc

#fill() : génère une grille de sodoku remplie dans la variable global tab. renvoie 1 si grille généré 0 sinon

#dispo(tab) : donne le nombre de cases à remplir au sein d'une grille (nombre de 0)

#sol(tab,vide) : vérifie si une grille est résoluble. renvoie tab si la grille est résoluble 0 sinon

#solution(tab,vide) : renvoie 0 si la grille n'est pas résoluble, la grille remplie sinon

#position(x) : renvoie les coordonnées de la x-ieme case d'un tableau sous la forme [x,y]

#cache(n) : retire n cases aléatoire d'un grille remplie en vérifiant que cette dernière reste résoluble après retrait de la valeur. renvoie la table caché avec un n(<57) valeurs retiré

#sudoku(n): renvoie une grille à remplir possédant n (<57) cases libres

# _________________________________________________________________________#

import random
import time


tab = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]] # grille sudoku complète

tab2 = [list(range(1,10)),list(range(10,19)),list(range(19,28)),list(range(28,37)),list(range(37,46)),list(range(46,55)),list(range(55,64)),list(range(64,73)),list(range(73,82))] #matrice des positions

tab3 = []

tab4 = [[0,2,0,0,8,5,0,3,0],[7,0,0,4,9,0,0,0,0],[0,0,0,0,0,3,8,6,0],[5,0,3,0,0,0,0,0,1],[8,7,0,0,0,0,0,4,0],[0,4,0,0,0,0,3,0,0],[0,0,0,0,0,0,5,7,2],[0,0,0,0,0,8,0,1,3],[6,0,1,0,0,0,9,8,4]]

nb = 0 # nombre de simulation afin d'obtenir une grille complète

def div_euc(a,b):

    q = a//b
    modulo = a-q*b
    list = [q,modulo]

    return list


def affiche(tab):

    for i in range(9):
        print(tab[i])
    print("\n")


def bloc(num):

    global tab2
    l = []
    b = []
    q = div_euc(num,3)[0]
    mod = div_euc(num,3)[1]
    a = tab2[q*3:q*3+3]

    for i in range(3):
        b.append(a[i][(mod)*3:(mod)*3+3])

    for i in range(3):
        for j in range(3):
            l.append(b[i][j])

    return l


def pos_bloc(x,y):

    global tab2
    a = tab2[x][y]

    for i in range(0,9):
        if a in bloc(i):
            return i

    return 0

        
def val_poss_bloc(tab,num):
    
    l_u = []
    a = []
    sol = div_euc(num,3)
    q = sol[0]
    mod = sol[1]
    t = tab[q*3:q*3+3]

    for i in range(3):
        a.append(t[i][mod*3:mod*3+3])

    for i in range(3):
        for j in range(3):
            if a[i][j] != 0:
                l_u.append(a[i][j])

    l_u = set(l_u)
    l_u = list(l_u)
    l = list(range(1,10))

    for i in range(len(l_u)):
        b = l_u[i]
        del l[l.index(b)]
        
    return l


def val_poss_row(tab,x,y):

    lrow = []

    for i in range(9):
        if tab[x][i] != 0:
            lrow.append(tab[x][i])

    l = list(range(1,10))

    for i in range(len(lrow)):
        a = lrow[i]
        del l[l.index(a)]
    
    return l


def val_poss_col(tab,x,y):

    lcol = []

    for i in range(9):
        if tab[i][y] != 0:
            lcol.append(tab[i][y])
        
    l = list(range(1,10))

    for i in range(len(lcol)):
        a = lcol[i]
        del l[l.index(a)]
    
    return l


def valeurs_possible(tab,x,y):

    num = pos_bloc(x,y)
    l1 = set(val_poss_row(tab,x,y))
    l2 = set(val_poss_col(tab,x,y))
    l3 = set(val_poss_bloc(tab,num))
    l = list(l1&l2&l3)

    return l


def fill():

    global tab
    global nb
    nb = nb+1
    for i in range(9):
        for j in range(9):
            
            if nb == 995: # empeche erreur exces de récursion
                return 0
            
            elif len(valeurs_possible(tab,i,j)) == 0:

                tab = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
                return(fill())

           
            else:
                a = random.choice(valeurs_possible(tab,i,j))
                tab[i][j] = a
                if (i==8 and j==8):
                    return 1
    return 0
   
 
def dispo(tab):

    zero = 0
    for i in range(9):
        for j in range(9):
            if tab[i][j] == 0:
                zero = zero+1
                
    return zero


def sol(tab1,vide):    

    global tab
    acc = 0
    tabl = [row[:] for row in tab1]
    l = []
    
    for k in range(vide):
        for i in range(9):
            for j in range(9):
                if tabl[i][j] == 0:
                    a = [i,j]
                    l.append(a)
                    
                    val = valeurs_possible(tabl,i,j)
                    
                    if len(val) == 1:
                        tabl[i][j] = val[0]
                        acc = acc+1
    if acc == vide:
        for k in range(vide):
            i = l[k][0]
            j = l[k][1]
            tabl[i][j] = 0
        return tabl
    
    return 0

def solution(tab1,vide):  

    global tab
    acc = 0
    tabl =  [row[:] for row in tab1]
    l = []
    
    for k in range(0,vide):
        for i in range(9):
            for j in range(9):
                if tabl[i][j] == 0:
                    a = [i,j]
                    l.append(a)
                    
                    val = valeurs_possible(tabl,i,j)
                    
                    if len(val) == 1:
                        tabl[i][j] = val[0]
                        acc = acc+1
                        if acc == vide:
                            return tabl
    
    return 0



def position(x):

    global tab2

    for i in range(9):
        if x in tab2[i]:

            b = i
            for j in range(9):
                if x == tab2[b][j]:
                    c = j
                    l = [i,j]

                    return l

    return 0


def verif(grille,tab1):

    tabl = [row[:] for row in grille]
    
    for i in range(9):
        for j in range(9):
            if grille[i][j] == 0:
                if tab1[i][j] in valeurs_possible(tabl,i,j):
                    tabl[i][j] = tab1[i][j]
                else:
                    return 0
    return 1


def cache(n): 
   
    global tab
    grille = [row[:]for row in tab]
    hide = 0
    pos = list(range(1,82))
    
    while hide !=n:
        
        numpos = random.choice(pos)
        i = position(numpos)[0]
        j = position(numpos)[1]
        grille[i][j] = 0
        if (sol(grille,hide+1) != 0):
            hide +=1
        else:
            grille[i][j] = tab[i][j]
        del pos[pos.index(numpos)]
        if len(pos) == 0:
            hide = n      
        
    return grille


def sudoku():

    #start = time.time()
    nb = 0
    
    print('choisissez la difficulté 1,2,3,4 ou 5\n')
    x = input()
    if x == '1':
        n = random.choice([44,45,46])
    elif x == '2':
        n = random.choice([46,47,48])
    elif x == '3':
        n = random.choice([48,49,50])
    elif x == '4':
        n = random.choice([50,51,52,53,54])
    else:
        n = random.choice([54,55,56])

    while (fill() != 1):
        fill()
    grille = cache(n)
    
    while (dispo(grille) != n):
        grille = cache(n)

    #end = time.time()
    #print(end-start)
    return grille


# test__________________________

#a = sudoku()
#print(dispo(a))
#affiche(a)


tab8  =[[7, 6, 0, 0, 0, 9, 0, 1, 0],
        [8, 0, 0, 0, 0, 0, 7, 2, 4],
	[0, 0, 0, 7, 1, 4, 0, 0, 9],
	[4, 0, 6, 0, 0, 0, 3, 0, 2],
	[0, 7, 0, 4, 5, 6, 0, 0, 0],
	[0, 5, 1, 0, 0, 0, 0, 7, 6],
	[1, 0, 0, 2, 9, 0, 0, 4, 0],
	[2, 0, 7, 6, 3, 0, 1, 0, 0],
	[0, 9, 8, 0, 0, 5, 2, 0, 7]]

