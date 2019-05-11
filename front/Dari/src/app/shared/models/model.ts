export interface ICategory{
    id:number;
    name: string;
  }
  
  export interface IProduct {
    name:String;
    price:Number;
    count:Number;
    image:String;
    visit:number;
    description:string;
  }
  export interface IToken{
    token:string; 
  }
  

  export interface IContact{
    name: string;
    email:string;
    phone:string;
    message:string;
  }