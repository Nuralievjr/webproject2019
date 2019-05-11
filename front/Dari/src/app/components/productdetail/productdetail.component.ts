import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ProviderService } from 'src/app/shared/serivces/provider.service';
import { ICategory } from 'src/app/shared/models/model';

@Component({
  selector: 'app-productdetail',
  templateUrl: './productdetail.component.html',
  styleUrls: ['./productdetail.component.css']
})
export class ProductdetailComponent implements OnInit {
  
  public product;
  public name ;
  public price ;
  public count;
  public image;
  public visit ;
  public description;

  public categories: ICategory[] = []

  value:any;
  constructor(private route: ActivatedRoute, private provider: ProviderService) { }

  ngOnInit() {
    scroll(300,0);
    this.route.params.subscribe(params => {
      this.value = params.id; // --> Name must match wanted parameter
    });
    this.provider.getProductDetail(this.value).then(res => {
      this.product = res;
      
      this.name = this.product.name;
      this.price = this.product.price;
      this.count = this.product.count;
      this.image= this.product.image;
      this.visit = this.product.visit;
      this.description = this.product.description
      this.provider.incVisit(this.product.id);
    });
    this.provider.getCategories().then(res => {
      this.categories = res;});
    

      


  }

  

}
