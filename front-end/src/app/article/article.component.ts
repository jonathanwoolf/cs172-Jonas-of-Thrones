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
  lat: number;//number = 33.9746831;
  lng: number; //number = -117.324226;
  markerlat: number = 0.0;
  markerlng: number = 0.0;

  rangeLimit: boolean = true;

  constructor(private articleService: ArticleService) { 
    if(navigator){
      navigator.geolocation.getCurrentPosition(pos => {
        this.lng = pos.coords.longitude;
        this.lat = pos.coords.latitude;
      })
    }
  } 

  clickedMarker(label: string, index: number){
    this.markerlat=this.markers[index].lat;
    this.markerlng=this.markers[index].lng;
  }

  ngOnInit() {    
  }

  switchRange(){
    this.rangeLimit = !this.rangeLimit;
    this.search(this.lastSearch);
  }

  search(query: string) {
    this.lastSearch = query;

    this.articleService.getArticles(query)
        .subscribe(articles => this.articles = articles);    
    this.markers = [];
    
    for(var i =0; i < this.articles.length; i++){
      if(this.rangeLimit) {
        if(this.distance(this.articles[i].lat,this.articles[i].lon) < 100){
        //if you have marker issues try switching these
          this.markers.push({
            lat: this.articles[i].lat,
            lng: this.articles[i].lon,
            label: this.articles[i].id.toString(),
          });
        }
      }
      else {
        this.markers.push({
          lat: this.articles[i].lat,
          lng: this.articles[i].lon,
          label: this.articles[i].id.toString(),
        });
      }
    }
  }
  
  degreesToRadians(degrees) {
    return degrees * Math.PI / 180;
  }

  distance(tweetLat: number, tweetLon: number){
      var earthRadiusMI = 3959;
      var latDist = this.degreesToRadians(tweetLat-this.lat);
      var lonDist = this.degreesToRadians(tweetLon-this.lng);

      var lat1 = this.degreesToRadians(this.lat);
      var lat2 = this.degreesToRadians(tweetLat);

      var a = Math.sin(latDist/2) * Math.sin(latDist/2) + 
              Math.sin(lonDist/2) * Math.sin(lonDist/2) * Math.cos(lat1)*Math.cos(lat2);
      var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 
      return earthRadiusMI * c;
  }
}

interface marker {
	lat: number;
	lng: number;
	label?: string;
}