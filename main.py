import random


def is_prime(number):
    if number<2:
        return False
    for _ in range(10):
    
        a=random.randint(2,number)-1
        if pow(a,number-1,number) !=1:
            
            return False
    return True


def primitive_root(prime):
    num_to_check = 0
    p_minus_1_range = range(1,prime)
    primitive_roots = []
    for each in range(1, prime):
	    num_to_check += 1
	    candidate_prim_roots = []
	    for i in range(1, prime):
		    modulus = (num_to_check ** i) % prime
		    candidate_prim_roots.append(modulus)
		    cleanedup_candidate_prim_roots = set(candidate_prim_roots)
		    if len(cleanedup_candidate_prim_roots) == len(range(1,prime)):
			    primitive_roots.append(num_to_check)
    return primitive_roots[len(primitive_roots)-1]


def generating_prime_and_primitive_root(start,end):
    number=random.randint(start,end)
    
    while not is_prime(number):
        number=random.randint(start,end)
    primitive_rootno=primitive_root(number)
    return number,primitive_rootno


def diffie_hellman(start,end):
    prime,primitive_root=generating_prime_and_primitive_root(start,end)
    user1_Pkey=random.randint(1,prime)
    user2_Pkey=random.randint(1,prime)

    private_key1=pow(primitive_root,user1_Pkey,prime)
    private_key2=pow(primitive_root,user2_Pkey,prime)
    
    key=pow(private_key2,user1_Pkey,prime)
    key2=pow(private_key1,user2_Pkey,prime)

    print(f"key1 -->{key}  ,key2-->{key2}")



diffie_hellman(1,67)

