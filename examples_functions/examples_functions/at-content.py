def get_at_content(dna): 
    length = len(dna) 
    a_count = dna.count('A') 
    t_count = dna.count('T') 
    at_content = (a_count + t_count) / length 
    return at_content


at_content = get_at_content("ATGACTGGACCA")
print("ATGACTGGACCA" + ": " + str(at_content))
print("AT content ATGACTGGACCA  is " + str(get_at_content("ATGACTGGACCA")))
print(get_at_content("ATGCGCGATCGATCGAATCG"))

