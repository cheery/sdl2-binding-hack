import sdl2

print 'init res', sdl2.init(0x20)

SDL_WINDOWPOS_UNDEFINED_MASK    = 0x1FFF0000
SDL_WINDOWPOS_UNDEFINED_DISPLAY = lambda x: SDL_WINDOWPOS_UNDEFINED_MASK | x
SDL_WINDOWPOS_UNDEFINED         = SDL_WINDOWPOS_UNDEFINED_DISPLAY(0)

window = sdl2.createWindow("kakkaa", 
    SDL_WINDOWPOS_UNDEFINED,
    SDL_WINDOWPOS_UNDEFINED,
    320, 320, 0)

sdl2.delay(2000)

sdl2.destroyWindow(window)
sdl2.quit()
