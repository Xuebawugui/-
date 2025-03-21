颜色碰撞游戏
这款简单的 颜色碰撞游戏 是一款自动化的小游戏，玩家无需操作，游戏通过小球碰撞、变色和演化来呈现不同的效果。该游戏使用 Python 和 Pygame 实现，目标是通过控制小球的碰撞规则，模拟颜色的变化，最终达到游戏结束条件。

游戏规则
初始设置：

游戏开始时，屏幕上会出现 12 个小球，每种颜色（红色、蓝色、绿色）各有 4 个小球。
小球会自动移动，并在屏幕边缘反弹。
碰撞与变色：

每次小球之间发生碰撞时，它们会随机变成两个小球的颜色之一。
每次碰撞后，小球会有一个冷却时间（0.3秒），避免频繁变色导致闪烁。
终结条件：

时间限制：30秒后，如果游戏没有结束，将提示“时间到，游戏结束”。
颜色统一：如果所有小球变成相同颜色，游戏将结束，提示“所有颜色匹配，游戏结束”。
游戏功能
简单的碰撞检测：通过 Pygame 的 pygame.draw.circle 和数学公式检测小球之间的碰撞。
颜色变化：碰撞后小球随机选择一个新颜色，从碰撞的两个小球颜色中选取。
游戏结束判断：判断所有小球是否变成相同颜色，或者超时结束。

运行要求
Python 3.x
Pygame 库

扩展和改进
增加更多颜色：可以根据需要添加更多颜色的小球，增加游戏的多样性。
更多游戏终结条件：比如设置更复杂的规则，例如随机生成的障碍物等。
音效和动画：为游戏增加音效和更加丰富的动画效果，提升游戏体验。
