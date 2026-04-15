import {Component, inject, OnInit, signal} from '@angular/core';
import {DemoService} from '../demo-service';
import {Product} from '../models';

@Component({
  selector: 'app-product-list',
  imports: [],
  templateUrl: './product-list.html',
  styleUrl: './product-list.css',
})
export class ProductList implements OnInit {
  demoService = inject(DemoService)
  products = signal<Product[]>([])

  ngOnInit() {
    this.demoService.get_products().subscribe({
      next: (products) => {
        this.products.set(products)
      },
      error: (err) => {
        console.log(err);
      }
    })
  }

}
