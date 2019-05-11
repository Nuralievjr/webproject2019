import { Component, OnInit } from '@angular/core';
import { ProviderService } from 'src/app/shared/serivces/provider.service';

@Component({
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css']
})
export class SigninComponent implements OnInit {

  
  public username;
  public password;
  constructor(private provider: ProviderService) { }

  ngOnInit() {

    /*if (this.logged) {
      this.provider.getTaskLists().then(res => {this.t_ls = res;});
      }*/
  }

  /*auth() {
    if(this.username!=='' && this.password!==''){
      this.provider.auth(this.username,this.password).then(r => {
        localStorage.setItem('token', r.token);
    });
    this.logged=true;
      }
}


  logout() {
  this.provider.logout().then(res => { localStorage.clear();this.logged = false;});
  }
  */

}
