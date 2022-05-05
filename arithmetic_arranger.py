def arithmetic_arranger(problems,a=False):
    l=problems
    operators = list(map(lambda x: x.split()[1], l))
    operators.append("+")
    operators.append("-")
    numbers=[]
    setnumbers=[]
    operator=[]
    for i in l:
        p=i.split()
        numbers.append(p[0]+p[2])
        number1=p[0]
        number2=p[2]
        setnumbers.append([number1,number2,p[1]])
        try:
            if len(number1)>4 or len(number2)>4:
                raise BaseException
        except:
            arranged_problems="Error: Numbers cannot be more than four digits."
            return arranged_problems
        
    if len(l)>5:
        arranged_problems="Error: Too many problems."
        return arranged_problems
    elif set(operators)!={"+","-"}:
        arranged_problems="Error: Operator must be '+' or '-'."
        return arranged_problems
    elif not all(map(lambda x: x.isdigit(), numbers)):
        arranged_problems="Error: Numbers must only contain digits."
        return arranged_problems
    
    else:
        line1=""
        line2=""
        dashes=""
        solutions=""
        for i in setnumbers:
            if len(i[0])<len(i[1]):
                line1=line1+(" "*((len(i[1])+2)-len(i[0]))+i[0]+"    ")
                line2=line2+(i[2]+" "+i[1]+"    ")
            else:
              line1=line1+("  "+i[0]+"    ")
              line2=line2+(i[2]+" "*((len(i[0])+1)-len(i[1]))+i[1]+"    ")
 
            dashes=dashes+("-"*(int(max(len(j)for j in i))+2)+"    ")
            if i[2]=="+":
                s=int(i[0])+int(i[1])
            else:
                s=int(i[0])-int(i[1])
            solutions=solutions+(" "*int(max(len(j)for j in i)+2-len(str(s)))+str(s)+"    ")
        line1=line1[:len(line1)-4]
        dashes=dashes[:len(dashes)-4]
        line2=line2[:len(line2)-4]
        solutions=solutions[:len(solutions)-4]
              
    if a:
        arranged_problems=line1+"\n"+line2+"\n"+dashes+"\n"+solutions
    else:
        arranged_problems=line1+"\n"+line2+"\n"+dashes
   
    return arranged_problems
