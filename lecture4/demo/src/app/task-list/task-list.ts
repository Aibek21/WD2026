import {Component, inject, signal} from '@angular/core';
import {Task} from '../../models';
import {FormsModule} from '@angular/forms';
import {TaskItem} from '../task-item/task-item';
import {CommonModule} from '@angular/common';
import {PostsService} from '../posts-service';

@Component({
  selector: 'app-task-list',
  imports: [FormsModule, CommonModule, TaskItem],
  templateUrl: './task-list.html',
  styleUrl: './task-list.css',
  // template: '<p>Task list</p>'
})
export class TaskList {
  taskList = signal<Task[]>([])
  currentTask = signal<Task>(new Task(1, '', false))

  addTask() {
    if (this.currentTask().title) {
      let task = this.currentTask();
      task.id = Task.autoInc++;
      this.taskList.update(tasks => [...tasks, task]);
      this.currentTask.set(new Task(1, '', false));
    }
  }


  onTaskRemove(id: number) {
    this.taskList.update(tasks => tasks.filter(val => val.id != id));
  }

}

