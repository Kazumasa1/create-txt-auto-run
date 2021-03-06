import pyautogui
import random
import string


# 左上の方にカーソルを持ってきてクリック
pyautogui.click(500, 500)

# ファイルをいくつ作成するか？
numberOfFiles = 10

n = 1
alf = []
alf_set = []

# 重複しないアルファベット2文字の組合せを<numberOfFiles>個生成
while len(alf) <= numberOfFiles:
    alf_set = ["".join(random.sample(string.ascii_lowercase, k=2)) for _ in range(numberOfFiles)]
    # 重複を削除
    alf_set = list(set(alf_set))
    alf.extend(alf_set)


while n <= numberOfFiles:
    # ファイルの作成処理
    # 「vi 00<n>.txt」を入力
    pyautogui.typewrite('vi ' + str(n).zfill(3) + '.txt')
    # returnキーを押す
    pyautogui.keyDown('return')


    # ファイル内容の入力処理
    # 入力モードに移行
    pyautogui.keyDown('i')
    pyautogui.typewrite(str(n).zfill(3) + alf[n-1] )
    # 入力モードを終了
    pyautogui.keyDown('esc')
    # 保存して閉じる
    pyautogui.typewrite(':wq')
    # returnキーを押す
    pyautogui.keyDown('return')
    n = int(n) + 1
