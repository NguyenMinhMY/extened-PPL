	li $t0,1
	li $t1,2
	add $t0,$t0,$t1
	li $t1,2
	li $t2,4
	add $t1,$t1,$t2
	add $t0,$t0,$t1
	li $t1,5
	li $t2,6
	add $t1,$t1,$t2
	add $t0,$t0,$t1
	move $a0,$t0
	li $v0,1
	syscall
