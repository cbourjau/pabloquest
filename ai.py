from gameclass import *import main_functions as mfimport fovimport interface as idef take_turn(v): #game,who##    print v.name +' turn start',v.get('align')              #get closest enemy        ene=closerEnemy(v)                if ene==None: #if no enemy move_random        if v.last_enemy_pos!=None:            x,y=v.last_enemy_pos            move_towards(v,x,y)            if x==v.x and y==v.y:                v.last_enemy_pos=None                    else:            if is_enemy(v,DB.p)==0:                move_towards(v,DB.p.x,DB.p.y)            move_random(v)                    return        #if low hp move away    v.last_enemy_pos=(ene.x,ene.y) #remember position  ##    if v.hp*100/v.maxhp<30:##        move_away(v,ene.x,ene.y)##        ##        return    if v.special_attack!=None and mf.d(v.ratio_special_attack)==1:        v.special_attack(ene)        v.wait+=8        return        if v.distance_to(ene.x,ene.y)<2:        v.attack(ene)        return    #move towards                    move_towards(v,ene.x,ene.y)    i.draw_game(DB,0)    def closerEnemy(who):        dist=999    for el in DB.inv:        if is_enemy(el,who) and fov.fov_check(who.x,who.y):            nd=el.distance_to(who.x,who.y)            x,y=el.x,el.y            if nd<dist: #and fov.fov_check(who.x,who.y):                closest=el                dist=nd    if dist!=999:        return closest    return None    def move_towards(self, target_x, target_y):    possible=[]        for l in  mf.closetiles((self.x,self.y)):        x,y=l        if mf.isblocked(x,y)==0:            possible.append(l)        choice=(0,0)    for el in possible:                if mf.distance(choice,(target_x,target_y))>mf.distance(el,(target_x,target_y)):            choice=el        x,y=choice    x-=self.x    y-=self.y        self.walk(x,y)        def move_random(v):    possible=[]    possible.append((0,0))    for l in mf.closetiles((v.x,v.y)):        x,y=l        if mf.isblocked(x,y)==0:            possible.append(l)        x,y=random.choice(possible)    x-=v.x    y-=v.y        v.walk(x,y)            def move_away(self, target_x, target_y):            possible=[[0,0]]        for l in mf.closetiles((self.x,self.y)):        x,y=l        if mf.isblocked(x,y)==0:            possible.append(l)        choice=random.choice(possible)    for el in possible:                if mf.distance(choice,(target_x,target_y))<mf.distance(el,(target_x,target_y)):            choice=el        x,y=choice    x-=self.x    y-=self.y        self.walk(x,y)             def is_enemy(el,who) :    if who.isFighter and el.isFighter:        if el.align==who.align:            return 0        return 1    return 0        