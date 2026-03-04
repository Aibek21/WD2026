// interface ITask {
//
// }

export class Task {
  static autoInc: number = 1;

  constructor(public id: number, public title: string, public isDone: boolean) {
  }
}


export class Post {

  constructor(public userId: number, public id: number, public title: string, public body: string) {
  }
}
