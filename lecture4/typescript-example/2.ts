let num: number = 1;
// num = 'hello';
console.log(num);
console.log(typeof num);


function sum(a: number, b: number): number {
    return a + b;
}

console.log(sum(10, 5));

// console.log(sum('h', 5));


class Person {
    constructor(protected name, protected age) {
    }
}


class Student extends Person {

    constructor(name, age, public gpa) {
        super(name, age);
    }

    getGPA() {
        return this.gpa;
    }
}


let student = new Student('Bob', 20, 3.5);
console.log(student.getGPA())


function display<T>(msg: T){
    console.log(msg)
}

display<string>('hello');

let arr: Array<number> = [1, 2, 3]