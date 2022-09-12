# oblicznenia dla rowów trapezowych
# dane
n=0.0333
i=0.002

B=0.5
h=0.6
m1=1.5
m2=1.5

d=B*h+0.5*(m1+m2)*h**2
e=B+h*((1+m1**2)**0.5+(1+m2**2)**0.5)
R=d/e

# prędkość
v=(1/n)*R**(2/3)*i**(0.5)
# pole
S=(B+0.5*(m1+m2)*h)*h
# natężenie
Q=v*S


print('V=',round(v,4))
print('Q=',round(Q,4))
print('S=',round(S,4))


# napełnienie dla zadanego Q
Qs=0.5227

# iteracja
h=1
wynik_Q=[Qs/2]
wynik_h=[h]
dok=0.001

while abs(1-(wynik_Q[-1]/Qs))>dok:   
    S=(B+0.5*(m1+m2)*h)*h

    d=B*h+0.5*(m1+m2)*h**2
    e=B+h*((1+m1**2)**0.5+(1+m2**2)**0.5)
    R=d/e
    v=(1/n)*R**(2/3)*i**(0.5)

    Q=v*S

    if Qs>=Q:
        h*=1.001
    else:
        h*=0.999
    wynik_Q.append(Q)
    wynik_h.append(h)

# print(wynik_Q,wynik_h)
print('****')
print('h=',round(wynik_h[-1],3))
print('Q=',round(wynik_Q[-1],3))


