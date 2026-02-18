import {Component, signal} from '@angular/core';
import {RouterOutlet} from '@angular/router';
import {FormsModule} from '@angular/forms';
import {TaskList} from './task-list/task-list';

@Component({
  selector: 'app-root',
  imports: [FormsModule, TaskList],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  title = signal('demo');

  toggleText() {
    this.title.update(val => val + '1');
  }

}
