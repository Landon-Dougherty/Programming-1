import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(246, 124)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(12, 484)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(246, 124)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(12, 250)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(246, 124)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(382, 69)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(362, 34)
        self._textBox1.TabIndex = 4
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(382, 26)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(362, 40)
        self._label2.TabIndex = 5
        self._label2.Text = "Enter Number To Factorial"
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(382, 295)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(362, 40)
        self._label1.TabIndex = 6
        self._label1.Text = "Factorial:"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self.ClientSize = System.Drawing.Size(843, 620)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog162a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        One = int(self._textBox1.Text)
        Last = 1
        for num in range (1,One+1):
            Last *= num
        self._label1.Text = "Factorial: " + str(Last)
        
            

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._label1.Text = "Factorial: "
        self._textBox1.Text = ""
        
