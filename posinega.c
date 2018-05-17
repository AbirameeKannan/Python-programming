int main(void) {
	int a; 
	printf("enter the number");
	scanf("%d",&a);
    if(1<=a<=100000)
    {
    	printf("positive");
    }
    else if(a==0)
    {
    	printf("neither negative nor positive");
    }
    else{
    	printf("error");
    }
    
	return 0;
}
