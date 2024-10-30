import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label3 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(25, 61)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(279, 26)
        self._textBox1.TabIndex = 0
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(26, 18)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(278, 40)
        self._label1.TabIndex = 1
        self._label1.Text = "Enter Seat Amount"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(26, 496)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(278, 40)
        self._label2.TabIndex = 3
        self._label2.Text = "Enter Amount Of People"
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(25, 539)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(279, 26)
        self._textBox2.TabIndex = 2
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(25, 119)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(279, 96)
        self._button1.TabIndex = 4
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(25, 382)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(279, 96)
        self._button2.TabIndex = 5
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(26, 250)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(279, 96)
        self._button3.TabIndex = 6
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(348, 123)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(482, 354)
        self._label3.TabIndex = 7
        self._label3.Text = "Total # Of Possible Arrangements :"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self.ClientSize = System.Drawing.Size(869, 621)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Prog162h"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button3Click(self, sender, e): #Exit Appl.
        Application.Exit()

    def Button1Click(self, sender, e):
        seats = int(self._textBox1.Text)
        fact = int(self._textBox2.Text)
        n = seats
        r = fact
        first = math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
        second = math.factorial(n)/(math.factorial(n-r))
        self._label3.Text = "Total # of Possible Arrangements: " + str(second) + "\nPeople Standing: " + str(abs(fact-seats))
        
            

    def Button2Click(self, sender, e): #Clear
        self._textBox1.Text = "" 
        self._textBox2.Text = ""
        self._label3.Text = ""