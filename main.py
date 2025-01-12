import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout, QFileDialog
from PyQt5.QtCore import Qt
from image_processor import ImageProcessor

app = QApplication([])
win = QWidget()
win.setWindowTitle("Easy Editor")
win.resize(700, 500)

app.setStyleSheet("""
    QWidget {
        background-color: black;
        color: red;
    }
    QLabel {
        font-size: 14px;
        color: red;
    }
    QPushButton {
        background-color: red;
        color: black;
        border: 2px solid red;
        border-radius: 5px;
    }
    QPushButton:hover {
        background-color: black;
        color: red;
        border: 2px solid red;
    }
    QListWidget {
        background-color: black;
        color: red;
        border: 1px solid red;
    }
    
    QListWidget::item:hover {
        background-color: gray;
        color: blue;
    }
    
""")

label_image = QLabel("Тут буде картинка")
label_image.setAlignment(Qt.AlignCenter)

btn_dir = QPushButton("Папка")
lw_files = QListWidget()
btn_left = QPushButton("Вліво")
btn_right = QPushButton("Вправо")
btn_flip = QPushButton("Дзеркало")
btn_updown = QPushButton("Перевернуть")

btn_blur = QPushButton("Размыть")
btn_find_edges = QPushButton("Найти грани")
btn_bw = QPushButton("Ч/Б")

btn_test = QPushButton("Жмых")
btn_test2 = QPushButton("Хымж")

row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
row_tools = QHBoxLayout()
row_tools_conv = QHBoxLayout()

col1.addWidget(btn_dir)
col1.addWidget(lw_files)

row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_updown)

row_tools_conv.addWidget(btn_bw)
row_tools_conv.addWidget(btn_blur)
row_tools_conv.addWidget(btn_find_edges)

row_tools_conv.addWidget(btn_test)
row_tools_conv.addWidget(btn_test2)

col2.addWidget(label_image)
col2.addLayout(row_tools)
col2.addLayout(row_tools_conv)

row.addLayout(col2, stretch=3)
row.addLayout(col1, stretch=1)
win.setLayout(row)
win.show()

work_dir = ""

def filter(files, extensions):
    result = []
    for file in files:
        for ext in extensions:
            if file.endswith(ext):
                result.append(file)
    return result

def chooseWorkDir():
    global work_dir
    work_dir = QFileDialog.getExistingDirectory()

def showFilenameList():
    extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
    chooseWorkDir()
    filenames = filter(os.listdir(work_dir), extensions)
    lw_files.clear()
    lw_files.addItems(filenames)

def showChosenImage():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(work_dir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path, label_image)

workimage = ImageProcessor()

lw_files.currentRowChanged.connect(showChosenImage)
btn_bw.clicked.connect(workimage.do_bw)
btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_right)
btn_flip.clicked.connect(workimage.do_flip)
btn_dir.clicked.connect(showFilenameList)
btn_updown.clicked.connect(workimage.upside_down)
btn_blur.clicked.connect(workimage.do_blur)
btn_find_edges.clicked.connect(workimage.find_edges)

btn_test.clicked.connect(workimage.do_func1)
btn_test2.clicked.connect(workimage.do_func2)

app.exec_()
