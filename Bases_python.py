#!/usr/bin/env python
# coding: utf-8

# ### Premier programme

# In[2]:


print("Je m'appelle Toto. Mon nom c'est bien Toto")


# Lors de l'appel d'une fonction on met toujours des parenthèses

# ### Variable et concaténation

# In[7]:


nom = "toto"
print("Je m'appelle " + nom)

# le print() sans parametres dit qu'on veut mettre une ligne vide
print()
print("Mon c'est bien " + nom + ".")


# ### Comment s'organiser

# In[1]:


# commence le debut de la video correction et faire les exercices
# demander à l'utilisateur son nom
nom = input("Quel est votre nom ?")
print("Je m'appelle "+ nom)


# In[2]:


nom = input("Quel est votre nom ?")
age = input("Quel est votre age ?")
print("Vous êtes " +nom+ " et vous avez " +age+ " ans.")


# In[3]:


# le type de la variable par la fonction type, en realite 
type(age)


# In[5]:


# input() renvoi un caractère ou une chaine de caractère donc il faut changer la valeur 
age = 30
age_prochain = age + 1
print("Vous êtes " +nom+ " et vous avez " + str(age) + " ans.")
print("L'an prochain vous aurez " + str(age_prochaine) + " ans.")


# In[6]:


# si on a une variable qui dépende d'une autre variable, on peut l'alléger utilisant cette variable, comme le code ci-dessous


# ### Convertir au niveau de la fonction input()

# In[8]:


nom = input("Quel est votre nom ?")
age = int(input("Quel est votre age ?"))
print("Votre nom est " + nom + " vous avez " + str(age) + " ans.")


# ### Erreurs et gestion des exceptions: si l'utilisateur met des alphabet ou autre chose à la place

# In[11]:


nom = input("Quel est votre nom ?")
age = input("Quel est votre age ?")
    
# on va mettre un code de gestion d'erreur
try:
    age_prochain = int(age) + 1
    print("Votre nom est " + nom + " vous avez " + str(age) + " ans.")
    print("Vous aurez " + str(age_prochain) + " ans l'annee prochaine.")
except:
    print("Erreur: Vous devez entrez une valeur numérique.")


# ### try: ... except: ... else: ...

# In[13]:


nom = input("Quel est votre nom ?")
age = input("Quel est votre age ?")
    
# on va mettre un code de gestion d'erreur
try:
    age_prochain = int(age) + 1
except ValueError:
    print("Erreur: Vous devez entrez une valeur numérique.")
# si ça a bien fonctionner
else:
    print("Votre nom est " + nom + " vous avez " + str(age) + " ans.")
    print("Vous aurez " + str(age_prochain) + " ans l'annee prochaine.")


# ### Boucle while

# In[15]:


nom = input("Quel est votre nom ?")
age = input("Quel est votre age ?")

# on va mettre un code de gestion d'erreur
try:
    age_prochain = int(age) + 1
except ValueError:
    print("Erreur: Vous devez entrez une valeur numérique.")
# si ça a bien fonctionner
else:
    print("Votre nom est " + nom + " vous avez " + str(age) + " ans.")
    print("Vous aurez " + str(age_prochain) + " ans l'annee prochaine.")


# ### Amélioration du code

# #### Sur cette exercice on a choisit de voir si la variable age_prochain est différent de zéro

# In[17]:


nom = input("Quel est votre nom ?")
age = input("Quel est votre age ?")

# on va utiliser l'age_prochain pour verifier la condition
age_prochaine = 0
# on va mettre un code de gestion d'erreur

# 
while age_prochain == 0:
    age = input("Quel est votre age ?")
    try:
        age_prochain = int(age) + 1
    except ValueError:
        print("Erreur: Vous devez entrez une valeur numérique.")
        
    # si ça a bien fonctionner
print("Votre nom est " + nom + " vous avez " + str(age) + " ans.")
print("Vous aurez " + str(age_prochain+1) + " ans l'annee prochaine.")


# In[ ]:




