import {Component, inject, signal} from '@angular/core';
import {RouterOutlet} from '@angular/router';
import {DemoService} from './demo-service';
import {FormsModule} from '@angular/forms';

@Component({
  selector: 'app-root',
  imports: [FormsModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {

  demoService = inject(DemoService)
  username = ''
  password = ''

  login() {
    this.demoService.login(this.username, this.password).subscribe({
      next: (authToken) => {
        localStorage.setItem('access', authToken.access)
        localStorage.setItem('refresh', authToken.refresh)
      },
      error: (err) => {
        console.log(err)
      }
    })
  }
}
