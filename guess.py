def checknum(oriNum,guessNum):
    strOriNum=str(oriNum)
    strGuessNum=str(guessNum)
    aNum=0
    bNum=0
    aList=[]
    for i in range(4):
        if(strOriNum[i]==strGuessNum[i]):
            aNum=aNum+1
            aList.append(strOriNum[i])
    for s in aList:
        strOriNum=strOriNum.replace(s,'')
        strGuessNum=strGuessNum.replace(s,'')
    for s in strGuessNum:
        if s in strOriNum:
            bNum=bNum+1
    return str(aNum)+'A'+str(bNum)+'B'

def allPossible():
    seed='0123456789'
    possibledata=[]
    for s1 in seed:
        seed2=seed.replace(s1,'')
        for s2 in seed2:
            seed3=seed2.replace(s2,'')
            for s3 in seed3:
                seed4=seed3.replace(s3,'')
                for s4 in seed4:
                    possibleStr=s1+s2+s3+s4
                    possibledata.append(possibleStr)
    return possibledata

def possibleOrigin(guessNum,result,dataArea):
    strGuessNum=str(guessNum)
    possibledata=[]
    for data in dataArea:
        if checknum(data,strGuessNum)==result.upper():
            possibledata.append(data)
    return possibledata

print(checknum(7381,7813))

data=allPossible()
data=possibleOrigin(1234,'0A2B',data)
data=possibleOrigin(2156,'0A1B',data)
data=possibleOrigin(7428,'1A1B',data)
data=possibleOrigin(4920,'0A0B',data)
data=possibleOrigin(7813,'1a3b',data)
print(data)