import { Component, OnInit } from '@angular/core';
import { CarouselModule } from 'ngx-bootstrap/carousel';
import {ProviderService} from '../../shared/serivces/provider.service';
import {ICategory, IProduct} from '../../shared/models/model';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css','bootstrap.css']
})
export class HomeComponent implements OnInit {


  public productspop: IProduct[] = [];

  public name: any = '';

  public isLogged = false;

  public login = '';
  public password = '';


  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getProductsPopular().then(res => {
      this.productspop = res;
    });


  }
  

    

}
