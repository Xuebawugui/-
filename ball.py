import pygame
import random
import math
import time

# 初始化 Pygame
pygame.init()

# 设置屏幕大小
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("颜色碰撞游戏")

# 固定三种颜色
COLORS = [(255, 0, 0), (0, 0, 255), (0, 255, 0)]  # 红、蓝、绿

# 颜色随机生成（只选固定的三种颜色）
def random_color():
    return random.choice(COLORS)

# 小球类
class Ball:
    def __init__(self, color):
        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(50, HEIGHT - 50)
        self.radius = 20
        self.color = color
        self.dx = random.choice([-2, 2])  # 随机速度
        self.dy = random.choice([-2, 2])
        self.last_collision_time = 0  # 记录上次变色时间

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # 碰到墙壁反弹
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.dx *= -1
        if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
            self.dy *= -1

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    # 检测两个小球是否碰撞
    def check_collision(self, other):
        distance = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return distance < self.radius * 2

    # 碰撞后变色，并设置冷却时间
    def change_color(self, other):
        now = time.time()
        if now - self.last_collision_time > 0.3:  # 0.3秒冷却
            self.color = random.choice([self.color, other.color])  # 颜色随机从两个小球中选
            self.last_collision_time = now

# 创建小球列表，每种颜色4个小球
balls = [Ball(color) for color in COLORS for _ in range(4)]

# 设定游戏时间
MAX_TIME = 60  # 30秒后游戏结束
start_time = pygame.time.get_ticks()

# 游戏循环
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((30, 30, 30))  # 背景色
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 移动小球并检测碰撞
    for ball in balls:
        ball.move()
        ball.draw()

    # 颜色碰撞逻辑
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            if balls[i].check_collision(balls[j]):
                balls[i].change_color(balls[j])  # 触发变色
                balls[j].change_color(balls[i])  # 触发变色

                # 让小球稍微弹开
                balls[i].dx *= -1
                balls[i].dy *= -1
                balls[j].dx *= -1
                balls[j].dy *= -1

    # 计算游戏时间
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # 转换为秒
    font = pygame.font.Font(None, 36)
    timer_text = font.render(f"Time: {int(MAX_TIME - elapsed_time)}s", True, (255, 255, 255))
    screen.blit(timer_text, (10, 10))

    # **游戏终结判断**
    # 1. 检查是否所有小球颜色相同
    first_color = balls[0].color
    if all(ball.color == first_color for ball in balls):
        win_text = font.render("All colors matched! Game Over!", True, (255, 255, 0))
        screen.blit(win_text, (WIDTH // 4, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(2000)  # 停留2秒
        break

    # 2. 超时结束
    if elapsed_time >= MAX_TIME:
        timeout_text = font.render("Time Up! Game Over!", True, (255, 0, 0))
        screen.blit(timeout_text, (WIDTH // 3, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(2000)  # 停留2秒
        break

    pygame.display.flip()
    clock.tick(60)  # 控制帧率

pygame.quit()
