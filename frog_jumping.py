from typing import List
# Write any import statements here

def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
  # Write your code here
  time_count = 0
  loops = 0
  # loop if there are any frogs left.
  while F > 0:
    for i in range(F):
        if P[0] > P[i]:
            hold = P[0]
            P[0] = P[i]
            P[i] = hold
    # every time this function is called a second has passed and a frog has jumpped.
    time_count += 1
    # get the lowest value at the front
    loops+=1
    # as long as there is at least 2 frongs
    print("exterior loop #: " + str(time_count)) 
    print(P)
    loops1 = 0
    #jump over all frogs in a line
    if P[0]+1 in P:
        pad = P[0]
        while pad in P:
            loops1 +=1
            loops +=1
            pad +=1
            print(pad)
        P[0] = pad # set the new lilypad value
        print("interior loops: " + str(loops1))
    else: P[0] +=1
      
    # if there is only one frog get him to the end.
    # frog leaves if on the highest lilly pad\
    if N in P:
      P.remove(N)
      F -= 1   
   
  print("total loops: " + str(loops))
  return time_count

N = 6
F = 3
P = [5, 2, 4]
N2= 15
F2= 5
P2= [7, 2, 11, 14, 4]
#print("answer: " + str(getSecondsRequired(N,F,P)))

#print("loops to beat is 7")
#print("answer: " + str(getSecondsRequired(N2,F2,P2)))
#print("desired answer: 13")


#maybe I can do it by group size?
def try2(N,F,P):
    loops = 0
    P.sort()
    group = 0
    i=0
    while F >= 1:
        loops +=1
        i +=1
        if P[group] + 1 in P: #if the value ahead of this is in the group list add it to the value
            group += 1
            
        elif group > 1:
            for j in range(group): # whole grope moves forward by one. 
                print(j)
                print(P[j])
                print(P)
                P[j] += 1
        else: P[0] += 1   
        if N in P:
            P.remove(N)
            F -= 1
            group -=1 
    return loops

print("answer: " + str(try2(N,F,P)))
print("desired answer: 13")