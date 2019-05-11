import { Component, OnInit } from '@angular/core';
import { IProduct } from 'src/app/shared/models/model';
import { ProviderService } from 'src/app/shared/serivces/provider.service';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {


  public products: IProduct[] = []

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getProducts().then(res => {
      this.products = res;
    });

  }
  SearchByCharacter(letter:any){
    this.provider.SearchByСharacter(letter).then(res=> {
      this.products = res;
    });
  }

}
