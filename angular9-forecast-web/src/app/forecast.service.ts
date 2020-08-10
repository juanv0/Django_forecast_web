import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Producto } from './producto';

@Injectable({
  providedIn: 'root'
})
export class ForecastService {


  private baseUrl = 'http://127.0.0.1:8000/forecast/'
  constructor(private http: HttpClient) { }

  getForecastList(): Observable<any>{
    return this.http.get(`${this.baseUrl}`);
  }

  createForecast(producto: Producto): Observable<Object>{
    return this.http.post(`${this.baseUrl}`, producto);
  }
}
