from pytube import YouTube
import uuid

class Downloader:

    def __init__(self) -> None:
        self.running = True
        self.musics_folder = '/home/aluno/Música'
    
    def start(self) -> None:
        while self.running:

            print('[0] - Sair do programa')
            print('[1] - Listar todas as músicas baixadas')
            print('[2] - Listar todas as bandas cadastradas')
            print('[3] - Baixar uma música')

            opt = input('Qual opção?: ')

            match opt:

                case '0':
                    self.running = False
                
                case '3':
                    confirm = False
                    while not confirm:

                        band  = input('Nome da banda: ')
                        music = input('Nome da música: ')
                        style = input('Nome do estilo músical: ')
                        link  = input('Link da música: ')

                        confirm = input('Está tudo certo? [S/N]: ').lower() == 's'

                    self.download(link)

    def download(self, url: str) -> None:
        stream = YouTube(url).streams.filter(only_audio=True).first()
        stream.download(output_path=self.musics_folder, filename=f"{ uuid.uuid4() }.mp3")
        print("Download realizado com sucesso!")

if __name__ == '__main__':
    downloader = Downloader()
    downloader.start()