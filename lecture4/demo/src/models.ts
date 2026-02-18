// interface ITask {
//
// }

export class Task {
  static autoInc: number = 1;

  constructor(public id: number, public title: string, public isDone: boolean) {
  }
}
