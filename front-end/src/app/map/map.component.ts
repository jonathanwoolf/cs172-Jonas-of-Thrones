import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {
  title: string = 'My Map';
  lat: number = 33.9746831;
  lng: number = -117.324226

  constructor() { }

  ngOnInit() {
  }
}
