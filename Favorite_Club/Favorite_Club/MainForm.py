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
        self._label1.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label1.Cursor = System.Windows.Forms.Cursors.Default
        self._label1.Font = System.Drawing.Font("Microsoft YaHei", 45, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label1.Location = System.Drawing.Point(12, 15)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(425, 403)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label1.UseMnemonic = False
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
        self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Pixel, 0)
        self._button1.Location = System.Drawing.Point(482, 15)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(270, 110)
        self._button1.TabIndex = 1
        self._button1.Text = "Favorite Sport"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
        self._button2.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Pixel, 0)
        self._button2.Location = System.Drawing.Point(482, 308)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(270, 110)
        self._button2.TabIndex = 2
        self._button2.Text = "Close Application"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
        self._button3.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Pixel, 0)
        self._button3.Location = System.Drawing.Point(482, 159)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(270, 110)
        self._button3.TabIndex = 3
        self._button3.Text = "Clear Out"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(763, 438)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None
        self.Name = "MainForm"
        self.Text = "Favorite_Club"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "My Favorite Sport Is Track and Field"

    def Button3Click(self, sender, e):
        self._label1.Text = ""

    def Button2Click(self, sender, e):
        Application.Exit()