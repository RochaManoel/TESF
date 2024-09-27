import flet as ft

def main(page: ft.Page):

    page.title = "Energia Solar"
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_EVENLY
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def pick_files_result(event: ft.FilePickerResultEvent):
        filePath.value = (
            ', '.join(map(lambda f: f.path, event.files)) if event.files else page.open(dlg)
        )
        filePath.update()
    
    pick_files_dialog = ft.FilePicker(
        on_result=pick_files_result,
    )

    # Botão de Carregamento do arquivo
    buttonFile = ft.ElevatedButton(
        'Adicionar Planilha',
        icon=ft.icons.UPLOAD_FILE,
        on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=True),
        width = 300,
        style = ft.ButtonStyle(padding = 20)
    )

    # Alerta da mensagem de caminho vazio
    dlg = ft.AlertDialog(
        title=ft.Text("Erro ao Carregar arquivo, tente novamente!"),
    )

    # Caminho do arquivo a ser analisado
    filePath = ft.Text(
        width = 0,
        text_align= ft.TextAlign.CENTER,
        overflow = ft.TextOverflow.ELLIPSIS,
        bgcolor=ft.colors.RED,
    )

    # Botão de Ação do arquivo
    buttonActionFile = ft.ElevatedButton(
        'Criar Design',
        icon=ft.icons.UPLOAD_FILE,
        # on_click=,
        width = 300,
        style = ft.ButtonStyle(padding = 20)
    )

    page.overlay.extend([pick_files_dialog])

    page.add(
        ft.Column(
            [
                ft.Row(
                    [buttonFile, filePath, buttonActionFile],
                    alignment = ft.MainAxisAlignment.SPACE_EVENLY,
                    width = 750,
                ),
            ]
        ),
    )

ft.app(target=main)