import {EventEmitter, Injectable} from '@angular/core';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
import {IToken, ICategory, IProduct, IContact} from '../models/model';
import { Message } from '@angular/compiler/src/i18n/i18n_ast';

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
  getProductDetail(id:any): Promise<IProduct> {
    return this.get(`http://localhost:8000/products/${id}`, {});
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


  sendContact(name:any,email:any,phone:any,message:any): Promise<IContact>
  {
    return this.post('http://localhost:8000/contact/us',{
      name: name,
      email: email,
      phone: phone,
      message: message
    });
  }

  incVisit(id): Promise<IProduct>
{
  return this.put(`http://localhost:8000/products/${id}/ivisit`,{});
}

SearchByСharacter(character:any): Promise<any>{
  return this.get(`http://localhost:8000/products/?name=${character}`,{});
}

CreateUser(username:any,password:any,email:any){
  return this.post(`http://localhost:8000/registration`, {
    username: username,
    password: password,
    email: email
  });
}


}