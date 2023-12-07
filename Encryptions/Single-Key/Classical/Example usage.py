from Caesar import caesar
from Monoalphabetic import monoalphabetic
from PlayFair import playfair
from RailFence import railfence
from RowTransposition import rowtransposition
from Vigenere import vigenere

'''
This file is an example usage of the Classical methods.

Note: YOU CAN SEND ANY KEY AS INT OR STRING ACCORDING TO THE CYPHER USED LOOK AT THE CAESAR CYPHER EXAMPLE USAGE IN THIS FILE.
Note: PLAIN OR ENCRYPTED TEXT WHEN GIVEN TO A CERTAIN CYPHER IF IT HAS ANY SPECIAL CHARATERS OR NUMBERS IT WILL BE AUTOMATICALLY REMOVED AT ONCE BUT BE CAREFUL.
Note: ALL THE CLASSCIAL CYPHERS ENCRYPT TEXT ONLY (A-Z) ALSO IT DOESN'T RETURN UPPER CASE LETTERS.
Note: IF ANY UPPER CASE LETTERS ARE SENT IT WILL BE AUTOMATICALLY CONVERTED TO LOWER CASE IN ALL CYPHERS.


Have fun exploring the code guys.
BY Pola
'''

if __name__ ==  "__main__":
    cypher = caesar("3")
    print(cypher.dic)
    print(cypher.encrypt("Hello World, I am a cypher"))
    print(cypher.decrypt(cypher.encrypt("Hello World, I am a cypher")))

    cypher = caesar(3)
    print(cypher.dic)
    print(cypher.encrypt("Hello World, I am a cypher"))
    print(cypher.decrypt(cypher.encrypt("Hello World, I am a cypher")))


    cypher = caesar(155) # it will be reduced to 5 (155 % 25 = 5)
    print(cypher.dic)
    print(cypher.encrypt("Hello World, I am a cypher"))
    print(cypher.decrypt(cypher.encrypt("Hello World, I am a cypher")))

    cypher = monoalphabetic("What are you doing back here! lets go away; we have so many things to do.")
    print(cypher.key)
    print(cypher.dic)
    print(cypher.encrypt("Hello World, I am a cypher"))
    print(cypher.decrypt(cypher.encrypt("Hello World, I am a cypher")))

    cypher = playfair("word")
    print(cypher.key)
    print(cypher.dic)
    print(cypher.encrypt("Hello World, I am a cypher"))
    print(cypher.decrypt(cypher.encrypt("Hello World, I am a cypher")))
    print(cypher.encrypt("what the are you doing"))
    print(cypher.decrypt(cypher.encrypt("what the are you doing")))


    cypher = vigenere("MaTH")
    print(cypher.dic)
    print(cypher.encrypt("Hello World, I am a cypher"))
    print(cypher.decrypt(cypher.encrypt("Hello World, I am a cypher")))
    print(cypher.encrypt("Make it happen."))
    print(cypher.decrypt(cypher.encrypt("Make it happen.")))

    cypher = vigenere("deceptivedeceptivedeceptive")
    print(cypher.dic)
    print(cypher.encrypt("wearediscoveredsaveyourself"))
    print(cypher.decrypt(cypher.encrypt("wearediscoveredsaveyourself")))
    

    cypher = rowtransposition("4312567") # you can send it as int or string
    print(cypher.dic)
    print(cypher.encrypt("Hello World, I am a cypher"))
    print(cypher.decrypt(cypher.encrypt("Hello World, I am a cypher")))

    print(cypher.encrypt("attack postponed until two am."))
    print(cypher.decrypt(cypher.encrypt("attack postponed until two am.")))


    cypher = railfence("11")
    print(cypher.dic)
    print(cypher.encrypt("Hello World, I am a cypher"))
    print(cypher.decrypt(cypher.encrypt("Hello World, I am a cypher")))

    cypher = railfence(2)
    print(cypher.dic)
    print(cypher.encrypt("This is a secret message."))
    print(cypher.decrypt(cypher.encrypt("This is a secret message.")))

    cypher = railfence(4)
    print(cypher.dic)
    print(cypher.encrypt("They are attacking from the north"))
    print(cypher.decrypt(cypher.encrypt("They are attacking from the north")))