// This is a comment 

'hello' == 'hello'
// True

1 == 1 && 2 == 2
// True

1 == 2 && 2 == 2
// False

'1' == 1 // True
// Type Convert Into String To Integer By Default 
// If You Dont Need To Convert The Datatype then use ' === '
'1' === 1 // False - check datatype and value both

// Or Operator
1 == 1 || 1 == 2
// True

// Not Operator
!(1 == 1) // False
1 != 2 // True
!!(1 == 1) // True 

var x = 1;
var y = 2;

'2' == y && x === 1;
x >= 0 || y === '2';

var names; // undefine console.log(names)

var hot = false 
var temp = 100

if (temp > 80){
    hot = true
}
console.log(hot)
// inside console write - hot -> ture

//
if (temp < 80){
    hot = true
}
else if (temp == 100){
    console.log('Very Hot')
}

// -----------------------------------------
var chicken = 10
var cheese = 10

report = 'blank'

if (chicken >= 10 && cheese >= 10){
    report = 'Strong Demand'
}
else if (chicken === 0 && cheese === 0){
    report = 'Nothing Sold'
}
else{
    report = 'We Had Some Sales'
}
console.log(report)
// Strong Demand

// -----------------------------------------------

var x = 0
while (x < 5){
    console.log('X is Currently : ' + x);
    x += 1;
}
// 0,1,2,3,4

// ------------------------------------------------

var x = 0
while (x < 5){
    console.log('X is Currently : ' + x);
    x += 1;

    if (x == 3){
        break
    }
}
// 0,1,2,3

// -----------------------------------------------

var num = 1;
while (num < 11){
    if (num % 2 == 0){
        console.log(num)
    }
}
// even no print - 0,2,4,6,8,10

// ----------------------------------------------

// - Define For Loop -> for(var i; condition; increment/decrement )
for (var num = 0; num < 5; num++){
    console.log('Number Is : ' + num)
}
// 0,1,2,3,4

// ----------------------------------------------

var word = 'abcdefgh'

for(var i = 0; i < word.length; i++){
    console.log(word[i])
}

// --------------------------------------------

var word = 'abababab'

for(var i = 0; i < word.length; i = i + 2){
    console.log(word[i])
}
// a * 4

// -----------------------------------------------
