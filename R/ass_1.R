d = c(5,10,15,20,25,30)
max(d)
min(d)

f = function(x){
	fac=1
	for(i in 1:x){
		fac=i*fac
	}
	return(fac)
}

n = as.numeric(readline("Enter a no: "))
if(n<0){
	print("ERROR")
	}else{
	print(f(n))
	}

fibo = function(o){
		if(o==0){
			return(0)
		}
		if(o==1){
			return(1)
		}
		a=0
		b=1
		c=0
		for(i in 2:o){
			c=a+b
			a=b
			b=c
		}
		return(c)
	}

u = as.numeric(readline("Enter a no: "))
for(i in 0:u){
	print(fibo(i))
	}

calc=function(){
p = as.numeric(readline("Enter the no1: "))
q = as.numeric(readline("Enter the no2: "))
}
calc()


m = c(1,2,3,4,5)
n = c(6,7,8,9,10)
plot(n,m,type="p",horiz=TRUE)
plot(m,n,type="l")
plot(n,m)

values <- c(10, 20, 100)
labels <- c("Apple", "Banana", "Cherry")
pie(values, labels, col=c("red", "yellow"), main="Fruit Distribution")


heights <- c(5, 7, 3, 8, 6)
names <- c("A", "B", "C", "D", "E")
barplot(names.arg=names,heights,horiz=TRUE,xlab="wew",ylab="cdw")


sample=rpois(30,40)
hist(sample)
