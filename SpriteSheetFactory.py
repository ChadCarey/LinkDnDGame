from PyGameEngine.Resources import SpriteSheet

def DungeonTileset16x16v4(resourceLoader):
    spriteSheet = resourceLoader.load_image('DungeonTileset16X16.v4.png')
    return SpriteSheet(spriteSheet, 
            {
            # 'name': (x,y,w,h)
            # Dungeon parts
            'wall_top1': (0,0,16,16),
            'wall_top2': (16,0,16,16),
            'wall_top3': (32,0,16,16),
            'wall1': (0,16,16,16),
            'wall2': (16,16,16,16),
            'wall3': (32,16,16,16),
            'short_wall_complete': (0,0,48,32),
            'wall_pipe1': (48,0,16,16),
            'wall_pipe2': (64,0,16,16),
            'wall_pipe3': (80,48,16,16),
            'pillar_top': (96,48,16,16),
            'pillar_mid': (96,64,16,16),
            'pillar_bot': (96,80,16,16),
            'wall_slime': (48,16,16,16),
            'wall_grate1': (64,16,16,16),
            'wall_grate2': (112,0,16,16),
            'wall_grate2': (112,0,16,16),
            'wall_missing_brick1': (64,32,16,16),
            'wall_missing_brick2': (64,48,16,16),
            
            'spitting_statue_top1': (0,48,16,16),
            'spitting_statue_top2': (48,48,16,16),
            'spitting_statue_top3': (160,64,32,16),
            
            'spitting_statue1': (0,64,16,16),
            'spitting_statue2': (16,64,16,16),
            'spitting_statue3': (32,64,16,16),
            'spitting_statue4': (48,64,16,16),
            'spitting_statue5': (64,64,16,16),
            'spitting_statue6': (80,64,16,16),
            'spitting_statue7': (160,80,32,16),
            'spitting_statue8': (192,80,32,16),
            'spitting_statue9': (224,80,32,16),

            'puddle1': (0,80,16,16),
            'puddle2': (16,80,16,16),
            'puddle3': (32,80,16,16),
            'puddle4': (48,80,16,16),
            'puddle5': (64,80,16,16),
            'puddle6': (80,80,16,16),
            'puddle7': (160,96,32,16),
            'puddle8': (192,96,32,16),
            'puddle9': (224,96,32,16),
            
            'skull': (16,48,16,16),
            'stairs': (80,0,32,48),
            'ground1': (32,48,16,16),
            'ground2': (0,32,16,16),
            'ground3': (16,32,16,16),
            'ground4': (32,32,16,16),
            'ground5': (48,32,16,16),
            'ground_patch1': (0,96,16,16),
            'ground_patch2': (16,96,16,16),
            'ground_patch3': (32,96,16,16),
            'ground_patch4': (48,96,16,16),
            'ground_patch5': (0,112,16,16),
            'ground_patch6': (16,112,16,16),
            'ground_patch7': (32,112,16,16),
            'ground_patch8': (48,112,16,16),
            'ground_patch9': (0,128,16,16),
            'ground_patch10': (16,128,16,16),
            'ground_patch11': (32,128,16,16),
            'ground_patch12': (48,128,16,16),
            'ground_patch_complete': (0,96,64,48),
            'boxes1': (80,96,16,32),
            'boxes2': (96,96,16,32),
            'wall_flag1': (192,64,16,16),
            'wall_flag2': (208,64,16,16),
            'wall_flag3': (224,64,16,16),
            'wall_flag4': (240,64,16,16),

            # weapons
            'sword1': (144,0, 16,32),
            'sword2': (160,0,16,32),
            'sword3': (176,0,16,32),
            'sword4': (192,0,16,32),
            'sword5': (208,0,16,32),
            'sword6': (224,0,16,32),
            'sword7': (112,32, 16, 32),
            'sword8': (128,32,16,32),
            'sword9': (144,32,16,32),
            'sword10': (160,32,16,32),
            'sword11': (176,32,16,32),
            'sword12': (192,32,16,32),
            'sword13': (208,32,16,32),
            'sword14': (224,32,16,32),
            'sword15': (112,64,16,32),
            'sword16': (128,64,16,32),
            'sword17': (144,64,16,32),
            'sword18': (160,64,16,32),
            'sword19': (176,64,16,32),
            'sword20': (192,64,16,32),
            'sword21': (208,64,16,32),
            'sword22': (224,64,16,32),
            'hammer': (240,0,16,48),
            'bomb': (240,48,16,16),
            'tools': (112,96,16,32),

            #characters
            'mob1': (0,144,16,16),
            'mob2': (16,144,16,16),
            'mob3': (32,144,16,16),
            'mob4': (48,144,16,16),
            'mob5': (64,144,16,16),
            'mob7': (80,144,16,16),
            'mob8': (96,144,16,16),
            'mob9': (112,144,16,16),
            'mob10': (0,160,16,16),
            'mob11': (16,160,16,16),
            'mob12': (32,160,16,16),
            'mob13': (48,160,16,16),
            'mob14': (64,160,16,16),
            'mob15': (80,160,16,16),
            'mob16': (64,128,16,16),
            }
        )

if __name__ == '__main__':
    from PyGameEngine.GameEngine import GameEngine
    from PyGameEngine.Resources import ResourceLoader
    from PyGameEngine.Entities import EntityBase
    gameEngine = GameEngine()
    loader = ResourceLoader()
    dungeonTileset = DungeonTileset16x16v4(loader)

    x = 0
    y = 0
    biggestY = 16
    for k,v in dungeonTileset.__dict__.iteritems():
        ent = EntityBase(v, None)
        ent.x=x
        ent.y=y
        x+=ent.rect.width
        if biggestY < ent.rect.width:
            biggestY = ent.rect.width
        if gameEngine.width < ent.rect.x+ent.rect.width:
            y += biggestY+16
            x = 0
            biggestY = 16
        gameEngine.renderer.register(ent)

    gameEngine.run()
