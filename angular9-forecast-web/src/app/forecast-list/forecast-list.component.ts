import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { ForecastService } from '../forecast.service';
import { Forecast } from '../forecast';

@Component({
  selector: 'app-forecast-list',
  templateUrl: './forecast-list.component.html',
  styleUrls: ['./forecast-list.component.css']
})
export class ForecastListComponent implements OnInit {
  forecast: Observable<Forecast[]>;

  constructor(private forecastService: ForecastService) { }

  ngOnInit(): void {
    this.reloadData();
  }
  reloadData(){
    console.log("antes de ir a djongo");
    
    this.forecast = this.forecastService.getForecastList();
    console.log(this.forecast);
  }
}
