#calculator 
while 1:
    ans=int(input("what function is to be done: 1)ADD,2)SUBTRACT,3)MULTIPLY,4)DIVIDE,5)SQUARE,6)SQUARE ROOT,7)TRIGNOMETRY FUNCTIONS,8)OTHERS"))
    print("enter the option in integer(1-8)")
    if ans==1:
        n=int(input("enter how many numbers to be added"))
        num=0
        for i in range(n):
            n=float(input("enter the number"))
            num=n+num
        print("the number after addition is ",num)
        z=input("do you want to continue? yes/no").lower()
        if z=="yes":
            continue
        else:
            break
    elif ans==2:
        n=int(input("enter how many numbers to be subtracted"))
        num=[]
        for i in range(n):
            n=float(input("enter the number"))
            num.append(n)
        num1=num[0]
        for i in range(1,len(num)):
            num1=num1-num[i]
        print("the number after subtraction is ",num1)
        z=input("do you want to continue? yes/no").lower()
        if z=="yes":
            continue
        else:
            break
    elif ans==3:
        n=int(input("enter how many numbers to be multiplied"))
        num=1
        for i in range(n):
            n=float(input("enter the number"))
            num=num*n
        print("the number after multiplication is ",num)
        z=input("do you want to continue? yes/no").lower()
        if z=="yes":
            continue
        else:
            break
    elif ans==4:
        div=float(input("enter the dividend"))
        divs=float(input("enter the divisior"))
        num=div/divs
        rem=div%divs
        print("the quotient is ",num)
        print("the reminder is",rem)
        z=input("do you want to continue? yes/no").lower()
        if z=="yes":
            continue
        else:
            break
    elif ans==5:
        b=float(input("enter the base"))
        sq=b**2
        print("the squared number  is",sq)
        z=input("do you want to continue? yes/no").lower()
        if z=="yes":
            continue
        else:
            break
    elif ans==6:
        import math
        n=float(input("enter the number"))
        sqrt=math.sqrt(n)
        print("the square root of",n,"is",sqrt)
        z=input("do you want to continue? yes/no").lower()
        if z=="yes":
            continue
        else:
            break
    elif ans==7:
        import math
        n=int(input("enter the trignometry function 1)sin,2)cos,3)tan,4)sec,5)cosec,6)cot"))
        print("enter the option in integer(1-6)")
        t=float(input("enter the angle in terms of radians"))
        if n==1:
            print("sin of",t,"is",math.sin(t))
        elif n==2:
            print("cos of",t,"is",math.cos(t))
        elif n==3:
            print("tan of",t,"is",math.tan(t))
        elif n==4:
            a=math.cos(t)
            print("sec of",t,"is",1/a)
        elif n==5:
            a=math.sin(t)
            print("cosec of",t,"is",1/a)
        elif n==6:
            a=math.tan(t)
            print("cot of",t,"is",1/a)
    elif ans==8:
        n=int(input("1)converstion,2)age calculator,3)simple interst,4)BMI,"))
        if n==1:
            n1=int(input("1.degree to radians,2.radians to degree,3.celcius to fahrenheit,4.fahrenheit to celcius"
                         "5.celcius to kelvin,6.kelvin to celcius"))
            if n1==1:
                import math
                t=float(input("enter the angle in degrees"))
                print("radians is ",math.radians(t))
                z=input("do you want to continue? yes/no").lower()
                if z=="yes":
                    continue
                else:
                    break
            elif n1==2:
                import math
                t=float(input("enter the angle in radians"))
                print("degree is",math.degrees(t))
                z=input("do you want to continue? yes/no").lower()
                if z=="yes":
                    continue
                else:
                    break
            elif n1==3:
                t=float(input("enter the temperatue in celcius"))
                f=9/5*t+32
                print("fahrenheit -",f)
                z=input("do you want to continue? yes/no").lower()
                if z=="yes":
                    continue
                else:
                    break
            elif n1==4:
                t=float(input("enter the temperatue in fahrenheit"))
                c=(t-32)*5/9
                print("celcius-",c)
                z=input("do you want to continue? yes/no").lower()
                if z=="yes":
                    continue
                else:
                    break
            elif n1==5:
                t=float(input("enter the temperatue in celcius"))
                k=273+t
                print("kelvin",k)
                z=input("do you want to continue? yes/no").lower()
                if z=="yes":
                    continue
                else:
                    break
            elif n1==6:
                t=float(input("enter the temperatue in kelvin"))
                c=t-273
                print("celcius-",c)
                z=input("do you want to continue? yes/no").lower()
                if z=="yes":
                    continue
                else:
                    break
        elif n==2:
            b=float(input("enter your birth year"))
            c=float(input("enter the year that you want your age in or to check your current age enter current year"))
            age=c-b
            print("your age is",age)
            z=input("do you want to continue? yes/no").lower()
            if z=="yes":
                continue
            else:
                break
        elif n==3:
            p=float(input("enter the principle balence"))
            r=float(input("enter the annual interest rate"))
            t=float(input("enter the number of years"))
            si=(p*r*t)/100
            a=p*si
            print("simple intrest=",si,"final amount=",a)
            z=input("do you want to continue? yes/no").lower()
            if z=="yes":
                continue
            else:
                break
        elif n==4:
            w=float(input("enter  the weight"))
            h=float(input("enter height in meters"))
            bmi=w/h**2
            print("BMI IS ",bmi)
            z=input("do you want to continue? yes/no").lower()
            if z=="yes":
                continue
            else:
                break
    else:
        print("you entered wrong number..try again")
        continue
            
            
            
                
                
            
            
            
