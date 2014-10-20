def cigar_party(cigars, is_weekend):
     if (not is_weekend):
         return 40 <= cigars <= 60
     else:
         return 40 <= cigars     

print cigar_party(30, True)
print cigar_party(50, False)
print cigar_party(70, True)