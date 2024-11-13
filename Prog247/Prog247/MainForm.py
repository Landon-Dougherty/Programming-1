import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._panel1 = System.Windows.Forms.Panel()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._checkBox3 = System.Windows.Forms.CheckBox()
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._panel1.SuspendLayout()
        self.SuspendLayout()
        # 
        # panel1
        # 
        self._panel1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._panel1.Controls.Add(self._checkBox3)
        self._panel1.Controls.Add(self._checkBox2)
        self._panel1.Controls.Add(self._checkBox1)
        self._panel1.Controls.Add(self._radioButton3)
        self._panel1.Controls.Add(self._radioButton2)
        self._panel1.Controls.Add(self._radioButton1)
        self._panel1.Location = System.Drawing.Point(51, 35)
        self._panel1.Name = "panel1"
        self._panel1.Size = System.Drawing.Size(462, 243)
        self._panel1.TabIndex = 1
        # 
        # radioButton1
        # 
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(16, 19)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(144, 39)
        self._radioButton1.TabIndex = 0
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Channel 1"
        self._radioButton1.UseVisualStyleBackColor = True
        # 
        # radioButton2
        # 
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(16, 96)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(144, 39)
        self._radioButton2.TabIndex = 1
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Channel 2"
        self._radioButton2.UseVisualStyleBackColor = True
        # 
        # radioButton3
        # 
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(16, 174)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(144, 39)
        self._radioButton3.TabIndex = 2
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Channel 3"
        self._radioButton3.UseVisualStyleBackColor = True
        # 
        # checkBox1
        # 
        self._checkBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox1.Location = System.Drawing.Point(252, 19)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Size = System.Drawing.Size(153, 39)
        self._checkBox1.TabIndex = 3
        self._checkBox1.Text = "Channel 4 "
        self._checkBox1.UseVisualStyleBackColor = True
        # 
        # checkBox2
        # 
        self._checkBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox2.Location = System.Drawing.Point(252, 97)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(153, 39)
        self._checkBox2.TabIndex = 4
        self._checkBox2.Text = "Channel 5"
        self._checkBox2.UseVisualStyleBackColor = True
        # 
        # checkBox3
        # 
        self._checkBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox3.Location = System.Drawing.Point(252, 174)
        self._checkBox3.Name = "checkBox3"
        self._checkBox3.Size = System.Drawing.Size(153, 39)
        self._checkBox3.TabIndex = 5
        self._checkBox3.Text = "Channel 6"
        self._checkBox3.UseVisualStyleBackColor = True
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label1.Location = System.Drawing.Point(122, 291)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(321, 31)
        self._label1.TabIndex = 2
        self._label1.Text = "You Checked"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(51, 365)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(197, 48)
        self._button1.TabIndex = 3
        self._button1.Text = "Okay"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(316, 365)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(197, 48)
        self._button2.TabIndex = 4
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self.ClientSize = System.Drawing.Size(583, 466)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._panel1)
        self.Name = "MainForm"
        self.Text = "Prog247"
        self._panel1.ResumeLayout(False)
        self.ResumeLayout(False)



        

    def Button1Click(self, sender, e):
        first = 0 
        second = 0 
        if self._radioButton1.Checked:
            first = " Channel 1 "
        elif self._radioButton2.Checked:
            first = " Channel 2 "
        else:
            first = " Channel 3 "
        if self._checkBox1.Checked:
            second = " Channel 4"
        elif self._checkBox2.Checked:
            second = " Channel 5"
        else:
            second = " Channel 6"
        self._label1.Text = "You Checked" + str(first) + "And" + str(second) + "!"

    def Button2Click(self, sender, e):
        Application.Exit()