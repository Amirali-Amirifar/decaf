	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 15, 0	sdk_version 15, 2
	.globl	_BBS__decaf__init               ; -- Begin function BBS__decaf__init
	.p2align	2
_BBS__decaf__init:                      ; @BBS__decaf__init
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #16
	.cfi_def_cfa_offset 16
	str	x0, [sp, #8]
	ldr	x9, [sp, #8]
	adrp	x8, _BBS__decaf__init.vtable@PAGE
	add	x8, x8, _BBS__decaf__init.vtable@PAGEOFF
	str	x8, [x9, #16]
	mov	w0, #0                          ; =0x0
	add	sp, sp, #16
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_BBS_Start                      ; -- Begin function BBS_Start
	.p2align	2
_BBS_Start:                             ; @BBS_Start
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
	ldr	x8, [x8, #24]
	ldur	x0, [x29, #-8]
	ldur	w1, [x29, #-12]
	blr	x8
	str	w0, [sp, #16]
	ldur	x8, [x29, #-8]
	ldr	x8, [x8, #16]
	ldr	x8, [x8, #16]
	ldur	x0, [x29, #-8]
	blr	x8
	str	w0, [sp, #16]
	mov	x9, sp
	mov	x8, #34463                      ; =0x869f
	movk	x8, #1, lsl #16
	str	x8, [x9]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	ldur	x8, [x29, #-8]
	ldr	x8, [x8, #16]
	ldr	x8, [x8, #8]
	ldur	x0, [x29, #-8]
	blr	x8
	str	w0, [sp, #16]
	ldur	x8, [x29, #-8]
	ldr	x8, [x8, #16]
	ldr	x8, [x8, #16]
	ldur	x0, [x29, #-8]
	blr	x8
	str	w0, [sp, #16]
	mov	w0, #0                          ; =0x0
	ldp	x29, x30, [sp, #32]             ; 16-byte Folded Reload
	add	sp, sp, #48
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_BBS_Sort                       ; -- Begin function BBS_Sort
	.p2align	2
_BBS_Sort:                              ; @BBS_Sort
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #64
	stp	x29, x30, [sp, #48]             ; 16-byte Folded Spill
	add	x29, sp, #48
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	stur	x0, [x29, #-8]
	ldur	x8, [x29, #-8]
	ldr	w8, [x8, #8]
	subs	w8, w8, #1
	stur	w8, [x29, #-16]
	mov	w8, #-1                         ; =0xffffffff
	stur	w8, [x29, #-20]
	b	LBB2_1
LBB2_1:                                 ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB2_3 Depth 2
	ldur	w8, [x29, #-20]
	ldur	w9, [x29, #-16]
	subs	w8, w8, w9
	cset	w8, ge
	tbnz	w8, #0, LBB2_9
	b	LBB2_2
LBB2_2:                                 ;   in Loop: Header=BB2_1 Depth=1
	mov	w8, #1                          ; =0x1
	str	w8, [sp, #8]
	b	LBB2_3
LBB2_3:                                 ;   Parent Loop BB2_1 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	ldr	w8, [sp, #8]
	ldur	w9, [x29, #-16]
	add	w9, w9, #1
	subs	w8, w8, w9
	cset	w8, ge
	tbnz	w8, #0, LBB2_8
	b	LBB2_4
LBB2_4:                                 ;   in Loop: Header=BB2_3 Depth=2
	ldr	w8, [sp, #8]
	subs	w8, w8, #1
	str	w8, [sp, #12]
	ldur	x8, [x29, #-8]
	ldr	x0, [x8]
	ldr	w1, [sp, #12]
	bl	_array_at
	ldr	w8, [x0]
	str	w8, [sp, #24]
	ldur	x8, [x29, #-8]
	ldr	x0, [x8]
	ldr	w1, [sp, #8]
	bl	_array_at
	ldr	w8, [x0]
	str	w8, [sp, #20]
	ldr	w8, [sp, #20]
	ldr	w9, [sp, #24]
	subs	w8, w8, w9
	cset	w8, ge
	tbnz	w8, #0, LBB2_6
	b	LBB2_5
LBB2_5:                                 ;   in Loop: Header=BB2_3 Depth=2
	ldr	w8, [sp, #8]
	subs	w8, w8, #1
	str	w8, [sp, #16]
	ldur	x8, [x29, #-8]
	ldr	x0, [x8]
	ldr	w1, [sp, #16]
	bl	_array_at
	ldr	w8, [x0]
	str	w8, [sp, #4]
	ldur	x8, [x29, #-8]
	ldr	x0, [x8]
	ldr	w1, [sp, #8]
	bl	_array_at
	ldr	w8, [x0]
	ldur	x9, [x29, #-8]
	ldr	x9, [x9]
	ldr	x9, [x9]
	ldrsw	x10, [sp, #16]
	str	w8, [x9, x10, lsl #2]
	ldr	w8, [sp, #4]
	ldur	x9, [x29, #-8]
	ldr	x9, [x9]
	ldr	x9, [x9]
	ldrsw	x10, [sp, #8]
	str	w8, [x9, x10, lsl #2]
	b	LBB2_7
LBB2_6:                                 ;   in Loop: Header=BB2_3 Depth=2
	stur	wzr, [x29, #-12]
	b	LBB2_7
LBB2_7:                                 ;   in Loop: Header=BB2_3 Depth=2
	ldr	w8, [sp, #8]
	add	w8, w8, #1
	str	w8, [sp, #8]
	b	LBB2_3
LBB2_8:                                 ;   in Loop: Header=BB2_1 Depth=1
	ldur	w8, [x29, #-16]
	subs	w8, w8, #1
	stur	w8, [x29, #-16]
	b	LBB2_1
LBB2_9:
	mov	w0, #0                          ; =0x0
	ldp	x29, x30, [sp, #48]             ; 16-byte Folded Reload
	add	sp, sp, #64
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_BBS_Print                      ; -- Begin function BBS_Print
	.p2align	2
_BBS_Print:                             ; @BBS_Print
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #48
	stp	x29, x30, [sp, #32]             ; 16-byte Folded Spill
	add	x29, sp, #32
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	stur	x0, [x29, #-8]
	stur	wzr, [x29, #-12]
	b	LBB3_1
LBB3_1:                                 ; =>This Inner Loop Header: Depth=1
	ldur	w8, [x29, #-12]
	ldur	x9, [x29, #-8]
	ldr	w9, [x9, #8]
	subs	w8, w8, w9
	cset	w8, ge
	tbnz	w8, #0, LBB3_3
	b	LBB3_2
LBB3_2:                                 ;   in Loop: Header=BB3_1 Depth=1
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
	b	LBB3_1
LBB3_3:
	mov	w0, #0                          ; =0x0
	ldp	x29, x30, [sp, #32]             ; 16-byte Folded Reload
	add	sp, sp, #48
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_BBS_Init                       ; -- Begin function BBS_Init
	.p2align	2
_BBS_Init:                              ; @BBS_Init
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #32
	stp	x29, x30, [sp, #16]             ; 16-byte Folded Spill
	add	x29, sp, #16
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	str	x0, [sp, #8]
	str	w1, [sp, #4]
	ldr	w8, [sp, #4]
	ldr	x9, [sp, #8]
	str	w8, [x9, #8]
	ldr	w0, [sp, #4]
	bl	_create_array
	ldr	x8, [sp, #8]
	str	x0, [x8]
	ldr	x8, [sp, #8]
	ldr	x8, [x8]
	ldr	x9, [x8]
	mov	w8, #20                         ; =0x14
	str	w8, [x9]
	ldr	x8, [sp, #8]
	ldr	x8, [x8]
	ldr	x9, [x8]
	mov	w8, #7                          ; =0x7
	str	w8, [x9, #4]
	ldr	x8, [sp, #8]
	ldr	x8, [x8]
	ldr	x9, [x8]
	mov	w8, #12                         ; =0xc
	str	w8, [x9, #8]
	ldr	x8, [sp, #8]
	ldr	x8, [x8]
	ldr	x9, [x8]
	mov	w8, #18                         ; =0x12
	str	w8, [x9, #12]
	ldr	x8, [sp, #8]
	ldr	x8, [x8]
	ldr	x9, [x8]
	mov	w8, #2                          ; =0x2
	str	w8, [x9, #16]
	ldr	x8, [sp, #8]
	ldr	x8, [x8]
	ldr	x9, [x8]
	mov	w8, #11                         ; =0xb
	str	w8, [x9, #20]
	ldr	x8, [sp, #8]
	ldr	x8, [x8]
	ldr	x9, [x8]
	mov	w8, #6                          ; =0x6
	str	w8, [x9, #24]
	ldr	x8, [sp, #8]
	ldr	x8, [x8]
	ldr	x9, [x8]
	mov	w8, #9                          ; =0x9
	str	w8, [x9, #28]
	ldr	x8, [sp, #8]
	ldr	x8, [x8]
	ldr	x9, [x8]
	mov	w8, #19                         ; =0x13
	str	w8, [x9, #32]
	ldr	x8, [sp, #8]
	ldr	x8, [x8]
	ldr	x9, [x8]
	mov	w8, #5                          ; =0x5
	str	w8, [x9, #36]
	mov	w0, #0                          ; =0x0
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
	tbnz	w8, #0, LBB5_2
	b	LBB5_1
LBB5_1:
	adrp	x0, l_.str.1@PAGE
	add	x0, x0, l_.str.1@PAGEOFF
	bl	_printf
	mov	w0, #1                          ; =0x1
	bl	_exit
LBB5_2:
	ldur	w8, [x29, #-12]
	subs	w8, w8, #0
	cset	w8, lt
	tbnz	w8, #0, LBB5_4
	b	LBB5_3
LBB5_3:
	ldur	w8, [x29, #-12]
	ldur	x9, [x29, #-8]
	ldr	w9, [x9, #8]
	subs	w8, w8, w9
	cset	w8, lt
	tbnz	w8, #0, LBB5_5
	b	LBB5_4
LBB5_4:
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
LBB5_5:
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
	tbnz	w8, #0, LBB6_2
	b	LBB6_1
LBB6_1:
	adrp	x0, l_.str.3@PAGE
	add	x0, x0, l_.str.3@PAGEOFF
	bl	_printf
	mov	w0, #1                          ; =0x1
	bl	_exit
LBB6_2:
	mov	x0, #16                         ; =0x10
	bl	_malloc
	str	x0, [sp, #16]
	ldr	x8, [sp, #16]
	subs	x8, x8, #0
	cset	w8, ne
	tbnz	w8, #0, LBB6_4
	b	LBB6_3
LBB6_3:
	adrp	x0, l_.str.4@PAGE
	add	x0, x0, l_.str.4@PAGEOFF
	bl	_printf
	mov	w0, #1                          ; =0x1
	bl	_exit
LBB6_4:
	ldursw	x8, [x29, #-4]
	lsl	x0, x8, #2
	bl	_malloc
	ldr	x8, [sp, #16]
	str	x0, [x8]
	ldr	x8, [sp, #16]
	ldr	x8, [x8]
	subs	x8, x8, #0
	cset	w8, ne
	tbnz	w8, #0, LBB6_6
	b	LBB6_5
LBB6_5:
	ldr	x0, [sp, #16]
	bl	_free
	adrp	x0, l_.str.5@PAGE
	add	x0, x0, l_.str.5@PAGEOFF
	bl	_printf
	mov	w0, #1                          ; =0x1
	bl	_exit
LBB6_6:
	str	wzr, [sp, #12]
	b	LBB6_7
LBB6_7:                                 ; =>This Inner Loop Header: Depth=1
	ldr	w8, [sp, #12]
	ldur	w9, [x29, #-4]
	subs	w8, w8, w9
	cset	w8, ge
	tbnz	w8, #0, LBB6_10
	b	LBB6_8
LBB6_8:                                 ;   in Loop: Header=BB6_7 Depth=1
	ldr	x8, [sp, #16]
	ldr	x9, [x8]
	ldrsw	x10, [sp, #12]
	mov	w8, #0                          ; =0x0
	str	w8, [x9, x10, lsl #2]
	b	LBB6_9
LBB6_9:                                 ;   in Loop: Header=BB6_7 Depth=1
	ldr	w8, [sp, #12]
	add	w8, w8, #1
	str	w8, [sp, #12]
	b	LBB6_7
LBB6_10:
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
	bl	_BBS__decaf__init
	ldr	x8, [sp, #24]
	ldr	x8, [x8, #16]
	ldr	x8, [x8]
	ldr	x0, [sp, #24]
	mov	w1, #10                         ; =0xa
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
	.p2align	3, 0x0                          ; @BBS__decaf__init.vtable
_BBS__decaf__init.vtable:
	.quad	_BBS_Start
	.quad	_BBS_Sort
	.quad	_BBS_Print
	.quad	_BBS_Init

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
