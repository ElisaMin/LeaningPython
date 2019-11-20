import os
import sqlite3

# sqlite
db=sqlite3.connect('config.db')
dbc=db.cursor()
def db(do):
    dbc.execute(do)
def updateConfig(id,name,boolean):
    # id=str(id);name=str(name);boolean=str(boolean);
    do="insert into config(id,name,boolean) values("+id+",'"+name+"','"+boolean+"')"
    try:
        db(do)
    except:
       id=int(id)
       table=updateTable()
       if table[id][0]==id:
            return "nothing"
       else:
           print("写入失败")



def updateTable(table):
    table = db("SELECT id,name,boolean from "+table)
    return table

try:
    db("create table config(id int auto_increment primary key not null, name text not null,boolean boolen not null)")
except:
    try:
        db("create table config-test(id int auto_increment primary key not null, name text not null,boolean boolen not null)")
        db("0",'sqlite_is_using',"true")
    except:
        print("表格创建失败，请联系开发者。")



# 环境
line = "-------------------------------------------------------------------------------"
def shell(cmd):  # 访问shell指令
    ret = os.popen(cmd).read()
    return ret
def cls():  # 清屏
    cls = os.system("cls")


# 真方法

def CrackLGUP():
    cls()

    print("破解")


def home():
    cls()
    print("主页")


def main():
    cls()
    print(line + "\n破解LGUP只出现一次。\n" +
          line + "\n\n\t1. 破解LGUP	|	使用该选项请关闭脚本后以管理者运行\n\n\t2. 其他		|	可刷入boot和GSI、一键禁用、切换ab分区等\n\n" +
          line + "\n请选择：", end="")
    c = int(input())
    updateConfig("1","is_frst_run","false")
    table=updateTable("config")
    print(table[0][1])
    CrackLGUP() if c == 1 else home() if c == 2 else main()


main()
