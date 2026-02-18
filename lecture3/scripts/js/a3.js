class Shape {

}


class Rectangle extends Shape {
    constructor(width, height) {
        super();
        this.width = width;
        this.height = height;
    }

    area() {
        return this.width * this.height;
    }
}


let rec = new Rectangle(10, 5);
console.log(rec.area());