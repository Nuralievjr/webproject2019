import { Component, OnInit } from '@angular/core';
import { ProviderService } from 'src/app/shared/serivces/provider.service';
import { ICategory, IProduct } from 'src/app/shared/models/model';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.css']
})
export class CategoryComponent implements OnInit {

  public categories: ICategory[] = []
  public products: IProduct[] = []
  constructor(private provider: ProviderService) { }

  
  ngOnInit() {
    this.provider.getCategories().then(res => {
      this.categories = res;
    });
  
  }
  getCategoryProducts(categories: ICategory)
  {
    this.provider.getCategoryProducts(categories).then(res => {
      this.products=res;
    });
  }
  

}
