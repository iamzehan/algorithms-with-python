N=int(input())
M=N*3
c1='.|.'
c2='-'
word='WELCOME'
l=len(c1)
dash=(M-l)//2
middle=N//2
count=0
count1=1
for line in range(0,N+1):
    if line<(middle):
        print(((dash-count)*c2)+count1*c1+((dash-count)*c2))
        count1+=2
        count+=l
    elif line==(middle):
        d_num=((M-len(word))//2)
        print(c2*d_num+word+d_num*c2)
        count1-=2
        count-=l
    elif middle<line<=N:
        if count<0:
            break
        print(((dash-count)*c2)+count1*c1+((dash-count)*c2))
        count1-=2
        count-=l