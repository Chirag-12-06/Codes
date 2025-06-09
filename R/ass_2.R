mode=function(x){
	uniq_val=unique(x)
	freq=tabulate(match(x,uniq_val))
	M=uniq_val[freq==max(freq)]
	return(M)
	}

p= c(1,2,3,3,2,5,4,7,8,3,2)
mod=mode(p)
print(mod)

coins=c(rep("G",20),rep("S",30),rep("B",50))
print(coins)
b=sample(coins,10,TRUE)
b

ch = c("Success","Failure")
prob = c(0.90,0.10)
f = sample(ch,10,replace=TRUE,prob)
f

t = sample(1:365,1000,TRUE)
t


con = function(P_a,P_b,P_a_by_B){
	x=P_a_by_B*P_b
	return(x/P_a)
	}
P_c = 0.4
P_r = 0.2
P_c_by_r = 0.85

P_r_by_c = con(P_c,P_r,P_c_by_r)
print(P_r_by_c)

data(iris)
head(iris)
tail(iris)
names(iris)
print(iris$Sepal.Length)
str(iris)
range(iris$Sepal.Length)
mean(iris$Sepal.Length)
median(iris$Sepal.Length)
quantile(iris$Sepal.Length)
IQR(iris$Sepal.Length)
sd(iris$Sepal.Length)
var(iris$Sepal.Length)
summary(iris)
