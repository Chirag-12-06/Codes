//DEFINATION

// const A=[2,3,4,5]
// console.log(A);

const B=new Array(9,7,6,3,5,2,1)
// console.log(B);


//METHODS
//ADD OR REMOVE FROM END
// B.pop()
// B.push(4)
// console.log(B);

//ADD OR REMOVE FROM START
// B.shift()
// B.unshift(0)
// console.log(B);

//ELEMENT EXISTS OR NOT
// console.log(B.includes(12));
// console.log(B.indexOf(12));


//JOIN
// const C=B.join()
// console.log(C);
// console.log(typeof(C));

//SLICE AND SPLICE
// const n1=B.slice(2,6)
// console.log("B ",B);
// console.log(n1);

// const n2=B.splice(2,6)
// console.log("B ", B);
// console.log(n2);

//JOINING 2 ARRAYS
const M=["one", "qwerty","op"]
const N=["it"," fifty","piece"]

// M.push(N)       
// console.log(M);             //PUSHES THE ARRAY N ASAN ELEMENT

// P=M.concat(N)
// console.log(P);

// const all=[...M,...N,...B]
// console.log(all);


//TO DEAL WITH ARRAY WITHIN ARRAY WITHIN ARRAY
// const old=[4,3,2,[6,5],1,[0,9,8,[1,7]]]
// console.log(old);
// const after=old.flat(1)
// const after1=old.flat(2)
// const after2=old.flat(Infinity)
// console.log(after);
// console.log(after1);
// console.log(after2);


// console.log(Array.isArray("were","to"));
// console.log(Array.from("were"));
// console.log(Array.from({name: "anything"}));        //NOTE!!!

const s1=234
const s2=2434
const s3=235
console.log(Array.of(s1,s2,s3));
