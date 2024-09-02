import flet as ft

class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.main()

    def main(self):
        
        def icon_container(icon: str):
            return ft.Container(
                padding = ft.padding.all(20),
                bgcolor = ft.colors.WHITE10,
                border_radius = ft.border_radius.all(10),
                alignment = ft.alignment.center,
                content = ft.Column(
                    controls = [
                        ft.Icon(name = icon, size = 50),
                        ft.Text(value = icon),
                    ],
                    alignment = ft.MainAxisAlignment.CENTER,
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                ),
            )
        
        def search(e):
            value = e.control.value.upper()
            icons_grid.controls.clear()
            for icon in dir(ft.icons):
                if value in icon:
                   icons_grid.controls.append(icon_container(icon = icon))
                if value == '':
                    icons_grid.controls.clear()
            icons_grid.update()

        searchbar = ft.TextField(
            value = '',
            prefix_icon = ft.icons.SEARCH,
            hint_text = 'Digite algo para buscar...',
            on_submit = search,
        )

        icons_grid = ft.GridView(
            expand = True,
            max_extent = 200,
            controls = [],
            child_aspect_ratio = 1.0,
        )

        layout = ft.Column(
            expand = True,
            controls = [
                searchbar,
                icons_grid,
            ],
        )

        self.page.add(layout)

if __name__ == '__main__':
    ft.app(target = App, assets_dir = 'assets')
