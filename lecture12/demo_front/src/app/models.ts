export interface AuthToken {
  access: string
  refresh: string

}

export interface Category {
  id: number;
  name: string;
}

export interface Product {

  id: number;
  name: string;
  price: number;
  description: string;
  category: Category;

}
