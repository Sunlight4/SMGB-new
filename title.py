import pygame, resources, optparse, intro
p=optparse.OptionParser()
p.add_option('--test', '-t', action='store_true')
options, arguments=p.parse_args()
pygame.init()
mixer=pygame.mixer
mixer.init()
music=mixer.music
screen=pygame.display.set_mode([640,480])
flip=pygame.display.flip
blit=screen.blit
load=pygame.image.load
fill=screen.fill
#path list begins here
title_path=resources.get_resource_path("FinalBowserCastleSMG2.ogg", "music/Areas")
titlebg_path=resources.get_resource_path("SuperMarioGalaxyTitle.png", "images")
#path list ends here
music.load(title_path)
music.set_volume(1)
music.play(-1)
titlebg=load(titlebg_path)
fill([0,0,0])
blit(titlebg, [0,0])
flip()
run=1
q=0
clear=0
if options.test:clear=1
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            q=1
            run=0
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                run=0
if q:pygame.quit()
if clear:resources.done()
intro.intro(screen)
