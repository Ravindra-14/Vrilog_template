import csv
print('''input file :
input|in_bits|output|out_bits|inout|inout-bits
a    3         b     3         c     4         ''')
in_file=input(" enter the input file name:")
out_file=input("enter the out put file name")
file1=[]
with open(in_file,'r') as file:
    read=csv.reader(file,delimiter=',')
    for x in read:
        file1.append(x)
end=['','','','','','']
file1.append(end)
##print(file1)
str1=''
str2=''
str3=''
str4=''
for i in file1:
    if i[0]!='input':
        if i[0]!='':
            str4=str4+i[0]+','
            if str1=='':
                str1='input'+' '+i[0]
            else:
                str1=str1+i[0]
            if(i[1]!='1'):
                str1=str1+'['+str(int(i[1])-1)+':0]'+','
            else:
                str1=str1+','
        if i[2]!='':
            str4=str4+i[2]+','
            if str2=='':
                str2='0utput'+' '+i[2]
            else:
                str2=str2+i[2]
            if(i[3]!='1'):
                str2=str2+'['+str(int(i[3])-1)+':0]'+','
            else:
                str2=str2+','
        if i[4]!='':
            str4=str4+i[4]+','
            if str3=='':
                str3='inout'+' '+i[4]
            else:
                str3=str3+i[2]
            if(i[5]!='1'):
                str3=str3+'['+str(int(i[5])-1)+':0]'+','
            else:
                str3=str3+','
str1=str1[:-1:]
str2=str2[:-1:]
str3=str3[:-1:]
str4=str4[:-1:]
if len(str1)>1: str1=str1+';'
if len(str2)>1:str2=str2+';'
if len(str3)>1:str3=str3+';'      
print(str1,str2,str3,str4)

f_out=open(out_file,"a")
f_out.write("module ")
f_out.write(out_file[:out_file.index('.'):])
f_out.write("(");
f_out.write(str4)
f_out.write(");\n")
f_out.write(str1)
f_out.write("\n")
f_out.write(str2)
f_out.write("\n")
f_out.write(str3)
f_out.write("\n")
f_out.write("#write your code here\n endmodule")
f_out.close()

    
            
