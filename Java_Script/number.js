// const num=new  Number(345)
// console.log(num);

// //TO USE PROPERTIES OF STRING
// console.log(num.toString().length);

// //FOR ADDING DECIMAL TO A SIMPLE NOS
// console.log(num.toFixed(2));

// //ROUNDING OFF
// const other=435.556
// console.log(other.toPrecision(1));

// //PUTTING COMMAS
// const hund=100000000;
// console.log(hund.toLocaleString());
// console.log(hund.toLocaleString('en-US'));

// //MATHS
// console.log(Math.PI);
// console.log(Math.abs(-23));
// console.log(Math.round(4.5));
// console.log(Math.round(4.4));
// console.log(Math.floor(4.9));
// console.log(Math.ceil(4.1));


// //FIND MIN MAX IN A RANGE
// console.log(Math.min(3,4,8,9,2));
// console.log(Math.max(3,4,8,9,2));

//RANDOM (GIVES VALUES BETWEEN 0 AND 1 INCLUDING 0 EXCLUDING 1)
console.log(Math.random());

//TO HAVE RANGE 0 AND 10
console.log(Math.random()*10);

//TO HAVE RANGE 1 AND 10
console.log((Math.random()*10)+1);
console.log(Math.floor(Math.random()*10)+1);

//TO HAVE RANGE WITH A MIN AND MAX
min=4
max=15
console.log(Math.floor(Math.random()*(max-min+1)+min));
