# This is a test script to run LinkConverter
from link_converter.LinkConverter import LinkConverter

if __name__ == "__main__":
    linkConverter = LinkConverter()
    links1 = linkConverter.convert_link('https://play.google.com/music/m/Todhdrnwy3w3clgsqttgsbrklqi?t=This_Is_the_Beginning_-_Shakey_Graves')
    links2 = linkConverter.convert_link('https://open.spotify.com/track/0GswbpVTZBVwvE4gZLaX7R')
    links3 = linkConverter.convert_link('https://open.spotify.com/track/0KDn1UsD2ym34dCT4P9ebj')
    links4 = linkConverter.convert_link('https://open.spotify.com/album/439SsuO2Esw1G67Xuw1HPS')
    links5 = linkConverter.convert_link('https://open.spotify.com/track/2Sm1PY9pcoQzFDL1NJsJj8')
    links6 = linkConverter.convert_link('https://open.spotify.com/album/6wbLFpKc9QnhMMWIVesC83')
    links7 = linkConverter.convert_link('https://soundcloud.com/shakey-graves-official/sets/and-the-war-came')
    links8 = linkConverter.convert_link('https://soundcloud.com/kendrick-lamar-music/sets/damn-86')
    links9 = linkConverter.convert_link('https://play.google.com/music/m/Bx7aimn4qvv7hjcgijqltqe27k4?t=Be_Kind_to_Yourself_-_Willow_Beats')
    links10 = linkConverter.convert_link('https://soundcloud.com/san-fermin-1/no-promises-1?in=san-fermin-1/sets/belong-11')
    links11 = linkConverter.convert_link('https://itunes.apple.com/us/album/freudian/1265893523')
    links12 = linkConverter.convert_link('https://itunes.apple.com/us/album/the-autobiography/1256952577')
    links13 = linkConverter.convert_link('https://itunes.apple.com/us/album/eleanor-rigby/401136641?i=401136644')
    links14 = linkConverter.convert_link('https://play.google.com/music/m/Tmnguilcqsjlj2mmmi6t6owif2a?t=Just_To_Talk_To_You_-_Nathaniel_Rateliff__The_Night_Sweats')
    links15 = linkConverter.convert_link('https://open.spotify.com/track/752Dp89E27wUgg20JV5PWA')

    print('\n')
    print(links1)
    print(links2)
    print(links3)
    print(links4)
    print(links5)
    print(links6)
    print(links7)
    print(links8)
    print(links9)
    print(links10)
    print(links11)
    print(links12)
    print(links13)
    print(links14)
    print(links15)
