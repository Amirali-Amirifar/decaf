	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 15, 0	sdk_version 15, 2
	.globl	_BS__decaf__init                ; -- Begin function BS__decaf__init
	.p2align	2
_BS__decaf__init:                       ; @BS__decaf__init
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #16
	.cfi_def_cfa_offset 16
	str	x0, [sp, #8]
	ldr	x9, [sp, #8]
	adrp	x8, _BS__decaf__init.vtable@PAGE
	add	x8, x8, _BS__decaf__init.vtable@PAGEOFF
	str	x8, [x9, #16]
	mov	w0, #0                          ; =0x0
	add	sp, sp, #16
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_BS_Start                       ; -- Begin function BS_Start
	.p2align	2
_BS_Start:                              ; @BS_Start
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
	ldur	x8, [x29, #-8]
	ldr	x8, [x8, #16]
	ldr	x8, [x8, #40]
	ldur	x0, [x29, #-8]
	ldur	w1, [x29, #-12]
	blr	x8
	str	w0, [sp, #16]
	ldur	x8, [x29, #-8]
	ldr	x8, [x8, #16]
	ldr	x8, [x8, #32]
	ldur	x0, [x29, #-8]
	blr	x8
	str	w0, [sp, #12]
	ldur	x8, [x29, #-8]
	ldr	x8, [x8, #16]
	ldr	x8, [x8, #8]
	ldur	x0, [x29, #-8]
	mov	w1, #8                          ; =0x8
	blr	x8
	tbz	w0, #0, LBB1_2
	b	LBB1_1
LBB1_1:
	mov	x9, sp
	mov	x8, #1                          ; =0x1
	str	x8, [x9]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	b	LBB1_3
LBB1_2:
	mov	x8, sp
	str	xzr, [x8]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	b	LBB1_3
LBB1_3:
	ldur	x8, [x29, #-8]
	ldr	x8, [x8, #16]
	ldr	x8, [x8, #8]
	ldur	x0, [x29, #-8]
	mov	w1, #19                         ; =0x13
	blr	x8
	tbz	w0, #0, LBB1_5
	b	LBB1_4
LBB1_4:
	mov	x9, sp
	mov	x8, #1                          ; =0x1
	str	x8, [x9]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	b	LBB1_6
LBB1_5:
	mov	x8, sp
	str	xzr, [x8]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	b	LBB1_6
LBB1_6:
	ldur	x8, [x29, #-8]
	ldr	x8, [x8, #16]
	ldr	x8, [x8, #8]
	ldur	x0, [x29, #-8]
	mov	w1, #20                         ; =0x14
	blr	x8
	tbz	w0, #0, LBB1_8
	b	LBB1_7
LBB1_7:
	mov	x9, sp
	mov	x8, #1                          ; =0x1
	str	x8, [x9]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	b	LBB1_9
LBB1_8:
	mov	x8, sp
	str	xzr, [x8]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	b	LBB1_9
LBB1_9:
	ldur	x8, [x29, #-8]
	ldr	x8, [x8, #16]
	ldr	x8, [x8, #8]
	ldur	x0, [x29, #-8]
	mov	w1, #21                         ; =0x15
	blr	x8
	tbz	w0, #0, LBB1_11
	b	LBB1_10
LBB1_10:
	mov	x9, sp
	mov	x8, #1                          ; =0x1
	str	x8, [x9]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	b	LBB1_12
LBB1_11:
	mov	x8, sp
	str	xzr, [x8]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	b	LBB1_12
LBB1_12:
	ldur	x8, [x29, #-8]
	ldr	x8, [x8, #16]
	ldr	x8, [x8, #8]
	ldur	x0, [x29, #-8]
	mov	w1, #37                         ; =0x25
	blr	x8
	tbz	w0, #0, LBB1_14
	b	LBB1_13
LBB1_13:
	mov	x9, sp
	mov	x8, #1                          ; =0x1
	str	x8, [x9]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	b	LBB1_15
LBB1_14:
	mov	x8, sp
	str	xzr, [x8]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	b	LBB1_15
LBB1_15:
	ldur	x8, [x29, #-8]
	ldr	x8, [x8, #16]
	ldr	x8, [x8, #8]
	ldur	x0, [x29, #-8]
	mov	w1, #38                         ; =0x26
	blr	x8
	tbz	w0, #0, LBB1_17
	b	LBB1_16
LBB1_16:
	mov	x9, sp
	mov	x8, #1                          ; =0x1
	str	x8, [x9]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	b	LBB1_18
LBB1_17:
	mov	x8, sp
	str	xzr, [x8]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	b	LBB1_18
LBB1_18:
	ldur	x8, [x29, #-8]
	ldr	x8, [x8, #16]
	ldr	x8, [x8, #8]
	ldur	x0, [x29, #-8]
	mov	w1, #39                         ; =0x27
	blr	x8
	tbz	w0, #0, LBB1_20
	b	LBB1_19
LBB1_19:
	mov	x9, sp
	mov	x8, #1                          ; =0x1
	str	x8, [x9]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	b	LBB1_21
LBB1_20:
	mov	x8, sp
	str	xzr, [x8]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	b	LBB1_21
LBB1_21:
	ldur	x8, [x29, #-8]
	ldr	x8, [x8, #16]
	ldr	x8, [x8, #8]
	ldur	x0, [x29, #-8]
	mov	w1, #50                         ; =0x32
	blr	x8
	tbz	w0, #0, LBB1_23
	b	LBB1_22
LBB1_22:
	mov	x9, sp
	mov	x8, #1                          ; =0x1
	str	x8, [x9]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	b	LBB1_24
LBB1_23:
	mov	x8, sp
	str	xzr, [x8]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	b	LBB1_24
LBB1_24:
	mov	w0, #999                        ; =0x3e7
	ldp	x29, x30, [sp, #32]             ; 16-byte Folded Reload
	add	sp, sp, #48
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_BS_Search                      ; -- Begin function BS_Search
	.p2align	2
_BS_Search:                             ; @BS_Search
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #64
	stp	x29, x30, [sp, #48]             ; 16-byte Folded Spill
	add	x29, sp, #48
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	stur	x0, [x29, #-8]
	stur	w1, [x29, #-12]
	str	wzr, [sp, #12]
	sturb	wzr, [x29, #-13]
	ldur	x8, [x29, #-8]
	ldr	x0, [x8]
	bl	_array_length
	stur	w0, [x29, #-20]
	ldur	w8, [x29, #-20]
	subs	w8, w8, #1
	stur	w8, [x29, #-20]
	str	wzr, [sp, #24]
	mov	w8, #1                          ; =0x1
	strb	w8, [sp, #23]
	b	LBB2_1
LBB2_1:                                 ; =>This Inner Loop Header: Depth=1
	ldrb	w8, [sp, #23]
	tbz	w8, #0, LBB2_12
	b	LBB2_2
LBB2_2:                                 ;   in Loop: Header=BB2_1 Depth=1
	ldr	w8, [sp, #24]
	ldur	w9, [x29, #-20]
	add	w8, w8, w9
	str	w8, [sp, #16]
	ldur	x8, [x29, #-8]
	ldr	x8, [x8, #16]
	ldr	x8, [x8, #16]
	ldur	x0, [x29, #-8]
	ldr	w1, [sp, #16]
	blr	x8
	str	w0, [sp, #16]
	ldur	x8, [x29, #-8]
	ldr	x0, [x8]
	ldr	w1, [sp, #16]
	bl	_array_at
	ldr	w8, [x0]
	str	w8, [sp, #12]
	ldur	w8, [x29, #-12]
	ldr	w9, [sp, #12]
	subs	w8, w8, w9
	cset	w8, ge
	tbnz	w8, #0, LBB2_4
	b	LBB2_3
LBB2_3:                                 ;   in Loop: Header=BB2_1 Depth=1
	ldr	w8, [sp, #16]
	subs	w8, w8, #1
	stur	w8, [x29, #-20]
	b	LBB2_5
LBB2_4:                                 ;   in Loop: Header=BB2_1 Depth=1
	ldr	w8, [sp, #16]
	add	w8, w8, #1
	str	w8, [sp, #24]
	b	LBB2_5
LBB2_5:                                 ;   in Loop: Header=BB2_1 Depth=1
	ldur	x8, [x29, #-8]
	ldr	x8, [x8, #16]
	ldr	x8, [x8, #24]
	ldur	x0, [x29, #-8]
	ldr	w1, [sp, #12]
	ldur	w2, [x29, #-12]
	blr	x8
	tbz	w0, #0, LBB2_7
	b	LBB2_6
LBB2_6:                                 ;   in Loop: Header=BB2_1 Depth=1
	strb	wzr, [sp, #23]
	b	LBB2_8
LBB2_7:                                 ;   in Loop: Header=BB2_1 Depth=1
	mov	w8, #1                          ; =0x1
	strb	w8, [sp, #23]
	b	LBB2_8
LBB2_8:                                 ;   in Loop: Header=BB2_1 Depth=1
	ldur	w8, [x29, #-20]
	ldr	w9, [sp, #24]
	subs	w8, w8, w9
	cset	w8, ge
	tbnz	w8, #0, LBB2_10
	b	LBB2_9
LBB2_9:                                 ;   in Loop: Header=BB2_1 Depth=1
	strb	wzr, [sp, #23]
	b	LBB2_11
LBB2_10:                                ;   in Loop: Header=BB2_1 Depth=1
	str	wzr, [sp, #8]
	b	LBB2_11
LBB2_11:                                ;   in Loop: Header=BB2_1 Depth=1
	b	LBB2_1
LBB2_12:
	ldur	x8, [x29, #-8]
	ldr	x8, [x8, #16]
	ldr	x8, [x8, #24]
	ldur	x0, [x29, #-8]
	ldr	w1, [sp, #12]
	ldur	w2, [x29, #-12]
	blr	x8
	tbz	w0, #0, LBB2_14
	b	LBB2_13
LBB2_13:
	mov	w8, #1                          ; =0x1
	sturb	w8, [x29, #-13]
	b	LBB2_15
LBB2_14:
	sturb	wzr, [x29, #-13]
	b	LBB2_15
LBB2_15:
	ldurb	w8, [x29, #-13]
	and	w0, w8, #0x1
	ldp	x29, x30, [sp, #48]             ; 16-byte Folded Reload
	add	sp, sp, #64
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_BS_Div                         ; -- Begin function BS_Div
	.p2align	2
_BS_Div:                                ; @BS_Div
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #32
	.cfi_def_cfa_offset 32
	str	x0, [sp, #24]
	str	w1, [sp, #20]
	str	wzr, [sp, #16]
	str	wzr, [sp, #12]
	ldr	w8, [sp, #20]
	subs	w8, w8, #1
	str	w8, [sp, #8]
	b	LBB3_1
LBB3_1:                                 ; =>This Inner Loop Header: Depth=1
	ldr	w8, [sp, #12]
	ldr	w9, [sp, #8]
	subs	w8, w8, w9
	cset	w8, ge
	tbnz	w8, #0, LBB3_3
	b	LBB3_2
LBB3_2:                                 ;   in Loop: Header=BB3_1 Depth=1
	ldr	w8, [sp, #16]
	add	w8, w8, #1
	str	w8, [sp, #16]
	ldr	w8, [sp, #12]
	add	w8, w8, #2
	str	w8, [sp, #12]
	b	LBB3_1
LBB3_3:
	ldr	w0, [sp, #16]
	add	sp, sp, #32
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_BS_Compare                     ; -- Begin function BS_Compare
	.p2align	2
_BS_Compare:                            ; @BS_Compare
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #32
	.cfi_def_cfa_offset 32
	str	x0, [sp, #24]
	str	w1, [sp, #20]
	str	w2, [sp, #16]
	strb	wzr, [sp, #15]
	ldr	w8, [sp, #16]
	add	w8, w8, #1
	str	w8, [sp, #8]
	ldr	w8, [sp, #20]
	ldr	w9, [sp, #16]
	subs	w8, w8, w9
	cset	w8, ge
	tbnz	w8, #0, LBB4_2
	b	LBB4_1
LBB4_1:
	strb	wzr, [sp, #15]
	b	LBB4_6
LBB4_2:
	ldr	w8, [sp, #20]
	ldr	w9, [sp, #8]
	subs	w8, w8, w9
	cset	w8, lt
	tbnz	w8, #0, LBB4_4
	b	LBB4_3
LBB4_3:
	strb	wzr, [sp, #15]
	b	LBB4_5
LBB4_4:
	mov	w8, #1                          ; =0x1
	strb	w8, [sp, #15]
	b	LBB4_5
LBB4_5:
	b	LBB4_6
LBB4_6:
	ldrb	w8, [sp, #15]
	and	w0, w8, #0x1
	add	sp, sp, #32
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_BS_Print                       ; -- Begin function BS_Print
	.p2align	2
_BS_Print:                              ; @BS_Print
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #48
	stp	x29, x30, [sp, #32]             ; 16-byte Folded Spill
	add	x29, sp, #32
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	stur	x0, [x29, #-8]
	mov	w8, #1                          ; =0x1
	stur	w8, [x29, #-12]
	b	LBB5_1
LBB5_1:                                 ; =>This Inner Loop Header: Depth=1
	ldur	w8, [x29, #-12]
	ldur	x9, [x29, #-8]
	ldr	w9, [x9, #8]
	subs	w8, w8, w9
	cset	w8, ge
	tbnz	w8, #0, LBB5_3
	b	LBB5_2
LBB5_2:                                 ;   in Loop: Header=BB5_1 Depth=1
	ldur	x8, [x29, #-8]
	ldr	x0, [x8]
	ldur	w1, [x29, #-12]
	bl	_array_at
	ldr	w9, [x0]
                                        ; implicit-def: $x8
	mov	x8, x9
	mov	x9, sp
	str	x8, [x9]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	ldur	w8, [x29, #-12]
	add	w8, w8, #1
	stur	w8, [x29, #-12]
	b	LBB5_1
LBB5_3:
	mov	x9, sp
	mov	x8, #34463                      ; =0x869f
	movk	x8, #1, lsl #16
	str	x8, [x9]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	mov	w0, #0                          ; =0x0
	ldp	x29, x30, [sp, #32]             ; 16-byte Folded Reload
	add	sp, sp, #48
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_BS_Init                        ; -- Begin function BS_Init
	.p2align	2
_BS_Init:                               ; @BS_Init
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
	ldur	x9, [x29, #-8]
	str	w8, [x9, #8]
	ldur	w0, [x29, #-12]
	bl	_create_array
	ldur	x8, [x29, #-8]
	str	x0, [x8]
	mov	w8, #1                          ; =0x1
	str	w8, [sp, #16]
	ldur	x8, [x29, #-8]
	ldr	w8, [x8, #8]
	add	w8, w8, #1
	str	w8, [sp, #12]
	b	LBB6_1
LBB6_1:                                 ; =>This Inner Loop Header: Depth=1
	ldr	w8, [sp, #16]
	ldur	x9, [x29, #-8]
	ldr	w9, [x9, #8]
	subs	w8, w8, w9
	cset	w8, ge
	tbnz	w8, #0, LBB6_3
	b	LBB6_2
LBB6_2:                                 ;   in Loop: Header=BB6_1 Depth=1
	ldr	w9, [sp, #16]
	mov	w8, #2                          ; =0x2
	mul	w8, w8, w9
	str	w8, [sp, #4]
	ldr	w8, [sp, #12]
	subs	w8, w8, #3
	str	w8, [sp, #8]
	ldr	w8, [sp, #4]
	ldr	w9, [sp, #8]
	add	w8, w8, w9
	ldur	x9, [x29, #-8]
	ldr	x9, [x9]
	ldr	x9, [x9]
	ldrsw	x10, [sp, #16]
	str	w8, [x9, x10, lsl #2]
	ldr	w8, [sp, #16]
	add	w8, w8, #1
	str	w8, [sp, #16]
	ldr	w8, [sp, #12]
	subs	w8, w8, #1
	str	w8, [sp, #12]
	b	LBB6_1
LBB6_3:
	mov	w0, #0                          ; =0x0
	ldp	x29, x30, [sp, #32]             ; 16-byte Folded Reload
	add	sp, sp, #48
	ret
	.cfi_endproc
                                        ; -- End function
	.p2align	2                               ; -- Begin function array_length
_array_length:                          ; @array_length
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #32
	stp	x29, x30, [sp, #16]             ; 16-byte Folded Spill
	add	x29, sp, #16
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	str	x0, [sp, #8]
	ldr	x8, [sp, #8]
	subs	x8, x8, #0
	cset	w8, ne
	tbnz	w8, #0, LBB7_2
	b	LBB7_1
LBB7_1:
	adrp	x0, l_.str.1@PAGE
	add	x0, x0, l_.str.1@PAGEOFF
	bl	_printf
	mov	w0, #1                          ; =0x1
	bl	_exit
LBB7_2:
	ldr	x8, [sp, #8]
	ldr	w0, [x8, #8]
	ldp	x29, x30, [sp, #16]             ; 16-byte Folded Reload
	add	sp, sp, #32
	ret
	.cfi_endproc
                                        ; -- End function
	.p2align	2                               ; -- Begin function array_at
_array_at:                              ; @array_at
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
	ldur	x8, [x29, #-8]
	subs	x8, x8, #0
	cset	w8, ne
	tbnz	w8, #0, LBB8_2
	b	LBB8_1
LBB8_1:
	adrp	x0, l_.str.1@PAGE
	add	x0, x0, l_.str.1@PAGEOFF
	bl	_printf
	mov	w0, #1                          ; =0x1
	bl	_exit
LBB8_2:
	ldur	w8, [x29, #-12]
	subs	w8, w8, #0
	cset	w8, lt
	tbnz	w8, #0, LBB8_4
	b	LBB8_3
LBB8_3:
	ldur	w8, [x29, #-12]
	ldur	x9, [x29, #-8]
	ldr	w9, [x9, #8]
	subs	w8, w8, w9
	cset	w8, lt
	tbnz	w8, #0, LBB8_5
	b	LBB8_4
LBB8_4:
	ldur	w9, [x29, #-12]
                                        ; implicit-def: $x8
	mov	x8, x9
	mov	x9, sp
	str	x8, [x9]
	adrp	x0, l_.str.2@PAGE
	add	x0, x0, l_.str.2@PAGEOFF
	bl	_printf
	mov	w0, #1                          ; =0x1
	bl	_exit
LBB8_5:
	ldur	x8, [x29, #-8]
	ldr	x8, [x8]
	ldursw	x9, [x29, #-12]
	add	x0, x8, x9, lsl #2
	ldp	x29, x30, [sp, #32]             ; 16-byte Folded Reload
	add	sp, sp, #48
	ret
	.cfi_endproc
                                        ; -- End function
	.p2align	2                               ; -- Begin function create_array
_create_array:                          ; @create_array
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #48
	stp	x29, x30, [sp, #32]             ; 16-byte Folded Spill
	add	x29, sp, #32
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	stur	w0, [x29, #-4]
	ldur	w8, [x29, #-4]
	subs	w8, w8, #0
	cset	w8, ge
	tbnz	w8, #0, LBB9_2
	b	LBB9_1
LBB9_1:
	adrp	x0, l_.str.3@PAGE
	add	x0, x0, l_.str.3@PAGEOFF
	bl	_printf
	mov	w0, #1                          ; =0x1
	bl	_exit
LBB9_2:
	mov	x0, #16                         ; =0x10
	bl	_malloc
	str	x0, [sp, #16]
	ldr	x8, [sp, #16]
	subs	x8, x8, #0
	cset	w8, ne
	tbnz	w8, #0, LBB9_4
	b	LBB9_3
LBB9_3:
	adrp	x0, l_.str.4@PAGE
	add	x0, x0, l_.str.4@PAGEOFF
	bl	_printf
	mov	w0, #1                          ; =0x1
	bl	_exit
LBB9_4:
	ldursw	x8, [x29, #-4]
	lsl	x0, x8, #2
	bl	_malloc
	ldr	x8, [sp, #16]
	str	x0, [x8]
	ldr	x8, [sp, #16]
	ldr	x8, [x8]
	subs	x8, x8, #0
	cset	w8, ne
	tbnz	w8, #0, LBB9_6
	b	LBB9_5
LBB9_5:
	ldr	x0, [sp, #16]
	bl	_free
	adrp	x0, l_.str.5@PAGE
	add	x0, x0, l_.str.5@PAGEOFF
	bl	_printf
	mov	w0, #1                          ; =0x1
	bl	_exit
LBB9_6:
	str	wzr, [sp, #12]
	b	LBB9_7
LBB9_7:                                 ; =>This Inner Loop Header: Depth=1
	ldr	w8, [sp, #12]
	ldur	w9, [x29, #-4]
	subs	w8, w8, w9
	cset	w8, ge
	tbnz	w8, #0, LBB9_10
	b	LBB9_8
LBB9_8:                                 ;   in Loop: Header=BB9_7 Depth=1
	ldr	x8, [sp, #16]
	ldr	x9, [x8]
	ldrsw	x10, [sp, #12]
	mov	w8, #0                          ; =0x0
	str	w8, [x9, x10, lsl #2]
	b	LBB9_9
LBB9_9:                                 ;   in Loop: Header=BB9_7 Depth=1
	ldr	w8, [sp, #12]
	add	w8, w8, #1
	str	w8, [sp, #12]
	b	LBB9_7
LBB9_10:
	ldur	w8, [x29, #-4]
	ldr	x9, [sp, #16]
	str	w8, [x9, #8]
	ldr	x0, [sp, #16]
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
	mov	x0, #24                         ; =0x18
	bl	_malloc
	str	x0, [sp, #24]
	ldr	x0, [sp, #24]
	bl	_BS__decaf__init
	ldr	x8, [sp, #24]
	ldr	x8, [x8, #16]
	ldr	x8, [x8]
	ldr	x0, [sp, #24]
	mov	w1, #20                         ; =0x14
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
	.p2align	3, 0x0                          ; @BS__decaf__init.vtable
_BS__decaf__init.vtable:
	.quad	_BS_Start
	.quad	_BS_Search
	.quad	_BS_Div
	.quad	_BS_Compare
	.quad	_BS_Print
	.quad	_BS_Init

	.section	__TEXT,__cstring,cstring_literals
l_.str:                                 ; @.str
	.asciz	"%d\n"

l_.str.1:                               ; @.str.1
	.asciz	"Null array reference\n"

l_.str.2:                               ; @.str.2
	.asciz	"Array index out of bounds: %d\n"

l_.str.3:                               ; @.str.3
	.asciz	"Invalid array size\n"

l_.str.4:                               ; @.str.4
	.asciz	"Failed to allocate array wrapper\n"

l_.str.5:                               ; @.str.5
	.asciz	"Failed to allocate array data\n"

.subsections_via_symbols
