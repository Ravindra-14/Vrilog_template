import csv
print(''' input file format
direction|name|msb|lsb|
input    |a   |1   |0''')

in_file=input(" enter the input file name:")
out_file=input("enter the out put file name")
file1=[]
with open(in_file,'r') as file:
    read=csv.reader(file,delimiter=',')
    for x in read:
        file1.append(x)
##print(file1)
        
input_pins=''
output_pins=''
inout_pins=''
all_pins=''

for i in file1:
    # for input pins
    if i[0]=='input':
        if input_pins=='':
            input_pins='input'+' '+i[1]
        else:
            input_pins=input_pins+i[1]
        if(i[2]!=''):
           input_pins=input_pins+'['+i[2]+':'+i[3]+'] '+','
        else:
            input_pins=input_pins+','
            
     # for output pis 
    if i[0]=='output':
        if output_pins=='':
            output_pins='output'+' '+i[1]
        else:
            output_pins=output_pins+i[1]
        if(i[2]!=''):
            output_pins=output_pins+'['+i[2]+':'+i[3]+'] '+','
        else:
            output_pins=output_pins+','
            
    #for inout pins
    if i[0]=='inout':
        if inout_pins=='':
            inout_pins='inout'+' '+i[1]
        else:
            inout_pins=inout_pins+i[1]
        if(i[2]!=''):
           inout_pins=inout_pins+'['+i[2]+':'+i[3]+'] '+','
        else:
            inout_pins=inout_pins+','

    if i[1]!='name':
        all_pins=all_pins+i[1]+','
        
#adding ; at the last      
input_pins=input_pins[:-1:]
output_pins=output_pins[:-1:]
inout_pins=inout_pins[:-1:]
all_pins=all_pins[:-1:]
if len(input_pins)>1: input_pins=input_pins+';'
if len(output_pins)>1:output_pins=output_pins+';'
if len(inout_pins)>1:inout_pins=inout_pins+';'
#print(input_pins,output_pins,inout_pins,all_pins)

f_out=open(out_file,"a")
f_out.write("module ")
f_out.write(out_file[:out_file.index('.'):])
f_out.write("(");
f_out.write(all_pins)
f_out.write(");\n")
f_out.write(input_pins)
f_out.write("\n")
f_out.write(output_pins)
f_out.write("\n")
f_out.write(inout_pins)
f_out.write("\n")
f_out.write("#write your code here\n endmodule")
f_out.close()




           
           
           
