import json,os,sys,getopt,argparse

def trans(x):
    #将事件转化成对应标号，-1表示不合法事件
    if x == 'PushEvent':
        return 0
    if x == 'IssueCommentEvent':
        return 1
    if x == 'IssuesEvent':
        return 2
    if x == 'PullRequestEvent':
        return 3
    return -1


def read(path):
    #初始化data文件以防重复写入
    with open('data.json', "w", encoding='utf-8') as f2:
        f2.write('')
    #搜索path路径下的所有json文件
    for root, dic, files in os.walk(path):
        for file in files:
            if file[-5:] == '.json':
                json_path = file
                filedir = open(path + '\\' + json_path, 'r', encoding='utf-8')
                with open(json_path, encoding = 'utf-8') as f:
                    for i in f:
                        y = json.loads(i)
                        evetype = trans(y['type'])
                        #如果事件合法，将事件需要的信息提取出来写入data文件
                        if not evetype == -1:
                            #提取关键数据到dict1
                            dict1 = {}
                            dict1['event'] = evetype
                            dict1['user'] = y['actor']['login']
                            dict1['repo'] = y['repo']['name']
                            #再把dict1输出到data
                            dict2 = json.dumps(dict1)
                            with open('data.json', "a", encoding='utf-8') as f2:
                                f2.write(str(dict2) + '\n')


def solve(data, user, repo, event):
    ans = 0
    for i in data:
        y = json.loads(i)
        if not len(user) == 0:
            if not user == y['user']:
                continue
            else:
                pass
        else:
            pass

        if not repo == None:
            if not repo == y['repo']:
                continue
            else:
                pass
        if trans(event) == y['event']:
            ans = ans + 1
        else:
            pass
    return ans


class working():
    #指令参数初始化
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.data = None
        self.argInit()
        print(self.analyse())
    #指令参数添加
    def argInit(self):
        self.parser.add_argument('-i', '--init')
        self.parser.add_argument('-u', '--user')
        self.parser.add_argument('-r', '--repo')
        self.parser.add_argument('-e', '--event')
    #指令分析
    def analyse(self):
        #初始化
        if self.parser.parse_args().init:
            read(self.parser.parse_args().init)
            return 0
        else:
            #访问已处理数据
            if self.data is None:
                self.data = open('data.json', 'r', encoding = 'utf-8')
            return solve(self.data,
                         self.parser.parse_args().user,
                         self.parser.parse_args().repo,
                         self.parser.parse_args().event)

if __name__ == '__main__':
    a = working()




