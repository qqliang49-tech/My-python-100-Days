def evaluate_lenght(test):
    if len(test) > 50:
        return "文案过长（超过50字）"
    return "文案长度合适"
bad_words = ["第一","最","绝对"]
good_words = ["治愈","猫","晚安"]
def evaluate_badwords(test):
    for w in bad_words:
        if w in test:
            return f"包含违禁词:{w}"
    return "不包含违禁词"
def score(test):
    score = 60
    for w in good_words:
        if w in test:
            score +=10
    return f"文案得分：{score}"
def evaluate(test):
    return [evaluate_lenght(test),evaluate_badwords(test),score(test)]
while True:
    test = input("请输入文案(输入exit退出)：")
    if test.lower() == "exit":
        break
    result = "\n".join(evaluate(test))
    print("-"*30)
    print(f"测评结果:\n{result}")
    print("-"*30)