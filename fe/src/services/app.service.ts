import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";

@Injectable({providedIn: 'root'})
export class AppService {
    constructor(private http: HttpClient){}

    public app():Observable<any>{
        return this.http.get<any>(`http://localhost:8080/wellcome`)
    }
}