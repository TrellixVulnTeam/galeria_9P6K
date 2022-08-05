import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http' 
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HourService {

  constructor(private http: HttpClient) { }

  getData(): Observable<any> {
    return this.http.get<any>('http://127.0.0.1:5050/configuration')    
  }

  getVideo(): Observable<any> {
    return this.http.get<any>('http://127.0.0.1:5050/playvideo')    
  }
  
  getImage(): Observable<any> {
    return this.http.get<any>('http://127.0.0.1:5050/playimage')    
  }  

}
