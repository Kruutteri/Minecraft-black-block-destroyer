# Minecraft-black-block-destroyer
Pretty useless but cool I guess. Destroys all the black blocks in a 20x20 arena. The thing I'm most proud in this code is the function that I made to viusally calculate the distance of a block using only the y-cordinate from your own computer screen. Everything else is pretty basic I would say. Cool mini-project regardless.

What libraries you need:
pip install pyautogui
pip install keyboard
pip install pillow
pip install pywin32
pip install pypiwin32

You need to also download the directkeys.py file and put it in the same directory as the main file

How to use:
1) Replace some blocks texture in your texturepack with a 64x64 black image (RGB(0,0,0))
2) Set your minecraft sensitivity to 60%
3) Create a totally flat world in creative mode
4) Put a block in the ground
5) Count 10 blocks in each direction from the center block and place a block on the 10th block
6) Connect the blocks
7) Place your black blocks on the arena you have created (try not to place them behind each other since it will break the code)
8) Run the code and if you need it to stop running, hold "l" and it will stop
