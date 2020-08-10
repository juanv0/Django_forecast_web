import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { CreateForecastComponent } from './create-forecast/create-forecast.component';
import { ForecastListComponent } from './forecast-list/forecast-list.component';

@NgModule({
  declarations: [
    AppComponent,
    CreateForecastComponent,
    ForecastListComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
