import {Component, inject, signal} from '@angular/core';
import {PostsService} from '../posts-service';
import {Post} from '../../models';
import {RouterModule} from '@angular/router';
import {FormsModule} from '@angular/forms';

@Component({
  selector: 'app-post-list',
  imports: [RouterModule, FormsModule],
  templateUrl: './post-list.html',
  styleUrl: './post-list.css',
})
export class PostList {

  postsService = inject(PostsService);
  postList = signal<Post[]>([]);

  newPost = signal<Post>(new Post(1, 101, '', ''));
  isLoaded = signal<boolean>(false);

  ngOnInit() {
    this.postsService.getPosts().subscribe((posts: Post[]) => {
      this.postList.set(posts);
      this.isLoaded.set(true);
    });
  }


  addPost() {
    this.postsService.addPost(this.newPost()).subscribe((post) => {
      this.postList.update((posts) => [...posts, post]);
    })
  }

}
