p = c(0,1,2,3,4)
q = c(0.41,0.37,0.16,0.05,0.01)
sum(p*q)
weighted.mean(p,q)
c(p%*%q)

f = function(t){
	if(t>0){
		return(0.1*exp(-0.1*t))
		}else{
		return(0)
	}

fun = function(t){
	t*f(t)
	}

ans=integrate(fun,lower=0,upper=Inf)
print(ans$value)