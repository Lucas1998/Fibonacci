def FuncionFibo (num):
    if num==1:
        return 1
    if num==0:
        return 0
    else:
        return FuncionFibo(num-1) + FuncionFibo(num-2)     
  
if __name__=="__main__":
    num=int(input("introducir numero"))
    print("La Funcion de Fibonacci es %d" %num)