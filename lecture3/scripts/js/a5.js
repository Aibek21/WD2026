let student = {
    'id': '20BD123123',
    age: 20,
    full_name: 'Some name',
    showInfo: function () {
        console.log({'id': this.id, 'full_name': this.full_name});
    }
};

student.showInfo();

let student_str = JSON.stringify(student);
console.log(student_str);


let newStudent = JSON.parse(student_str);
console.log(typeof newStudent)
console.log(newStudent)



let user = {
    address: null
};


console.log(user?.address?.city)
