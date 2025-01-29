	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 15, 0	sdk_version 15, 2
	.globl	_Fac__decaf__init               ; -- Begin function Fac__decaf__init
	.p2align	2
_Fac__decaf__init:                      ; @Fac__decaf__init
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #16
	.cfi_def_cfa_offset 16
	str	x0, [sp, #8]
	ldr	x9, [sp, #8]
	adrp	x8, _Fac__decaf__init.vtable@PAGE
	add	x8, x8, _Fac__decaf__init.vtable@PAGEOFF
	str	x8, [x9]
	mov	w0, #0                          ; =0x0
	add	sp, sp, #16
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_Fac_ComputeFac                 ; -- Begin function Fac_ComputeFac
	.p2align	2
_Fac_ComputeFac:                        ; @Fac_ComputeFac
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #48
	stp	x29, x30, [sp, #32]             ; 16-byte Folded Spill
	add	x29, sp, #32
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	stur	x0, [x29, #-8]
	stur	w1, [x29, #-12]
	ldur	w8, [x29, #-12]
	subs	w8, w8, #1
	cset	w8, ge
	tbnz	w8, #0, LBB1_2
	b	LBB1_1
LBB1_1:
	mov	w8, #1                          ; =0x1
	str	w8, [sp, #16]
	b	LBB1_3
LBB1_2:
	ldur	w8, [x29, #-12]
	str	w8, [sp, #12]                   ; 4-byte Folded Spill
	ldur	x8, [x29, #-8]
	ldr	x8, [x8]
	ldr	x8, [x8]
	ldur	x0, [x29, #-8]
	ldur	w9, [x29, #-12]
	subs	w1, w9, #1
	blr	x8
	ldr	w8, [sp, #12]                   ; 4-byte Folded Reload
	mul	w8, w8, w0
	str	w8, [sp, #16]
	b	LBB1_3
LBB1_3:
	ldr	w0, [sp, #16]
	ldp	x29, x30, [sp, #32]             ; 16-byte Folded Reload
	add	sp, sp, #48
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_main                           ; -- Begin function main
	.p2align	2
_main:                                  ; @main
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #64
	stp	x29, x30, [sp, #48]             ; 16-byte Folded Spill
	add	x29, sp, #48
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	mov	w8, #0                          ; =0x0
	str	w8, [sp, #20]                   ; 4-byte Folded Spill
	stur	wzr, [x29, #-4]
	stur	w0, [x29, #-8]
	stur	x1, [x29, #-16]
	mov	x0, #8                          ; =0x8
	bl	_malloc
	str	x0, [sp, #24]
	ldr	x0, [sp, #24]
	bl	_Fac__decaf__init
	ldr	x8, [sp, #24]
	ldr	x8, [x8]
	ldr	x8, [x8]
	ldr	x0, [sp, #24]
	mov	w1, #5                          ; =0x5
	blr	x8
	mov	x9, sp
                                        ; implicit-def: $x8
	mov	x8, x0
	str	x8, [x9]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	ldr	x0, [sp, #24]
	bl	_free
	ldr	w0, [sp, #20]                   ; 4-byte Folded Reload
                                        ; kill: def $x8 killed $xzr
	str	xzr, [sp, #24]
	ldp	x29, x30, [sp, #48]             ; 16-byte Folded Reload
	add	sp, sp, #64
	ret
	.cfi_endproc
                                        ; -- End function
	.section	__DATA,__data
	.p2align	3, 0x0                          ; @Fac__decaf__init.vtable
_Fac__decaf__init.vtable:
	.quad	_Fac_ComputeFac

	.section	__TEXT,__cstring,cstring_literals
l_.str:                                 ; @.str
	.asciz	"%d\n"

.subsections_via_symbols
