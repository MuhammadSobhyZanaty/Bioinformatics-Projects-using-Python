f = open ("weight.txt")
weightD = {}
weightaa ={}
for line in f:
      line=line.rstrip()
      words = line.split(" ")
      aa = words[0]
      da = int(words[1])
      weightD[da]=aa
      weightaa[aa]=da


def LinearSpectrum (pep):
      pepList = ['',pep]
      for i in range(1,len(pep),1):
            for j in range(len(pep)-i+1):
                        pepList.append(pep[j:j+i])
      weightList=[]
      for pep in pepList:
            weight = 0
            for aa in pep:
                  weight+=weightaa[aa]
            weightList.append(weight)
      weightList.sort()
      return weightList

def createInitialList(SpectrumList):
      ListOfInitials=[]
      for spec in SpectrumList:
            if int(spec) in weightD.keys() and spec != 0:
                  ListOfInitials.append(weightD[int(spec)])
      return ListOfInitials 
            
def isConsistent (subList,SpectrumList):
      cons= True
      Temp = SpectrumList[:]
      for x in subList:
            if x not in Temp:
                  cons=False
            else:
                  Temp.remove(x)
      return cons
     
      
#Main

SpectrumList = [0,97,97,99,101,103,196,198,198,200,202,295,297,299,299,301,394,396,398,400,400,497]

initialList = createInitialList(SpectrumList)

FinalList = initialList[:]

while True:
      TempList=[]
      for p in range(len(FinalList)):
            for element in initialList: 
                  NewPep = FinalList[p]+element
                  if isConsistent(LinearSpectrum(NewPep),SpectrumList)==True:
                        TempList.append(NewPep)
      if len(TempList)!=0:
            FinalList=TempList[:]
            FinalList=list(set(FinalList)) #remove duplicates
      else:
            break

print (FinalList)

      


      
            
                  
                                       
                       
                  
