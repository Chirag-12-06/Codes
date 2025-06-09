const n="vg"
const m="vgt"
// console.log(n +"Fd" +m);

//INSTEAD
// console.log(`iniially ${n} then${m}`);      //LOOK FOR THE BLANK SPACES PRINTED AS IT IS

//ANOTHER WAY FOR DEFINING STRING
const any=new String("fvfijfbITUTg")

// console.log(any);
// console.log(any.length);
// console.log(any.toUpperCase());
// console.log(any.charAt(2));
// console.log(any.indexOf('f'));

const news=any.substring(-7,5)       //VALUE ENTERED AT LAST IS IGNORED
// console.log(news);

const revs=any.slice(-8,5)          //VALUE ENTERED AT LAST IS IGNORED, FOR (-) VALUE LAST IS IGNORED 
// console.log(revs);

const spaced=new String("   df egregf gre c      ")
// console.log(spaced);
// console.log(spaced.trim());         //REMOVES THE SPACES BEFORE AND AFTER MAIN STRING
// console.log(spaced.trimStart());
// console.log(spaced.trimEnd());

const url="ffkj_frgf2gamil.cokm"
// console.log(url.replace('_fr','po'));       //NO NEED TO USE " "
// console.log(url.includes("f"));             //NO NEED TO USE " " and INCLUDES USE TO FIND IN A STRING

const kode="c*j**wiv*vf*ei*g"
console.log(kode.split('*',5));                //DIVIDES THE STRING INTO MULTIPLE ON THE BASIS OF CHARACTER ENTERED, LIMIT IS MAXIMUM SPLITS SHOULD APPEAR IN OUTPUT, IF 2 OF SAME CHARACTERS ENTERED EMPTY STRING IS RETURNED


