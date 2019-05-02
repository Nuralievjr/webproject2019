import { Component, OnInit } from '@angular/core';

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
  public constructor() { }

  ngOnInit() {
  }

  pro(){
    console.log(this.message);
  }
    
  

}
