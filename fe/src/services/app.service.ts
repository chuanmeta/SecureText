import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";

@Injectable({providedIn: 'root'})
export class AppService {

    constructor(private http: HttpClient){}

    public app():Observable<any>{
        return this.http.get<any>(`/api/mkdir`)
    }

    public getText(req: any): Observable<any>{
        return this.http.post<any>(`/api/get-text`, req)
    }

    public genFont(fontGen: string): Observable<any>{
        return this.http.post<any>(`/api/gen-font?fontName=${fontGen}`, {})
    }
}