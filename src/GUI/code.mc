~data
0x10000000 0x1
0x10000004 0x2
0x10000008 0x3
0x1000000C 0x4
~text
0x0	0x10000537	#lui x10 65536	li x10,0x10000000
0x4 0x00000033
0x8 0x00000033
0xC 0x00000033
0x10	0x00050513	##addi x10 x10 0	li x10,0x10000000
0x14	0x0002A283	#lw x5 0(x5)	lw x5,0(x5)
0x18	0x0042A303	#lw x6 4(x5)	lw x6,4(x5)
0x1C	0x0082A383	#lw x7 8(x5)	lw x7,8(x5)
0x20	0x00C2A403	#lw x8 12(x5)	lw x8,12(x5)
0x24	0x00628A63	##beq x5 x6 20	beq x5, x6, case1
0x28	0x00728C63	#beq x5 x7 24	beq x5, x7, case2
0x2C	0x00828E63	#beq x5 x8 28	beq x5, x8, case3
0x30	0x00100493	#addi x9 x0 1	li x9, 1
0x34	0x00000C63	#beq x0 x0 24	beq x0, x0, exit
0x38	0x00130313	#addi x6 x6 1	addi x6, x6, 1
0x3C	0x00000863	#beq x0 x0 16	beq x0, x0, exit
0x40	0x00138393	#addi x7 x7 1	addi x7, x7, 1
0x44	0x00000463	#beq x0 x0 8	beq x0, x0, exit
0x48	0x00140493	#addi x9 x8 1	addi x9, x8, 1
0x4C	0x00000033
0x50 0x11