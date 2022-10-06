from pytube import YouTube
import moviepy.editor as mp
import re
import os
def MP3(url):
    path = str('Download')
    yt = YouTube(url)
    ys = yt.streams.filter(only_audio=True).first().download(path)
    print('-='*20)
    print('Baixado!')
    print('-='*20)
    print('Convertendo para MP3')
    print('-='*20)
    for file in os.listdir(path):
        if re.search('mp4', file):
            mp4_path = os.path.join(path, file)
            mp3_path = os.path.join(path, os.path.splitext(file)[0] +' .mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)
def MP4(url):
    path = str('Download')
    yt = YouTube(url)
    ys = yt.streams.filter().first().download(path)
    print('-='*20)
    print('Baixado!')
    
#Instale o PYTUBE e MOVIEPY
while True:

    choice = int(input('''Quer baixar:
    ( 0 ) MP3
    ( 1 ) MP4
    :  '''))
    if choice == 0:
        linkk = str(input('Link (only youtube!): '))
        MP3(linkk)
        break
    elif choice == 1:
        linkk = str(input('Link (only youtube!): '))
        MP4(linkk)
    else:
        print('Erro!')


# print('Baixado!')

# print('Convertendo para MP3')
# for file in os.listdir(pasta):
#     if re.search('mp4', file):
#         mp4_path = os.path.join(pasta, file)
#         mp3_path = os.path.join(pasta, os.path.splitext(file)[0] + '.mp3')
#         new_file = mp.AudioFileClip(mp4_path)
#         new_file.write_audiofile(mp3_path)
#         os.remove(mp4_path)
# print('FINALIZADO!')