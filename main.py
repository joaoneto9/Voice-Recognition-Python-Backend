import pyaudio
import wave

audio = pyaudio.PyAudio()  # instância da classe Pyaudio que permite a captura de informações do microfone

stream = audio.open( # objeto 'stream' de fluxo de áudio, que coleta as informações de áudio

    input=True, # indica que o fluxo é para entrada de áudio somente

    format=pyaudio.paInt16, # define o formato do áudio como 16 bits.
    # quanto maior o valor, maior a qualidade do áudio e maior o tamanho do arquivo gerado

    channels=1, # determina a quantidade de canais que o arquivo terá
    # como se trata de um áudio mono, possui apenas um canal (um áudio estéreo teria 2)

    rate=44000, # número de amostras de áudio coletadas por segundo, medido em Hertz (Hz)
    # quanto maior, tem-se um áudio mais preciso e de maior qualidade
    frames_per_buffer=1024 # tamanho do buffer de captura de áudio em quadros (frames)
    # "buffer" é um espaço de memória temporária alocada para armazenar uma quanidade limitada de dados antes que eles sejam processados definitivamente

) 

frames = [] # inicizalização da lista para armzaenar os blocos de áudio de 1024 quadros

try: # bloco try-except que inicia a captura de áudio até que ela seja interrompida via teclado
    while True:
        bloco = stream.read(1024) # lê um bloco de áudio com 1024 amostras
        frames.append(bloco) # adiciona o bloco à lista 'frames'
except KeyboardInterrupt:
    pass

stream.start_stream()
stream.close() # finaliza o fluxo de áudio (stream)
audio.terminate() # encerra a instância 'audio'

arquivo_final = wave.open("gravacao.wav", "wb") # abre o arquivo 'gravacao.wav' com o modo de escrita em binário - wb

arquivo_final.setnchannels(1); # configura o arquivo para ser de áudio mono
arquivo_final.setframerate(44000) # define a taxa de amostragem
arquivo_final.setsampwidth(audio.get_sample_size(pyaudio.paInt16)) # define o formato de 16 bits

arquivo_final.writeframes(b"".join(frames)) # escreve os blocos em 'gravacao.wav', concatenando cada elemento de 'frames' no formato de bytes (indicado pelo b)

arquivo_final.close() # fecha-se o arquivo
