#! /usr/bin/python

import os, sys, math, string

#in_file = open ('RT-HB-tutto.dat','r')
#out_file = open ('lifetime.dat','w')

content = sys.stdin.readlines() 
nline = len (content)


#######################################################################################
# definte variables
d_pair = {} #dictionary containing unique hb pairs
list_row_frame = []
n = 0
list_AB = []
z = 0


#######################################################################################
# get total number of frame n

for  i in range(0,nline):
    row = content[i].rstrip()
    if row[:3] == '###':
        list_row_frame.append(i+1) #i+1 to get the actual row number in text file because python count from row zero 
        n = n + 1
list_row_frame.append(nline+1)
#print n
#print list_row_frame

#######################################################################################
# get list of unique hb pairs occurred

for i in range (0, nline):
    row = content[i].rstrip()
    if row[:3] != '###': 
        index_1 = row.split()[0]
        #print index_1
        index_2 = row.split()[1]
        #print index_2
        atom_1 = row.split()[2]
        #print atom_1
        atom_2 = row.split()[3]
        #print atom_2
    
        if atom_1 == 'O':
            wat_atom = atom_1
            wat_index = index_1
            cel_atom = atom_2
            cel_index = index_2
        if atom_2 == 'O':
            wat = atom_2
            wat_index = index_2
            cel_atom = atom_1
            cel_index = index_1
        pair = str(cel_index+' '+wat_index)
        #print pair for debug
        if pair not in d_pair:
            d_pair[pair] = pair

#print len(d_pair)

#######################################################################################
# convert dictionary into list, which contains unique pairs
list_pair = d_pair.values()
#list_pair.sort()
#print len(list_pair)
#print list_pair


######################################################################################
# cycle through length of list_pair and calulate lifetime for each unique pair

for j in range (0, len(list_pair)):
#for j in range (0, 1):
    sum_top = 0.0
    sum_bottom = 0.0
    pair_AB = list_pair[j].rstrip()
    #cel_indexA = pair.split()[0]
    #wat_indexB = pair.split()[1]
    #print cel_index
    #print wat_index
    #print pair_AB
    list_AB = []  
    for k in range (0, len(list_row_frame)-1):
        frame_start = list_row_frame[k]
        frame_end = list_row_frame[k+1] - 2
        d_frame_pair = {}
        for l in range (frame_start, frame_end+1):
            row = content[l].rstrip()
            #print row
            index_1 = row.split()[0]
            index_2 = row.split()[1]
            atom_1 = row.split()[2]
            atom_2 = row.split()[3]

            if atom_1 == 'O':
                wat_atom = atom_1
                wat_index = index_1
                cel_atom = atom_2
                cel_index = index_2
            if atom_2 == 'O':
                wat = atom_2
                wat_index = index_2
                cel_atom = atom_1
                cel_index = index_1
           
            pair = str(cel_index+' '+wat_index)
            d_frame_pair[pair] = pair

            if pair_AB in d_frame_pair:
                m = 1
            else:
                m = 0
        list_AB.append(m)
    #print len(list_AB)
    #print list_AB

    

######################################################################################
# get estimate on hbond lifetime using correlation function
    
    #print sum_top
    #print sum_bottom
 
    y = 1    
    while y < len(list_AB):
        sum = 0.0
        x = 0
        while x < len(list_AB)-y:
            sum = sum + (list_AB[x]*list_AB[x+y])/float((len(list_AB)-y))
            #print sum
            x = x + 1
        #term_top.append(sum)
        sum_top = sum_top + sum
        y = y + 1
        #print str(y)+' '+str(x)

    #print sum_top
 
    sum2 = 0.0
    z = 0
    while z < len(list_AB):
        sum2 = sum2 + list_AB[z]*list_AB[z]
        #print sum2
        #print z
        z = z + 1
    #print sum2

        #print list_AB
    sum_bottom = sum2/len(list_AB)
        #print sum_bottom    
    
    #print sum_top
    #print sum_bottom
    lifetime = sum_top/sum_bottom
    #print lifetime
    #out_file.write(pair_AB+' '+str(lifetime)+'\n')
    sys.stdout.write(pair_AB+' '+str(lifetime)+'\n')   
    sys.stdout.flush()
#out_file.close()
#in_file.close()





