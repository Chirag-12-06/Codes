//OBJECT LITERALLS
// const user={
//     name:"db",
//     age:78
// }


// //PRINTING METHODS
// console.log(user.age);
// console.log(typeof user.age);
// console.log(user["age"]);


//FOR DEFINING SYMBOLS
const sym=Symbol("k")

const user={
    name:"db",
    age:78,
    [sym]:"k1"
}

// console.log(typeof user[sym]);
// console.log(user[sym]);


//MODIFY AND FREEZE
// user.age=98
// user["age"]=90
// console.log(user.age);
// Object.freeze(user)
// user.age=7
// console.log(user);


//FUNCTIONS IN OBJECTS
// user.greeting=function(){
//     console.log("Hello");
// }
// user.greetingto=function(){
//     console.log(`Hello ${this.name}`);
// }
// console.log(user.greeting);
// console.log(user.greeting());
// console.log(user.greetingto());

//COMBINING OBJECTS
// const ob1={
//     1: "u",
//     2: "o"
// }
// const ob2={
//     3: "u",
//     4: "o"
// }
// const ob3={
//     5: "u",
//     6: "o"
// }
// const ob4={ob1,ob2,ob3}
// console.log(ob4);
// const ob5=Object.assign(ob1,ob2,ob3)        //{target,source.....}
// console.log(ob5);
// console.log(ob1);

// const ob6=Object.assign({},ob2,ob3)
// console.log(ob6);

// const ob7={...ob1,...ob2,...ob3}
// console.log(ob7);

//KEYS,VALUES,ENTRIES,HAS PROPERTY
console.log(Object.keys(user));
console.log(Object.values(user));
console.log(Object.entries(user));
console.log(user.hasOwnProperty('name'));
console.log(Object.hasOwnProperty('nae'));

