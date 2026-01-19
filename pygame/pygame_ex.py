import pygame

# 1.초기화
pygame.init()
# 2.게임화면설정
size = [400, 900]
screen = pygame.display.set_mode(size)  # 게임화면의 크기
title = "pygame_0119"  #  게임제목
pygame.display.set_caption(title)  # 파이게임 실행 시 상단에 나오는 게임 제목
# 3.게임내에서의 설정 => 변수
clock = pygame.time.Clock()
black_color = (0, 0, 0)

class Img_Object:
    def __init__(self):
        self.x = 0
        self.y = 0
    def add_img(self, address):
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()
        else:
            self.img = pygame.image.load(address)
    def change_size(self, width, height):
        self.img = pygame.transform.scale(self.img, (width, height))
        self.width , self.height = self.img.get_size()
    def show_img(self):
        screen.blit(self.img, (self.x, self.y))
        
hero = Img_Object()  
hero.add_img("C:/Users/admin/Desktop/pyhon_25_12/pygame/hero.jpg")       
hero.change_size(80, 80)
hero.x = round(size[0] / 2) - round(hero.width / 2)
hero.y = size[1] - hero.height - 100
hero.move = 30
k = 0
# 4.이벤트
system_exit = 0
while system_exit == 0:
    clock.tick(60)  # fps설정 => 프레임속도
    # 입력(키보드, 마우스)의 감지 => 활용
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            system_exit = 1
        if event.type == pygame.KEYDOWN: # 키가 눌렸을 때
            if event.key == pygame.K_LEFT: # 방향키 왼쪽
                hero.x -= hero.move
            if event.key == pygame.K_RIGHT: # 방향키 오른쪽    
                hero.x += hero.move
    # 변화(입력에 따른 변화, 시간에 따른 변화)
    k += 1

    # 전사작업(그리기)
    screen.fill(black_color)
    hero.show_img()
    # 업데이트
    pygame.display.flip()
# 종료
pygame.quit()
