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
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self._label1.Location = System.Drawing.Point(7, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(629, 419)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(655, 15)
        self._button1.Name = "button1"
        self._button1.RightToLeft = System.Windows.Forms.RightToLeft.Yes
        self._button1.Size = System.Drawing.Size(103, 83)
        self._button1.TabIndex = 1
        self._button1.Text = "Clear"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(655, 337)
        self._button2.Name = "button2"
        self._button2.RightToLeft = System.Windows.Forms.RightToLeft.Yes
        self._button2.Size = System.Drawing.Size(103, 83)
        self._button2.TabIndex = 2
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(655, 125)
        self._button3.Name = "button3"
        self._button3.RightToLeft = System.Windows.Forms.RightToLeft.Yes
        self._button3.Size = System.Drawing.Size(103, 183)
        self._button3.TabIndex = 3
        self._button3.Text = """S
C
H
E
D
U
L
E
"""
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Transparent
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(7, 40)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(594, 25)
        self._label2.TabIndex = 4
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(7, 185)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(594, 25)
        self._label3.TabIndex = 5
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(7, 234)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(594, 25)
        self._label4.TabIndex = 6
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(7, 283)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(594, 25)
        self._label5.TabIndex = 7
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(7, 337)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(594, 25)
        self._label6.TabIndex = 8
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(7, 138)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(594, 25)
        self._label7.TabIndex = 9
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label8
        # 
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(7, 385)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(594, 25)
        self._label8.TabIndex = 10
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label9
        # 
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(7, 89)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(594, 25)
        self._label9.TabIndex = 11
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(779, 441)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Schedule"
        self.ResumeLayout(False)


    def Button3Click(self, sender, e):
        self._label2.Text = "1st Hour - Spanish I"
        self._label9.Text = "2nd Hour - Computer Programming I"
        self._label7.Text = "3rd Hour - Symphonic Band"
        self._label3.Text = "4th Hour - 10,11,12 PE"
        self._label4.Text = "5th Hour - English 10 Honors"
        self._label5.Text = "6th Hour - Algebra II Honors"
        self._label6.Text = "7th Hour - Chemistry Honors"
        self._label8.Text = "AP US History"

    def Button1Click(self, sender, e):
        self._label2.Text = ""
        self._label9.Text = ""
        self._label7.Text = ""
        self._label3.Text = ""
        self._label4.Text = ""
        self._label5.Text = ""
        self._label6.Text = ""
        self._label8.Text = ""

    def Button2Click(self, sender, e):
        Application.Exit()