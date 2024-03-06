# ライブラリのインポート
from random import randint

# 単語リストの設定
word_list: list = ["Japanese", "train", "zoo", "work", "carrer"]

# 選択肢の設定
word_dic: dict = {
    "Japanese": ("英語", "ドイツ語", "日本語", "中国語"),
    "train": ("飛行機", "電車", "船", "車"),
    "zoo": ("図書館", "遊園地", "美術館", "動物園"),
    "work": ("働く", "遊ぶ", "死ぬ", "食べる"),
    "carrer": ("カレー", "未来", "経歴", "カメラ")
    }

correct_answer: dict = {
    "Japanese": 3,
    "train": 2,
    "zoo": 4,
    "work": 1,
    "carrer": 3
    }


# 問題選択の処理
def QuessionSelected() -> tuple:
    # 問題用の変数
    quession_word: str
    quession_choice: tuple
    
    # 戻り値の定義
    random_index: int
        
    # 単語辞書の総数からランダムな数字を算出
    random_index = randint(0, (len(word_list)-1))
        
    # 単語リストから出題する単語を抽出
    for que in word_dic.items():
        if word_list[random_index] == que[0]:
            quession_word = que[0]
            quession_choice = que[1]
            
            return quession_word, quession_choice
        

# 正誤判定
def answerJudge(s_no: int, quession_tuple: tuple) -> str:
    # 回答内容が正しいか判定
    for word in correct_answer.keys():
        if word == quession_tuple[0]:
            if s_no == correct_answer[word]:
                return "正解！"
            else:
                return "残念、不正解!"


def main_method():
    # 問題の表示
    quession_tuple: tuple = QuessionSelected()
    print(f"次の単語の意味は:{quession_tuple[0]}")

    # 判定の際に仕様する解答群を辞書に格納し、選択肢を表示
    choice_dic: dict = {}
    for no, choice in enumerate(quession_tuple[1]):
        choice_dic[no] = choice
        print(f"{no + 1}:{choice}")

    # 回答の入力
    s_no: int = int(input("回答Noを入力してください:"))

    # 入力した解答が正しいか判定処理を呼び出す
    ans: str = answerJudge(s_no, quession_tuple)
    print(ans)