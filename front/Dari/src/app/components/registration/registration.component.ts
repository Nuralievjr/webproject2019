import { Component, OnInit } from '@angular/core';
import { ProviderService } from 'src/app/shared/serivces/provider.service';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {

  public username;
  public password;
  public email;
 

  constructor(private provider: ProviderService) { }

  ngOnInit() {
  }

  CreateUser(){
    this.provider.CreateUser(this.username,this.password,this.email).then(res => {
      this.username = '';
      this.password = '';
      this.email = '';
  
    });
  }

}
