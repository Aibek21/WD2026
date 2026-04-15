import {inject, Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs';
import {AuthToken, Product} from './models';

@Injectable({
  providedIn: 'root',
})
export class DemoService {

  client = inject(HttpClient)
  BASE_URL = 'http://localhost:8000/api'

  login(username: string, password: string): Observable<AuthToken> {
    return this.client.post<AuthToken>(`${this.BASE_URL}/login/`, {username, password})
  }


  get_products(): Observable<Product[]> {
    // let token = localStorage.getItem('access')
    // let headers = {}
    // if (token) {
    //   headers = new HttpHeaders({
    //     'Content-Type': 'application/json',
    //     'Authorization': `Bearer ${token}`
    //   })
    // }
    return this.client.get<Product[]>(`${this.BASE_URL}/products/`)
  }
}
