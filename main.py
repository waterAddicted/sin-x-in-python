
def sinus(x,eps):
    t=x
    k=float(1)
    s=float(0)  
    print("t=",t,"k=",k,"s=",s)
    while abs(t)>eps:
        print(t)
        s = s + t
        t = t*((-x*x)/((k*2)*(k*2+1)))
        k += 1
    return s

x=float(input())
eps=0.000001
print("sinus de",x,"este",float(sinus(x,eps)))