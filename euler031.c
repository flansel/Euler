#include <stdio.h>

int main(int argc, char* argv[]){
	int n;
	scanf("%d", &n);
	int a,b,c,d,e,f,o;
	int count = 0;
	for(a=0;a<=(n/200);a++){
		for(b=0;b<=(n-200*a)/100;b++){
			for(c=0;c<=(n-200*a-100*b)/50;c++){
				for(d=0;d<=(n-200*a-100*b-50*c)/20;d++){
					for(o=0;o<=(n-200*a-100*b-50*c)/10;o++){
						for(e=0;e<=(n-200*a-100*b-50*c-20*d-10*o)/5;e++){
							for(f=0;f<=(n-200*a-100*b-50*c-20*d-10*o-5*e)/2;f++){
								if(200*a+100*b+50*c+20*d+10*o+5*e+2*f <= n)
									count++;
							}
						}
					}
				}
			}
		}
	}	
	printf("%d", count);
}
