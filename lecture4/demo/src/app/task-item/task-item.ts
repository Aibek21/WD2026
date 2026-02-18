import {Component, input, output} from '@angular/core';
import {Task} from '../../models';
import {FormsModule} from '@angular/forms';

@Component({
  selector: 'app-task-item',
  imports: [FormsModule],
  templateUrl: './task-item.html',
  styleUrl: './task-item.css',
})
export class TaskItem {
  task = input.required<Task>();
  remove = output<number>();

  removeTask(){
    this.remove.emit(this.task().id);
  }

}
