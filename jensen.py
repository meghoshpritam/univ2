C=float(input("Enter the effective technology  constant:"))
T=float(input("Enter the development time:"))
K=float(input("Enter the effort needed to develop:"))
L=C*T*pow(K,1/3)
print("The product size is: ",L,"KLOC")


