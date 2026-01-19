import pygame

# 1.초기화
pygame.init()
# 2.게임화면설정
size = [500, 600]
screen = pygame.display.set_mode(size) # 게임화면의 크기
# 3.게임내에서의 설정 => 변수
clock = pygame.time.Clock()
black_color = (0,0,0)
# 4.이벤트
system_exit = 0
while (system_exit == 0):
    clock.tick(5) # fps설정 => 프레임속도
    # 입력(키보드, 마우스)의 감지 => 활용
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            system_exit = 1
    # 변화(입력에 따른 변화, 시간에 따른 변화)
    # 전사작업(그리기)
    screen.fill(black_color)
    # 업데이트
    pygame.display.flip()
# 종료
pygame.quit()