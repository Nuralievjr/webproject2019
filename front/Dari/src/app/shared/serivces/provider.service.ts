import {EventEmitter, Injectable} from '@angular/core';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
import {IToken, ICategory, IProduct} from '../models/model';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {


  constructor(http: HttpClient) {
    super(http);
  }

  getCategories(): Promise<ICategory[]> {
    return this.get('http://localhost:8000/category/', {});
  }
  getProducts(): Promise<IProduct[]> {
    return this.get('http://localhost:8000/products/', {});
  }


  getProductsPopular(): Promise<IProduct[]> {
    return this.get('http://localhost:8000/products/popular', {});
  }

  getCategoryProducts(categories: ICategory): Promise<IProduct[]> {
    return this.get(`http://localhost:8000/category/${categories.id}/products`, {});
  }

  createCategory(name: any): Promise<ICategory> {
    return this.post('http://localhost:8000/api/categories/', {
      name: name
    });
  }

  updateCategory(category: ICategory): Promise<ICategory> {
    return this.put(`http://localhost:8000/api/categories/${category.id}/`, {
      name: category.name
    });
  }

  deleteCategory(id: number): Promise<any> {
    return this.delet(`http://localhost:8000/api/categories/${id}/`, {});
  }

  auth(login: string, password: string): Promise<IToken> {
    return this.post('http://localhost:8000/api/login/', {
      username: login,
      password: password
    });
  }

  logout(): Promise<any> {
    return this.post('http://localhost:8000/api/logout/', {});
  }

}