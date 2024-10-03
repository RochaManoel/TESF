import flet as ft
import numpy as np
import pandas as pd

class Graphic:
    def __init__(self):
        self.path = "C:/Users/ManoelRocha/Documents/energiaSolar/TabelaTESF.xlsx"
        self.table = pd.read_excel(self.path)

    def setPath(self):
        # self.path = path
        if self.path != "":
            tabelaTESF = pd.read_excel(self.path)
            self.setTable(table=tabelaTESF)

    def setTable(self, table):
        self.table = table

    def generateDataSeriesRadiance(self):
        labels = []
        for i in range(0,len(self.table["Radiação"])):
            labels.append(
                ft.LineChartDataPoint(i, float(self.table["Radiação"][i]))
            )
        return labels
    
    def generateDataSeriesTemperature(self):
        labels = []
        for i in range(0,len(self.table["Temp_Cel"])):
            labels.append(
                ft.LineChartDataPoint(i, float(self.table["Temp_Cel"][i]))
            )
        return labels

    def getListHours(self):
        list = []
        for t in self.table["Data_Hora"]:
            list.append(ft.dropdown.Option(t.strftime("%H:%M")))
        return list

    def getMinYRadiance(self):
        return -1
    
    def getMaxYRadiance(self):
        r = max(self.table["Radiação"]) % 100
        if r > 0:
            return max(self.table["Radiação"]) + (100-r)
        return max(self.table["Radiação"])
        
    def getMinYTemperature(self):
        return min(self.table["Temp_Cel"])-10
    
    def getMaxYTemperature(self):
        return max(self.table["Temp_Cel"])+1
    
    def getMinX(self):
        return -1
    
    def getMaxX(self):
        return len(self.table["Data_Hora"])+1


g = Graphic()

