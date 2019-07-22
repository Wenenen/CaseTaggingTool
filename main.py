import form
import sys
import os
import json
import pickle
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt


class mywindow(QtWidgets.QMainWindow, form.Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

        self.file_path = None
        self.save_file_name = None
        self.save_json_name = None
        self.numToLabel = ["正确","相关","错误","未标记"]
        self.is_save = True

        self.no = 1
        self.soso = 2
        self.yes = 3

        self.jsonDict=None
        self.curQueryKey = 1
        self.curAnsQueryIndex = 0
        self.curDocumentKey = 1
        self.curAnsDocumentIndex = 0

        self.ansList=list()

        self.viewpoint.setReadOnly(True)
        self.content.setReadOnly(True)


        QShortcut(QKeySequence(Qt.Key_1), self, self.set_yes)
        QShortcut(QKeySequence(Qt.Key_2), self, self.set_soso)
        QShortcut(QKeySequence(Qt.Key_3), self, self.set_no)
        QShortcut(QKeySequence(Qt.Key_U), self, self.last_case)
        QShortcut(QKeySequence(Qt.Key_S), self, self.save)

    def set_yes(self):
        if (self.file_path == None ):
            return
        self.ansList[self.curAnsQueryIndex][self.curAnsDocumentIndex]=1
        self.nextOne()
        self.show_info()

    def set_soso(self):
        if (self.file_path == None ):
            return
        self.ansList[self.curAnsQueryIndex][self.curAnsDocumentIndex]=2
        self.nextOne()
        self.show_info()

    def set_no(self):
        if (self.file_path == None ):
            return
        self.ansList[self.curAnsQueryIndex][self.curAnsDocumentIndex]=3
        self.nextOne()
        self.show_info()

    def nextOne(self):
        if(self.file_path == None ):
            return
        if(self.curDocumentKey<self.documentsSize):
            self.curAnsDocumentIndex+=1
            self.curDocumentKey+=1
        elif(self.curQueryKey<self.querySize):
            self.curAnsDocumentIndex = 0
            self.curDocumentKey = 1
            self.curAnsQueryIndex+=1
            self.curQueryKey+=1
        else:
            msg_box = QMessageBox(QMessageBox.Information, "消息提醒", "数据标完了，快去保存鸭。")
            msg_box.exec_()
        print(self.curQueryKey,self.querySize)

    def save(self):
        if (self.file_path == None ):
            return

        for qIdx in range(len(self.ansList)):
            for dIdx in range(len(self.ansList[qIdx])):
                self.jsonDict[str(qIdx+1)]["documents"][str(dIdx+1)]["Label"]=self.numToLabel[self.ansList[qIdx][dIdx]-1]
        with open(self.save_json_name, 'w', encoding='utf-8') as json_file:
            json.dump(self.jsonDict, json_file, ensure_ascii=False, indent=4)


        f = open(self.save_file_name, 'wb')
        pickle.dump(self.ansList, f)
        f.close()

        msg_box = QMessageBox(QMessageBox.Information, "消息提醒", "保存成功")
        msg_box.exec_()

        #clear variables related to the last file
        self.file_path = None
        self.curAnsQueryIndex = 0
        self.curQueryKey = 1
        self.curAnsDocumentIndex = 0
        self.curDocumentKey = 1
        self.save_file_name = None
        self.is_save = True
        self.jsonDict = None
        self.ansList.clear()

    def show_info(self):
        currentQueryDict = self.jsonDict[str(self.curQueryKey)]
        currentDocumentDict = currentQueryDict["documents"][str(self.curDocumentKey)]

        #show query text
        self.current_query.setText(currentQueryDict["query"])

        #show content text
        self.case_title.setText(currentDocumentDict["Title"])
        self.content.setText(currentDocumentDict["Content"])
        self.viewpoint.setText(currentDocumentDict["CourtViewPoint"])
        self.case_cause.setText(currentDocumentDict["Cause"])
        currentIndexText = "问题索引:"+str(self.curQueryKey)+"/"+str(len(self.jsonDict))+"\n案例索引:"+str(self.curDocumentKey)+"/"+str(len(currentQueryDict["documents"]))

        self.current_index.setText(currentIndexText)
        if(self.curDocumentKey > 1):
            lastCaseViewText = "标题为："+currentQueryDict["documents"][str(self.curDocumentKey-1)]["Title"] + "\n案由为："+currentQueryDict["documents"][str(self.curDocumentKey-1)]["Cause"]+ \
                                            "\n被标记为："+self.numToLabel[self.ansList[self.curAnsQueryIndex][self.curAnsDocumentIndex-1]-1]
            self.last_case_view.setText(lastCaseViewText)
        else:
            self.last_case_view.clear()

    def last_query(self):
        if (self.file_path == None):
            return
        if (self.curQueryKey > 1):
            self.curQueryKey -= 1
            self.curAnsQueryIndex -= 1
            self.show_info()
        else:
            msg_box = QMessageBox(QMessageBox.Information, "消息提醒", "已是第一个问题")
            msg_box.exec_()

    def last_case(self):
        if (self.file_path == None):
            return
        if(self.curDocumentKey>1):
            self.curDocumentKey-=1
            self.curAnsDocumentIndex -= 1
            self.show_info()
        else:
            msg_box = QMessageBox(QMessageBox.Information, "消息提醒", "已是第一个案件")
            msg_box.exec_()

    def select_file(self):
        if self.is_save is False:
            reply = QtWidgets.QMessageBox.question(self, '警告', '还未保存，确定重新选文件？',
                                                   QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                pass
            else:
                return

        #read new file

        self.file_path = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd())
        if not os.path.exists(self.file_path[0]):  # 如果有这个文件
            msg_box = QMessageBox(QMessageBox.Information, "消息提醒", "好像没选数据文件噢。")
            msg_box.exec_()
            return
        if (self.file_path[0].split('.')[1] != "json"):
            msg_box = QMessageBox(QMessageBox.Information, "消息提醒", "只能选择json文件。")
            msg_box.exec_()
            return

        self.save_json_name = self.file_path[0].split('.')[0] + "_label.json"
        self.save_file_name = self.file_path[0].split('.')[0] + "_ansList"
        with open(self.file_path[0], "r", encoding='utf-8') as load_f:
            self.jsonDict = json.load(load_f)

        #init the size of "self.ansList"
        self.querySize = len(self.jsonDict)
        self.documentsSize = len(self.jsonDict["1"]["documents"])

        #if the ansList file is already exists, load it
        if (os.path.exists(self.save_file_name)):
            msg_box = QMessageBox(QMessageBox.Information, "消息提醒", "检测到该文件标注过，已载入最新进度。")
            msg_box.exec_()
            f = open(self.save_file_name, 'rb')
            self.ansList = pickle.load(f)
            f.close()

            # reset the index last time
            qIdx = len(self.ansList)-1
            dIdx = 0
            while (qIdx >= 0 and self.ansList[qIdx][0] == 0):
                qIdx -= 1
            while (dIdx < len(self.ansList[0])-1 and self.ansList[qIdx][dIdx] != 0):
                dIdx += 1
            self.curAnsQueryIndex = qIdx
            self.curQueryKey = qIdx + 1
            self.curAnsDocumentIndex = dIdx
            self.curDocumentKey = dIdx + 1
        else:
            self.ansList = [[0]*self.documentsSize for i in range(self.querySize)]
        self.is_save = False
        self.show_info()

    def closeEvent(self, event):
        if self.is_save:
            return
        reply = QtWidgets.QMessageBox.question(self, '警告', '还未保存，确定退出？',
                                               QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())
