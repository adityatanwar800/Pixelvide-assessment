from django.shortcuts import render
from django.conf import settings
import random
from django.http import HttpResponse

def home(request):
    club=['Arsenal','Astana','Atletico','Bate','CSKA','Dinamo Zagreb','Dynamo Kyiv','Galatasaravy','Gent','Leverkusevn','Lyon','M. Tel-Aviv','Malmo','Man.City','Man. United','Mochengladbach','Olampiacos','Porto','Real Mardrid','Roma','Sevilia','Sakhtar','Valencia','Wolfsburg']
    winning_club=['Barcelona','Bayern','Benfica','Chelsa','Juventus','Paris','PSV','Zenit']
    A=[]
    B=[]
    C=[]
    D=[]
    E=[]
    F=[]
    G=[]
    H=[]
    temp1=club[:]
    temp2=winning_club[:]
    for i in range(0,3):
        temp1=club[:]
        temp2=winning_club[:]
        if i==0:
            winn_count=random.choice(temp2)
            count=random.choice(temp1)
            A.append(winn_count)
            A.append(count)
            temp1.remove(count)
            temp2.remove(winn_count)
            
            winn_count=random.choice(temp2)
            count=random.choice(temp1)
            B.append(winn_count)
            B.append(count)
            temp1.remove(count)
            temp2.remove(winn_count)

            winn_count=random.choice(temp2)
            count=random.choice(temp1)
            C.append(winn_count)
            C.append(count)
            temp1.remove(count)
            temp2.remove(winn_count)

            
            winn_count=random.choice(temp2)
            count=random.choice(temp1)
            D.append(winn_count)
            D.append(count)
            temp1.remove(count)
            temp2.remove(winn_count)
            
            winn_count=random.choice(temp2)
            count=random.choice(temp1)
            E.append(winn_count)
            E.append(count)
            temp1.remove(count)
            temp2.remove(winn_count)
            
            winn_count=random.choice(temp2)
            count=random.choice(temp1)
            F.append(winn_count)
            F.append(count)
            temp1.remove(count)
            temp2.remove(winn_count)
            
            winn_count=random.choice(temp2)
            count=random.choice(temp1)
            G.append(winn_count)
            G.append(count)
            temp1.remove(count)
            temp2.remove(winn_count)
            
            
            winn_count=random.choice(temp2)
            count=random.choice(temp1)
            H.append(winn_count)
            H.append(count)
            temp1.remove(count)
            temp2.remove(winn_count)
            
        else:
            
            
            count=random.choice(temp1)
            A.append(count)
            temp1.remove(count)
            
            
            count=random.choice(temp1)
            B.append(count)
            temp1.remove(count)
            
            
            count=random.choice(temp1)
            C.append(count)
            temp1.remove(count)
            
            
            count=random.choice(temp1)
            D.append(count)
            temp1.remove(count)
            
            
            count=random.choice(temp1)
            E.append(count)
            temp1.remove(count)
            
            
            count=random.choice(temp1)
            F.append(count)
            temp1.remove(count)
            
            
            count=random.choice(temp1)
            G.append(count)
            temp1.remove(count)
            
    
            count=random.choice(temp1)
            H.append(count)
            temp1.remove(count)
        

    return render(request,'base/main.html',{'t1':A,'t2':B,'t3':C,'t4':D,'t5':E,'t6':F,'t7':G,'t8':H})