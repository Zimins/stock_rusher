# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
import logging.handlers
import time
from pymongo import MongoClient
from pandas import DataFrame

if __name__ == "__main__":
    # 현재 어플리케이션에서는 GUI 가 필요하지는 않지만 몇가지 메소드들을 프로그램이 종료되기 이전에 실행해야 하므로 임의로 켜놓기만 한다.
    # 앞으로 GUI를 추가 할 예정이기도 하고 지금은 간편해보여서 유지
    app = QApplication(sys.argv)
    # apiConnector = ApiConnector()
    # apiConnector.initialize()
    client = MongoClient('127.0.0.1', 27017)
    db = client.test_db
    print(type(db))
    test_collection = db.test_collection
    print(type(test_collection))

    posts = []
    for i in range(1000000):
        post = {
            "index": i,
            "name": "zimin",
            "article": "external",
            "tags": "fun"
        }
        posts.append(post)

    print("목록이 완성되었습니다.")

    test_collection.insert_many(posts)

    print(test_collection.count_documents({}))

    # 실행을 유지하는 코드가 있어 apiconnector 의 실행이 보장된다.
    app.exec_()
