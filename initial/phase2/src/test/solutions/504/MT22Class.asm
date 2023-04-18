	li $t0,2
	li $t1,9
	add $t0,$t0,$t1
	li $t1,1
	li $t2,3
	add $t1,$t1,$t2
	add $t0,$t0,$t1
	move $a0,$t0
	li $v0,1
	syscall
