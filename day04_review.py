bad_words = ["第一", "最", "绝对"]
good_words = ["治愈", "猫", "晚安"]


def evaluate_all_in_one(text):
    # 1. 预设初始状态（防止出现 None）
    status = "✅ 审核通过"
    score = 60
    
    # 2. 长度检查（如果失败，直接更新状态）
    if len(text) > 50:
        status = "❌ 文案过长（超过50字）"
        score = 0
    
    # 3. 违禁词检查（如果失败，直接更新状态）
    # 注意：如果长度已经报错，我们通常就不再检查违禁词了，所以加个判断
    if score != 0: 
        for w in bad_words:
            if w in text:
                status = f"❌ 包含违禁词：{w}"
                score = 0
                break # 发现一个就停，提高效率
    
    # 4. 评分逻辑（只有审核通过的才加分）
    if score != 0:
        for w in good_words:
            if w in text:
                score += 10
                
    # 5. 统一返回（永远返回两个值，绝不 None）
    return status, score


# --- 主循环 ---
while True:
    user_input = input("\n请输入文案（输入 exit 退出, show 查看素材库）：")
    if user_input.lower() == "show":
        try:
            with open("database.txt","r",encoding="utf-8") as f:
                content = f.read()
                if content.strip() == "":
                    print("⚠️ 素材库目前为空")
                else:
                    print(f"---当前素材库---\n{content}")
        except FileNotFoundError:
            print("⚠️ 素材库文件尚未创建！请先存入文案。")
    elif user_input.lower() == "exit":
        print("👋 辛苦了，明天见！")
        break
    
    # 解包获取两个返回值
    else:
        res_status, res_score = evaluate_all_in_one(user_input)
        print("-" * 30)
        print(f"评估结果：{res_status}")
        print(f"最终得分：{res_score}")
        print("-" * 30)
        if res_score > 0:
            with open("database.txt","a",encoding="utf-8") as f:
                f.write(user_input + "\n")
            print("✅ 文案已存入素材库！")
