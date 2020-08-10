import { Component, OnInit } from '@angular/core';
import { ForecastService } from '../forecast.service';
import { Producto } from '../producto';
import { Forecast } from '../forecast';
import { Router } from '@angular/router';
import { Ventas } from '../ventas';

@Component({
  selector: 'app-create-forecast',
  templateUrl: './create-forecast.component.html',
  styleUrls: ['./create-forecast.component.css']
})
export class CreateForecastComponent implements OnInit {

  producto: Producto = new Producto();
  forecast: Forecast = new Forecast();
  submitted = false;

  constructor(private forecastService: ForecastService, private router: Router) { }

  ngOnInit(): void {
    console.log(this.producto)
  }

  newProducto(): void{
    this.submitted = false;
    this.producto = new Producto();
  }

  save(){
    var a = this.producto.ventas;
    this.producto.ventas=this.createVentas(a.toString());
    console.log(this.producto.ventas);

    this.forecastService.createForecast(this.producto)
      .subscribe(data => console.log(data), error => console.log(error));
    this.producto = new Producto();
    this.gotoList();
  }

  onSubmit(){
    this.submitted = true;
    this.save();
  }

  gotoList(){
    this.router.navigate(['forecast']);
  }
  createVentas(ventas_planas: string): Ventas[]{
    var ar = ventas_planas.split(',');
    console.log('arreglo' + ar);
    var ventas = Array<Ventas>();
    for (let i in ar){
      var v:Ventas = new Ventas();
      v.ganancia = ar[i];
      ventas.push(v);
    }
    return ventas;
  }

}
