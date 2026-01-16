import { ChangeDetectorRef, Component, OnInit, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { AppService } from '../services/app.service';
import { FormsModule, NgForm } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  imports: [CommonModule, FormsModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('fe');
  logs: string[] = []
  font: string = "";
  text: string = "";
  decode: string = "";

  constructor(private appService: AppService){}
  
  generateFont(): void {
    this.appService.genFont().subscribe({
      next: (res) =>{
        this.logs.push(res)
      },
      error: (err) => this.logs.push(err)
    });
  }

  encrypt(): void {

    let form = new FormData();
    form.append("font", this.font);
    form.append("text", this.text)

    this.appService.getText(form).subscribe({
      next: (res) =>{
        this.decode = res;
      },
      error: (err) => this.logs.push(err)
    });
  }
}
