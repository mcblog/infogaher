#作者:古酒道人
#请勿作违法用途
import sys
import time
from scripts import inittarget,ipfind,subdomain
def main(target):
    text="""
 ██            ████                              ██   ██                    
░░            ░██░            █████             ░██  ░██                    
 ██ ███████  ██████  ██████  ██░░░██  ██████   ██████░██       █████  ██████
░██░░██░░░██░░░██░  ██░░░░██░██  ░██ ░░░░░░██ ░░░██░ ░██████  ██░░░██░░██░░█
░██ ░██  ░██  ░██  ░██   ░██░░██████  ███████   ░██  ░██░░░██░███████ ░██ ░ 
░██ ░██  ░██  ░██  ░██   ░██ ░░░░░██ ██░░░░██   ░██  ░██  ░██░██░░░░  ░██   
░██ ███  ░██  ░██  ░░██████   █████ ░░████████  ░░██ ░██  ░██░░██████░███   
░░ ░░░   ░░   ░░    ░░░░░░   ░░░░░   ░░░░░░░░    ░░  ░░   ░░  ░░░░░░ ░░░    
                   古酒道人的信息搜集小工具
    """
    print(text)
    inittarget.initworkfloder(target)
while True:
    if __name__ == '__main__':
        while True:
            try:
                while (str(sys.argv[1])=='-i'):
                    main(str(sys.argv[2]))
                    sys.exit()
                # 删除目录应该不用写，怕误操作
            except Exception as information:
                title = "出现未知异常！"
                content = "出现了未知异常，请及时反馈错误信息哦！"
                sys.exit()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
