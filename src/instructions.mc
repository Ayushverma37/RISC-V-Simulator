~text
0x0	0x00C000EF	#jal x1 12	jal x1,l1
0x4	0x00500293	#addi x5 x0 5	l2: addi x5,x0,5
0x8	0x0080026F	#jal x4 8	jal x4 exit
0xc	0x00008367	#jalr x6 x1 0	l1: jalr x6, x1, 0
0x10	0x00000033	#add x0 x0 x0	exit: add x0,x0,x0
0x14 0x11