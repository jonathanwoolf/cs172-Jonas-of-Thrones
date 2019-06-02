import { Component, OnInit } from '@angular/core';

import { ArticleService } from './article.service';
import { Article } from './article';
import { Observable, Subject } from 'rxjs';
import { MarkerManager } from '@agm/core';
import { MouseEvent } from '@agm/core';
import { NgForOf } from '@angular/common';

@Component({
  selector: 'app-article',
  templateUrl: './article.component.html',
  styleUrls: ['./article.component.css']
})
export class ArticleComponent implements OnInit {
  articles: Article[];
  markers: marker[] = [];
  lastSearch: string;
  lat: number = 33.9746831;
  lng: number = -117.324226;


  constructor(private articleService: ArticleService) { }

  ngOnInit() {    
  }
  search(query: string) {
    this.lastSearch = query;

    this.articleService.getArticles(query)
        .subscribe(articles => this.articles = articles);    
    this.markers = [];
    console.log("Hello World");
    
    for(var i =0; i < this.articles.length; i++){
      this.markers.push({
        lat: this.articles[i].lon,
        lng: this.articles[i].lat,
      });
      
    }
  }
  /*
  mapClicked($event: MouseEvent) {
    this.markers.push({
      lat: $event.coords.lat,
      lng: $event.coords.lng,
    });
  }*/

  // markers: marker[] = [
	//   {
	// 	  lat: 34.061622,
	// 	  lng: -118.226382,
	// 	  label: 'A',
	// 	  draggable: true
	//   },
	//   {
	// 	  lat: 33.66558,
	// 	  lng: -117.810101,
	// 	  label: 'B',
	// 	  draggable: false
	//   },
	//   {
	// 	  lat: 34.01713,
	// 	  lng: -118.463708,
	// 	  label: 'C',
	// 	  draggable: true
	//   }
  // ]
}

interface marker {
	lat: number;
	lng: number;
	label?: string;
}