with open('/Users/Pedro/Documents/Principal/Python/Bootrain Data Science/Cancion.txt', 'a') as f:
    f.write('\n\nCanción para mi muerte\nCompositor: Carlos Alberto García\nArtista: Sui Generis')

with open('/Users/Pedro/Documents/Principal/Python/Bootrain Data Science/Cancion.txt', 'r') as f:
    lyrics = f.read()

print(lyrics)