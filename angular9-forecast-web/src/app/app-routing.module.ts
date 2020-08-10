import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ForecastListComponent } from './forecast-list/forecast-list.component';
import { CreateForecastComponent }from './create-forecast/create-forecast.component';


const routes: Routes = [
  {path: 'forecast', component: ForecastListComponent},
  {path: 'add-forecast', component: CreateForecastComponent},
  {path: '**', redirectTo: 'forecasting'},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
