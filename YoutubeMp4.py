from flet import * #Importando Tudo do flet
from Downloads import Downloads #Puxando a função
def main(page: Page):
    URLs = TextField( # Input Do Tipo Texto para por URL
        label="Url",
        color="#00fce2",
        border_color='#00ff7f',
        text_size=20,
        cursor_color="white",
        focused_color="white",
       
        )
    Formatos = Dropdown( #Selecionar Formato
        options=[
            dropdown.Option("Mp3"),
            dropdown.Option("Mp4")
        ],
        value="Mp4",
        width=200,
        border_color="white",
        color='#00ff7f',
        bgcolor='#ffff',
        text_size=20,
        label="Formato",
        label_style=alignment.center
        
    )

    ThemeMode.DARK

    def Play_Downloads(e):#função para baixar video 
 
        try: # Caso Tenha uma URL baixar o tal video
            Downloads(URLs.value,Formatos.value)
        except: # Caso De erro
            page.snack_bar = SnackBar(Text('[ERRO]'),TextStyle(size=25)) #Aviso de Erro
            page.snack_bar.open = True
            page.update()
    page.padding = 25 #Distanciamento
    page.bgcolor = "#151518" # Cor
    Baixar = ElevatedButton("Baixar",on_click=Play_Downloads) # Botão-Baixar


    



    page.add(      # Adicionando os Elementos Já Pronto na tela.
        URLs,
        Formatos,
        Baixar,
      
     )
    
    














    

app(target=main) #Iniciando Tudo.