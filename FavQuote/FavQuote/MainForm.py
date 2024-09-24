import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.LightSalmon
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label1.Cursor = System.Windows.Forms.Cursors.AppStarting
        self._label1.Font = System.Drawing.Font("Monotype Corsiva", 30, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Cornsilk
        self._label1.Location = System.Drawing.Point(128, 56)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(482, 252)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft JhengHei Light", 27, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(10, 56)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(112, 252)
        self._button1.TabIndex = 1
        self._button1.Text = "Clear "
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft JhengHei UI Light", 30, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(128, 311)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(482, 98)
        self._button2.TabIndex = 2
        self._button2.Text = "Quote "
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft JhengHei UI Light", 36, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(616, 56)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(112, 252)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(747, 421)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "FavQuote"
        self.ResumeLayout(False)


    def Button2Click(self, sender, e):
        #Display Text
        self._label1.Text = "Behind Every Great Man Is A Woman Rolling Her Eyes - Jim Carrey"

    def Button1Click(self, sender, e):
        #Clear
        self._label1.Text = ""

    def Button3Click(self, sender, e):
        #Exit Application
        Application.Exit()