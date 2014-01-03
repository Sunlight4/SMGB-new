import resources, pygame, easygui
def intro(screen):
    #path list begins here
    music_path=resources.get_resource_path("BiancoHills.ogg", "music/Areas")
    mario_path=resources.get_resource_path("Mario.png", "images")
    grass_path=resources.get_resource_path("Grass.png", "images")
    bg_path=resources.get_resource_path("Grass_BG.png", "bg")
    jump_path=resources.get_resource_path("Mario_run_sprite.png", "images")
    mario=pygame.image.load(mario_path)
    grass=pygame.image.load(grass_path)
    bg=pygame.image.load(bg_path)
    mario_jump=pygame.image.load(jump_path)
    blit=screen.blit
    flip=pygame.display.flip
    fill=screen.fill
    music=pygame.mixer.music
    music.stop()
    music.load(music_path)
    music.set_volume(1)
    music.play(-1)
    mariox=0
    marioy=0
    jump=False
    up=True
    traveled=0
    while mariox < 640:
        fill([0,0,0])
        blit(bg, [0,0])
        for i in [0, 72, 144, 216, 360, 432, 576]:
            blit(grass, [i, 200])
        marioh=mario.get_rect().height
        if mariox==288:jump=True
        elif mariox==504:jump=True
        if traveled >=72:jump=False; traveled=0
        if not jump:
            blit(mario, [mariox, 200-marioh+marioy])
            up=True
        else:
            traveled+=1
            if marioy<=-36:up=False
            if up:marioy-=1
            else:marioy+=1
            blit(mario_jump, [mariox, 200-marioh+marioy])
        flip()
        mariox+=1
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    jump=True
    #TODO:replace with code to run game
    pygame.quit()
    raise SystemExit
