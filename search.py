import urllib.request
import re
""" 
função para procurar vídeos no youtube.
@param String of video
@return link
"""
def Search(pedido):
    pedido = pedido.replace(" ","+")
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + pedido )
    videoIds=re.findall(r"watch\?v=(\S{11})",html.read().decode())
    videoUrl = "https://www.youtube.com/watch?v=" + videoIds[0]
    return videoUrl

