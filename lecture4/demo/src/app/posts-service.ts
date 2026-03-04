import {inject, Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {Post} from '../models';

@Injectable({
  providedIn: 'root',
})
export class PostsService {

  client = inject(HttpClient)

  getPosts(): Observable<Post[]> {
    return this.client.get<Post[]>('https://jsonplaceholder.typicode.com/posts');
  }

  getPost(id: number): Observable<Post> {
    return this.client.get<Post>(`https://jsonplaceholder.typicode.com/posts/${id}`)
  }

  addPost(post: Post): Observable<Post> {
    return this.client.post<Post>('https://jsonplaceholder.typicode.com/posts', post);
  }

  deletePost(id: number): Observable<Post> {
    return this.client.delete<Post>(`https://jsonplaceholder.typicode.com/posts/${id}`);
  }

  updatePost(id: number, post: Post): Observable<Post> {
    return this.client.put<Post>(`https://jsonplaceholder.typicode.com/posts/${id}`, post);
  }
}
