import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateForecastComponent } from './create-forecast.component';

describe('CreateForecastComponent', () => {
  let component: CreateForecastComponent;
  let fixture: ComponentFixture<CreateForecastComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CreateForecastComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CreateForecastComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
