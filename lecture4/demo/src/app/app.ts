import {Component, inject, signal} from '@angular/core';
import {FormsModule} from '@angular/forms';
import {TaskList} from './task-list/task-list';
import {PostList} from './post-list/post-list';
import {RouterModule, RouterOutlet} from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, RouterModule, FormsModule, TaskList, PostList],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  title = signal('demo');

  toggleText() {
    this.title.update(val => val + '1');
  }

}

