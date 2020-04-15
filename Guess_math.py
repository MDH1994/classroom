import os
import random       #统计
import requests     #网络请求
import re           #转义字符
class guess_maths():
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return repr(self.name)
    def creat_name(self):
        play_list = []
        name_list = []
        new_name_list = [player, 0, 0, 0]
        with open('play_name.txt','r', encoding='utf-8-sig') as f:
            game_list=f.read().splitlines()
            for line in game_list:
                ls=line.split()
                play_list.append(ls)
            #print(play_list)
            if len(play_list)!=0:
                pass
            else:
                play_list.append(new_name_list)
                print('欢迎进入游戏，你是本区域的首位玩家')
            for name_list in play_list:
                if player in name_list:
                    print('{},你已经玩了{}次，最少{}轮猜出答案，平均{}轮猜对答案，开始游戏'.format(name_list[0],name_list[1],name_list[2],name_list[3]))
                    req = requests.get('https://python666.cn/cls/number/guess/')
                    number = req.json()
                    count = 0
                    num = float(name_list[1]) * float(name_list[3])
                    while True:
                        answer=input('请猜一个1-100的数字:')
                        if re.match("^(\\d|[1-9]\\d|100)$",answer):
                        #if answer in range(0,101):
                            print(type(answer),type(number),type(name_list[2]))
                            count+=1
                            answer=int(answer)
                            if answer>number:
                                print('猜大了，请再试试')
                                continue
                            elif answer<number:
                                print('猜小了，请再试试')
                            else:
                                name_list[1] = int(name_list[1]) + 1
                                name_list[3] = (num + count) / float(name_list[1])
                                print('猜对了，你一共猜了{}轮'.format(count))
                                if int(name_list[2])<=count and (int(name_list[2])!=0):
                                    name_list[2] = name_list[2]
                                else:
                                    name_list[2] = count
                                print('{},你已经玩了{}次，最少{}轮猜出答案，平均{}轮猜对答案，开始游戏'.format(name_list[0], name_list[1],name_list[2], name_list[3]))
                                choose = input('是否继续游戏？（输入y继续，其他退出)')
                                if choose!='y':
                                    print('游戏结束，欢迎下次再来')
                                    break       #跳出while
                                else:
                                    req = requests.get('https://python666.cn/cls/number/guess/')
                                    print('测试')
                        else:
                            print('输入有误，请重新输入数字')
                    break  #打破for
                else:
                    if new_name_list in play_list:
                        pass
                    else:
                        play_list.append(new_name_list)
        with open('play_name.txt','w', encoding='utf-8') as f1:
            for name_list in play_list:
                for i in name_list:
                    f1.write(str(i)+'\t')
                f1.write('\n')
while True:
    player=input('请输入你的姓名：')
    if re.match(r'[a-zA-Z\u4E00-\u9FA5]+',player):
        game=guess_maths(player)
        game.creat_name()
        break
    else:
        print('请重新输入玩家姓名，可采用汉字或字母组合')