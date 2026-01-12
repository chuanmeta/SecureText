import { ChangeDetectorRef, Component, OnInit } from "@angular/core";
import { AppService } from "../../../services/app.service";
import { CommonModule } from "@angular/common";

@Component({
    selector: 'post-component',
    templateUrl: './post.component.html',
    styleUrl: './post.component.css',
    imports: [CommonModule]
})
export class PostComponent implements OnInit{
    appData: any = null;
  loading: boolean = false;

  constructor(private appService: AppService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.loadAppData();
  }

  loadAppData(): void {
    this.loading = true;

    this.appService.app().subscribe({
      next: (res) => {
        this.appData = { ...this.appData, data: res };
        this.loading = false;
        console.log(this.appData);
      },
      complete: () => {
        console.log("completed");
        this.loading = false;
        this.cdr.detectChanges();
      },
      error: (err) => {
        console.error(err);
        this.loading = false;
      }
    })
  }
}