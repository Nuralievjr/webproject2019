import { Component, OnInit } from '@angular/core';
import { ProviderService } from 'src/app/shared/serivces/provider.service';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent implements OnInit {

  public name;
  public email;
  public phone;
  public message;
  public constructor(private provider: ProviderService) { }

  ngOnInit() {

  }

  sendContact(){
    console.log(this.name,this.email,this.phone,this.message)
    return this.provider.sendContact(this.name,this.email,this.phone,this.message).then(res => {
      this.name = '';
      this.email= '';
      this.phone = '';
      this.message = '';
    })
  }

  
    
  

}
