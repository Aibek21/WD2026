import {Component, inject, signal} from '@angular/core';
import {Post} from '../../models';
import {PostsService} from '../posts-service';
import {ActivatedRoute, RouterModule} from '@angular/router';

@Component({
  selector: 'app-post-detail',
  imports: [RouterModule],
  templateUrl: './post-detail.html',
  styleUrl: './post-detail.css',
})
export class PostDetail {
  post = signal<Post>(new Post(1, 1, '', ''));

  postsService = inject(PostsService);
  route = inject(ActivatedRoute);

  ngOnInit() {
    this.route.paramMap.subscribe((params) => {
      const postId = Number(params.get('id'));
      this.postsService.getPost(postId).subscribe((post) => {
        this.post.set(post);
        console.log(post);
      })
    })
  }
}
