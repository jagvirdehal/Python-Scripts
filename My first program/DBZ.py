import webbrowser

EP = input('What Episode?:  ')

with open ("EPISODE.txt", "r") as myfile:
    eptxt = myfile.read()

if EP == 'ep':
    webbrowser.open('www.animefreak.tv/watch/dragon-ball-z-episode-'+eptxt+'-online#English')
else:
    webbrowser.open('www.animefreak.tv/watch/dragon-ball-z-episode-'+EP+'-online#English')
