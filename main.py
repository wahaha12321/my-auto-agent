import datetime

def main():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello World! 自动化脚本已于 {now} 成功执行。")
    print("目前正在检查今日 AI 论文动态...")

if __name__ == "__main__":
    main()
