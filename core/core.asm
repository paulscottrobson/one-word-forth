
		ld 		ix,Next_Instruction 
		ld 		iy,IYCode
Next_Instruction:
		ld 		a,(bc) 									; read into HL
		ld  	l,a
		inc 	bc
		ld 		a,(bc) 									
		ld 		h,a
		inc 	bc
		add 	hl,hl 									; make it into an address, bit 15 into Carry.
		jr		nc,Constant 							; bit 15 clear, it's a constant.
		jp 		(hl) 									; go there as code.
;
;	15 bit constant
;
Constant:
		sra  	h 										; make the 15 bit value a 16 bit sign extended
		rr 	 	l 										; unpicks the ADD HL,HL
		push 	hl 										; save HL (the constant) on the stack.
		jr 	 	Next_Instruction
;
;	Compiled code which is a list of words starts with this.
;
IYCode:
		ld 		a,b  									; push BC on the DE return stack.
		dec 	de
		ld		(de),a
		ld 		a,c
		dec 	de
		ld 		(de),a

		ld 		b,h 									; copy HL to BC. BC points to a JP (IY) instruction
		ld 		c,l
		inc 	bc 										; so skip over that.
		inc 	bc
		jr 		Next_Instruction 						; and do the next instruction

