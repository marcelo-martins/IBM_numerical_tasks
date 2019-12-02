	.file	"helloworld.c"
	.abiversion 2
	.section	".text"
	.section	.rodata
	.align 3
.LC0:
	.string	"Hello World!"
	.section	".text"
	.align 2
	.globl main
	.type	main, @function
main:
.LCF0:
0:	addis 2,12,.TOC.-.LCF0@ha
	addi 2,2,.TOC.-.LCF0@l
	.localentry	main,.-main
	mflr 0
	std 0,16(1)
	std 31,-8(1)
	stdu 1,-48(1)
	mr 31,1
	addis 3,2,.LC0@toc@ha
	addi 3,3,.LC0@toc@l
	bl puts
	nop
	li 9,0
	mr 3,9
	addi 1,31,48
	ld 0,16(1)
	mtlr 0
	ld 31,-8(1)
	blr
	.long 0
	.byte 0,0,0,1,128,1,0,1
	.size	main,.-main
	.ident	"GCC: (Ubuntu 7.4.0-1ubuntu1~18.04.1) 7.4.0"
	.section	.note.GNU-stack,"",@progbits
