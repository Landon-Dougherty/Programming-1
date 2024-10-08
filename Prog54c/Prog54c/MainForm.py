﻿import System.Drawing
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
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.SystemColors.InactiveCaption
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(275, 112)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(213, 38)
        self._textBox1.TabIndex = 0
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(317, 47)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(123, 37)
        self._label1.TabIndex = 1
        self._label1.Text = "Enter Radius Here"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 35, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(43, 60)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(226, 150)
        self._label2.TabIndex = 2
        self._label2.Text = "--->"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 35, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(494, 60)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(226, 150)
        self._label3.TabIndex = 3
        self._label3.Text = "<---"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(300, 153)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(157, 67)
        self._label4.TabIndex = 4
        self._label4.Text = """|
|
\\/
"""
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(143, 233)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(143, 109)
        self._label5.TabIndex = 5
        self._label5.Text = "A = "
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.InactiveCaption
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(11, 233)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(117, 109)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.InactiveCaption
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(632, 233)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(122, 109)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(300, 356)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(156, 81)
        self._button3.TabIndex = 8
        self._button3.Text = "Quit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(303, 233)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(154, 109)
        self._label6.TabIndex = 9
        self._label6.Text = "C ="
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(472, 233)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(154, 109)
        self._label7.TabIndex = 10
        self._label7.Text = "R ="
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(766, 449)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Prog54c"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button3Click(self, sender, e):
        Application.Exit()

    def Button1Click(self, sender, e):
        radius = float(self._textBox1.Text)
        P = 3.14159
        area = round(P * radius**2,3)
        circum = 2 * P * radius
        self._label5.Text = str(area)
        self._label6.Text = str(circum)
        self._label7.Text = str(radius)

    def Button2Click(self, sender, e):
        self._label5.Text = "A ="
        self._label6.Text = "C ="
        self._label7.Text = "R ="
        self._textBox1.Text = "" 

