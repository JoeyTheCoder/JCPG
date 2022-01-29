import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GamecornerComponent } from './gamecorner.component';

describe('GamecornerComponent', () => {
  let component: GamecornerComponent;
  let fixture: ComponentFixture<GamecornerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GamecornerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GamecornerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
