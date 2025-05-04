print("OR table")
for i in [True, False]:
    for j in [True, False]:
        print(i,"OR",j,"IS", i or j,sep='\t')
    print()
        
print("XOR table")
for i in [True, False]:
    for j in [True, False]:
        print(i, "XOR", j, "IS", i^j, sep = '\t')
    print()

x_before = 0b00000100   
print(f"{x_before:08b}","<< 1 =",{x_before<<1})
print(f"{x_before:08b}",">> 1 =",{x_before>>1})
