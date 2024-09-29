import flet as ft

def main(page: ft.Page):
    page.window_maximized = True
    page.title = "Software - Célula Fotovoltáica"
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_EVENLY
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_resizable = False

    # Container Principal - Row Header - Container 02 - buttonSpaceRecord02
    buttonSpaceRecord02 = ft.ElevatedButton(
        'Ação 02',
        icon=ft.icons.ADD,
        # on_click= ,
        width = 300,
        style = ft.ButtonStyle(padding = 20)
    )

    # Container Principal - Row Header - Container 02 - buttonSpaceRecord01
    buttonSpaceRecord01 = ft.ElevatedButton(
        'Ação 01',
        icon=ft.icons.ADD,
        # on_click= ,
        width = 300,
        style = ft.ButtonStyle(padding = 20)
    )

    # Container Principal - Row Header - Container 02 - titleSpaceRecord
    titleSpaceRecord = ft.Container(
        content = ft.Text(
            "Gerenciamento de Gravação", 
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
        # on_click=,
        width = 300,
        style = ft.ButtonStyle(padding = 20)
    )

    # Container Principal - Row Header - Container 01 - textPathSpacefile
    textPathSpacefile = ft.Text(
        width = 0,
        text_align= ft.TextAlign.CENTER,
        overflow = ft.TextOverflow.ELLIPSIS,
    )

    # Container Principal - Row Header - Container 01 - buttonSpaceFile - def filesResult
    def filesResult(event: ft.FilePickerResultEvent):
        textPathSpacefile.value = (
            ', '.join(map(lambda f: f.path, event.files)) if event.files else page.open(ft.AlertDialog(title=ft.Text("Erro ao Carregar arquivo, tente novamente!")))
        )
        textPathSpacefile.update()

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
        width = page.width*0.595,
        height = page.height*0.055,
    )

    # Container Principal - Row Header
    headerSpace =  ft.Row(
            controls = [
                ft.Container(
                    content = ft.Row(
                        controls = [titleSpaceFile, buttonSpaceFile, textPathSpacefile, buttonActionSpaceFile],
                        alignment = ft.MainAxisAlignment.SPACE_EVENLY,
                        vertical_alignment = ft.CrossAxisAlignment.CENTER,
                        width = page.width*0.595,
                        height = page.height*0.165,
                        wrap = True,
                    ),
                    # bgcolor = ft.colors.BLUE_GREY_800,
                ),
                ft.Container(
                    content = ft.Row(
                        controls=[titleSpaceRecord, buttonSpaceRecord01, buttonSpaceRecord02],
                        alignment = ft.MainAxisAlignment.SPACE_EVENLY,
                        vertical_alignment = ft.CrossAxisAlignment.CENTER,
                        width = page.width*0.595,
                        height = page.height*0.165,
                        wrap = True,
                    ),
                    # bgcolor = ft.colors.GREEN_800,
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
                ft.Container(
                    content=ft.Text("olá mundo"),
                    width=page.width*1.2,
                    height = page.height*0.935,
                    bgcolor=ft.colors.BLACK54,
                )
            ],
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            width = page.width*1.2,
            height = page.height*1.1, 
        ),
        # bgcolor = ft.colors.RED_700,
    )

    page.overlay.extend([filesDialog])
    page.add(viewControl)

ft.app(target=main)