def main(page: ft.Page):
    page.title = "Software - Célula Fotovoltáica"
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_EVENLY
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.resizable = False
    page.window.maximized = True

    titlePowerNetwork = ft.Text(
        
    )

    viewPowerNetwork = ft.LineChart(

    )

    titleNetwork = ft.Text(
        
    )

    viewNetwork = ft.LineChart(

    )

    titlePower = ft.Text(

    )

    viewPower = ft.LineChart(

    )

    inputHour = ft.Dropdown(
        bgcolor = ft.colors.TRANSPARENT,
        color = ft.colors.WHITE,
        value = "00:00",
        options = g.getListHours(),
    )

    viewRadiance = ft.LineChart(
        data_series = [
            ft.LineChartData(
                data_points = g.generateDataSeriesRadiance(),
                stroke_width=1,
                color=ft.colors.YELLOW_ACCENT,
                stroke_cap_round=True,
            ),
        ],
        min_y = g.getMinYRadiance(),
        min_x = g.getMinX(),
        max_y = g.getMaxYRadiance(),
        max_x = g.getMaxX(),
        tooltip_bgcolor = ft.colors.with_opacity(0.8, ft.colors.BLACK),
        expand = True,
    )

    titleRadiance = ft.Container(
        content = ft.Text(
            "Radiância ao longo do dia", 
            size = 20,
            text_align = ft.TextAlign.CENTER,
            weight = ft.FontWeight.BOLD,
        ),
        width = page.width*0.7,
        height = page.height*0.055,
    )

    viewTemperature = ft.LineChart(
        data_series = [
            ft.LineChartData(
                data_points = g.generateDataSeriesTemperature(),
                stroke_width=1,
                color=ft.colors.RED,
                stroke_cap_round=True,
            ),
        ],
        min_y = g.getMinYTemperature(),
        min_x = g.getMinX(),
        max_y = g.getMaxYTemperature(),
        max_x = g.getMaxX(),
        tooltip_bgcolor = ft.colors.with_opacity(0.8, ft.colors.BLACK),
        expand = True,
    )

    titleTemperature = ft.Container(
        content = ft.Text(
            "Temperatura ao longo do dia", 
            size = 20,
            text_align = ft.TextAlign.CENTER,
            weight = ft.FontWeight.BOLD,
        ),
        width = page.width*0.7,
        height = page.height*0.055,
    )

    GraphicSpace =  ft.Row(
            controls = [
                ft.Container(
                        content = ft.Row(
                            controls = [
                                ft.Container(
                                    content = ft.Column(
                                        controls = [
                                            titleRadiance,
                                            viewRadiance,
                                            titleTemperature,
                                            viewTemperature
                                        ],
                                    ),
                                    width = page.width*0.7,
                                    height = page.height*0.9,
                                ),
                                ft.Container(
                                    content = ft.Column(
                                        controls = [
                                            inputHour,
                                            titlePower,
                                            viewPower,
                                            titleNetwork,
                                            viewNetwork,
                                            titlePowerNetwork,
                                            viewPowerNetwork,
                                        ],
                                    ),
                                    width = page.width*0.24,
                                    height = page.height*0.9,
                                )
                            ]
                        ),
                        width = page.width*0.95,
                        height = page.height*0.9,
                ),
                ft.Container(
                    bgcolor=ft.colors.RED,
                    width = page.width*0.24,
                    height = page.height*0.9,
                )
            ],
            alignment= ft.MainAxisAlignment.CENTER,
            width = page.width*1.2,        
        )





    # Container Principal - Row Header - Container 02 - buttonSpaceRecord02
    buttonSpaceRecord02 = ft.ElevatedButton(
        'A',
        icon=ft.icons.ADD,
        # on_click= ,
        width = 100,
        style = ft.ButtonStyle(padding = 20)
    )

    # Container Principal - Row Header - Container 02 - titleSpaceRecord
    titleSpaceRecord = ft.Container(
        content = ft.Text(
            "Gerenciamento", 
            size = 20,
            text_align = ft.TextAlign.CENTER,
            weight = ft.FontWeight.BOLD,
        ),
        width = page.width*0.595,
        height = page.height*0.055,
    )

    # Container Principal - Row Header - Container 01 - buttonActionSpaceFile
    buttonActionSpaceFile = ft.ElevatedButton(
        'Gerar Dashboard',
        icon=ft.icons.DASHBOARD_CUSTOMIZE,
        # on_click = dashboard(),
        width = 300,
        style = ft.ButtonStyle(padding = 20)
    )

    # Container Principal - Row Header - Container 01 - buttonSpaceFile - def filesResult
    def filesResult(event: ft.FilePickerResultEvent):
        if event.files:
            path = ', '.join(f.path for f in event.files)
        else:
            page.open(ft.AlertDialog(title=ft.Text("Erro ao Carregar arquivo, tente novamente!")))
            path = ""
        g.setPath()

    # Container Principal - Row Header - Container 01 - buttonSpaceFile - filesDialog
    filesDialog = ft.FilePicker(on_result=filesResult)

    # Container Principal - Row Header - Container 01 - buttonSpaceFile
    buttonSpaceFile = ft.ElevatedButton(
        'Adicionar Planilha',
        icon=ft.icons.UPLOAD_FILE,
        on_click=lambda _: filesDialog.pick_files(allow_multiple=True),
        width = 300,
        style = ft.ButtonStyle(padding = 20)
    )

    # Container Principal - Row Header - Container 01 - titleSpaceFile
    titleSpaceFile = ft.Container(
        content = ft.Text(
            "Gerenciamento de Arquivos", 
            size = 20,
            text_align = ft.TextAlign.CENTER,
            weight = ft.FontWeight.BOLD,
        ),
        width = page.width*0.9,
        height = page.height*0.055,
    )

    # Container Principal - Row Header
    headerSpace =  ft.Row(
            controls = [
                ft.Container(
                    content = ft.Row(
                        controls = [titleSpaceFile, buttonSpaceFile, buttonActionSpaceFile],
                        alignment = ft.MainAxisAlignment.SPACE_EVENLY,
                        vertical_alignment = ft.CrossAxisAlignment.CENTER,
                        width = page.width*0.95,
                        height = page.height*0.165,
                        wrap = True,
                    ),
                    bgcolor=ft.colors.AMBER
                ),
                ft.Container(
                    content = ft.Row(
                        controls=[titleSpaceRecord, buttonSpaceRecord02],
                        alignment = ft.MainAxisAlignment.SPACE_EVENLY,
                        vertical_alignment = ft.CrossAxisAlignment.CENTER,
                        width = page.width*0.24,
                        height = page.height*0.165,
                        wrap = True,
                    ),
                    bgcolor=ft.colors.RED
                ),
            ],
            alignment= ft.MainAxisAlignment.CENTER,
            width = page.width*1.2,        
        )

    # Container Principal
    viewControl = ft.Container(
        content = ft.Column(
            controls = [
                headerSpace,
                GraphicSpace,
            ],
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            width = page.width*1.2,
            height = page.height*1.1, 
        ),
    )

    page.overlay.extend([filesDialog])
    page.add(viewControl)

ft.app(target=main)
