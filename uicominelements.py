from nicegui import ui
from nicegui.events import ValueChangeEventArguments

def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')

ui.button('Boton', on_click=lambda: ui.notify('Click'))
with ui.row():
    ui.checkbox('terminos', on_change=show)
    ui.switch('Sus', on_change=show)
ui.radio(['m', 'i', 'r', 'i'], value='m', on_change=show).props('inline')
with ui.row():
    ui.input('quien eres', on_change=show)
    ui.select(['si', 'no'], value='si', on_change=show)
ui.link('tilino...', '/documentation').classes('mt-8')

ui.run()