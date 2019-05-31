import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { HttpModule } from '@angular/http';
import { HttpClientModule }    from '@angular/common/http';

import { ArticleService } from './article/article.service';


import { AppComponent } from './app.component';
import { ArticleComponent } from './article/article.component';
import { MapComponent } from './map/map.component'

import { AgmCoreModule } from '@agm/core';

@NgModule({
  declarations: [
    AppComponent,
    ArticleComponent,
    MapComponent
  ],
  imports: [
    BrowserModule,
    HttpModule,
    HttpClientModule,
    AgmCoreModule.forRoot({
      apiKey: 'AIzaSyDW6QAEg9BEQquxMDoYy_gAMGPNgtpddf0'
    })
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }