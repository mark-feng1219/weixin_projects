import flask
import sqlite3
import json

app = flask.Flask(__name__)


class StudentDB:
    def openDB(self):  # 打开学生数据库
        self.con = sqlite3.connect("students.db")
        self.cursor = self.con.cursor()

    def closeDB(self):  # 关闭学生数据库
        self.con.commit()
        self.con.close()

    def initTable(self):  # 初始化/建立一张表
        res = {}
        try:
            self.cursor.execute("create table students(No varchar(16)primary key,Name varchar(16),"
                                "Sex varchar(8),Age int,Favorite varchar(16))")
            self.cursor.execute("insert into students(No,Name,Sex,Age,Favorite)values(?,?,?,?,?)",
                                (20, "陈杜康", "男", 20, "英雄联盟"))
            self.cursor.execute("insert into students(No,Name,Sex,Age,Favorite)values(?,?,?,?,?)",
                                (21, "郭巧闲", "男", 19, "小新"))
            self.cursor.execute("insert into students(No,Name,Sex,Age,Favorite)values(?,?,?,?,?)",
                                (22, "江仁化", "男", 21, "Steam"))
            self.cursor.execute("insert into students(No,Name,Sex,Age,Favorite)values(?,?,?,?,?)",
                                (23, "蒋英语", "女", 20, "Java"))  # 创建包含我和舍友的信息表
            res["msg"] = "OK"
        except Exception as err:
            res["msg"] = str(err)
        return res

    def insertRow(self, No, Name, Sex, Age, Favorite):  # 增加学生数据
        res = {}
        try:
            self.cursor.execute("insert into students(No,Name,Sex,Age,Favorite)values(?,?,?,?,?)",
                                (No, Name, Sex, Age, Favorite))
            res["msg"] = "OK"
        except Exception as err:
            res["msg"] = str(err)
        return res

    def deleteRow(self, No):  # 删除学生数据
        res = {}
        try:
            self.cursor.execute("delete from  students where No=?", (No,))
            res["msg"] = "OK"
        except Exception as err:
            res["msg"] = str(err)
        return res

    def updateRow(self, No, Name, Sex, Age, Favorite, Num):  # 修改某位学生的数据
        res = {}
        try:
            self.cursor.execute("update students set No=?,Name = ?,Sex = ?,Age = ?,Favorite = ? "
                                "where No = ?", (No, Name, Sex, Age, Favorite, Num))
            res["msg"] = "OK"
        except Exception as err:
            res["msg"] = str(err)
        return res

    def selectRow(self, No):  # 查询某位学生的数据
        res = {}
        try:
            data = {}
            self.cursor.execute("select * from students order by No")
            rows = self.cursor.fetchall()
            for row in rows:
                if row[0] == No:  # 如果找到与No相同的row,则记录下来
                    data["No"] = row[0]
                    data["Name"] = row[1]
                    data["Sex"] = row[2]
                    data["Age"] = row[3]
                    data["Favorite"] = row[4]
                    break
            res["msg"] = "OK"
            res["data"] = data
        except Exception as err:
            res["msg"] = str(err)
        return res

    def returnALL(self):
        res = {}
        try:
            data = []
            self.cursor.execute("select * from students order by No")
            rows = self.cursor.fetchall()
            for row in rows:
                d = {"No": row[0], "Name": row[1], "Sex": row[2], "Age": row[3], "Favorite": row[4]}
                data.append(d)
            res["msg"] = "OK"
            res["data"] = data
        except Exception as err:
            res["msg"] = str(err)
        return res


@app.route("/", methods=["GET", "POST"])
def process():  # 这边曾经误写了process(self),结果报错了
    opt = flask.request.values.get("opt") if "opt" in flask.request.values else ""
    res = {}
    db = StudentDB()
    db.openDB()
    if opt == "init":
        res = db.initTable()
    elif opt == "insert":  # 增
        No = flask.request.values.get("No") if "No" in flask.request.values else ""
        Name = flask.request.values.get("Name") if "Name" in flask.request.values else ""
        Sex = flask.request.values.get("Sex") if "Sex" in flask.request.values else ""
        Age = flask.request.values.get("Age") if "Age" in flask.request.values else ""
        Favorite = flask.request.values.get("Favorite") if "Favorite" in flask.request.values else ""
        res = db.insertRow(No, Name, Sex, Age, Favorite)
    elif opt == "delete":  # 删
        No = flask.request.values.get("No") if "No" in flask.request.values else ""
        res = db.deleteRow(No)
    elif opt == "update":  # 改
        No = flask.request.values.get("No") if "No" in flask.request.values else ""
        Name = flask.request.values.get("Name") if "Name" in flask.request.values else ""
        Sex = flask.request.values.get("Sex") if "Sex" in flask.request.values else ""
        Age = flask.request.values.get("Age") if "Age" in flask.request.values else ""
        Favorite = flask.request.values.get("Favorite") if "Favorite" in flask.request.values else ""
        Num = flask.request.values.get("Num") if "Num" in flask.request.values else ""
        res = db.updateRow(No, Name, Sex, Age, Favorite, Num)
    elif opt == "select":  # 查
        No = flask.request.values.get("No") if "No" in flask.request.values else ""
        res = db.selectRow(No)
    elif opt == "":
        res = db.returnALL()
    db.closeDB()
    return json.dumps(res)


if __name__ == "__main__":
    app.run()
