import {Routes} from '@angular/router';
import {PostList} from './post-list/post-list';
import {PostDetail} from './post-detail/post-detail';
import {Home} from './home/home';
import {About} from './about/about';

export const routes: Routes = [
  {path: 'home', component: Home, title: 'Home page'},
  {path: 'about', component: About, title: 'About page'},
  {path: 'posts', component: PostList, title: 'Post list'},
  {path: 'posts/:id', component: PostDetail, title: 'Post detail'}
];
