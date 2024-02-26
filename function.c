#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
// function prototype
//float speed( float distance, float time);
float speed( float distance, float time){
	float speedrate = distance / time;
	return speedrate;
}
main() {
	// function call
	printf("%.2f",speed(100, 5));
	
	return 0;
}
// function defination

