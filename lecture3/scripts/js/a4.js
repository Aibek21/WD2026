let arr = [2, 3, 4, 5, 10];
let newArr = [];
for (let i = 0; i < arr.length; i++) {
    newArr[i] = arr[i] * i;
}

console.log(newArr)


function calcValue(val, ind) { // named function
    return val * ind;
}

newArr = arr.map(function (val, ind) { // anonymous function
    return val * ind;
})

console.log(newArr);


newArr = arr.map((val, ind) => val * ind)

console.log(newArr);


console.log(arr.reduce((acc, val) => {
    return acc + val
}));

