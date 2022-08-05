import { Component, OnInit } from '@angular/core';
import { HourService } from './hour.service';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css'],
})
export class TableComponent implements OnInit {
  constructor(private hourService: HourService) {}
  rows: string[] = [];
  parkingfull_description = "Pátio lotado"; 
  parkingfull_color = "#B22222"

  ngOnInit(): void {
    this.getData()
    //this.description_parking = "Pátio lotado"
  }

  addNewItem(): void {
    //POST PARA ADICIONAR NOVO ELEMENTO
    //this.itens.push({});
  }

  parkingFull(): void {
    if (this.parkingfull_description == "Pátio lotado") {
      this.parkingfull_description = "Pátio aberto";
      this.getImage();
      

      //this.parkingfull_color = "#7CFC00";
    } 
    else 
    {
      this.parkingfull_description = "Pátio lotado"
      this.getVideo();
      //this.parkingfull_color = "#B22222"
    }
  }

  itens: any = [];

  getData() {
    this.hourService.getData().subscribe((res) => {
      this.itens = res;
      console.log(res);
    });
  }

  getVideo() {
    this.hourService.getVideo().subscribe((res) => {
      this.itens = res;
      console.log(res);
    });
  }

  getImage() {
    this.hourService.getImage().subscribe((res) => {
      this.itens = res;
      console.log(res);
    });
  }
  
}
