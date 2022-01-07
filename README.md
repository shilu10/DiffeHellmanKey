# DiffeHellmanKey

#diffie hellman key exchange

#1. step generate large prime and largest primitive root of that prime .primitive root is nothing but
#when the number is mod with the prime number it wil give all th possible number 
#prime number is proportinal to the primitive root number  
#prime number (p)  and primitive root(g)

#2.generate prime number for the personal private key x,y< prime number (p) for both users

#3.we will produce a private key for the exchange purpose using the modular exponention
# formula a**g mode p  ->>  g **x mod p( ,g**Y mod p

#and both will exchange the key with each other ,attacker can have all of these things
#but he cant able to break the inverse of modular exponentation (discrete logarithm)

#4.using that both can have the same private key with each other......by using the formula of 
#modular exponentation with the (key ** x,y mod p)--->>>> this will give same key for both of them in conversation

#we can generate the given number is prime or not using the fermat little theorem but fermat theorem is not proven
#fermat little theorem  -->>  a**p-1 mod p=1  where p is the prime number a is not divisable of p
#and fermat little theorem is probablistic which means we need some iteration for the confirmation that it is really a prime  number
