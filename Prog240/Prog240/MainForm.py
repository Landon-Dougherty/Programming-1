import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(278, 53)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(214, 30)
        self._textBox1.TabIndex = 0
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(278, 106)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(214, 30)
        self._textBox2.TabIndex = 1
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(43, 53)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(209, 30)
        self._label1.TabIndex = 5
        self._label1.Text = "Sales :"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(43, 106)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(209, 30)
        self._label2.TabIndex = 6
        self._label2.Text = "Adv Pay :"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(43, 270)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(209, 30)
        self._label3.TabIndex = 7
        self._label3.Text = "Commission Rate :"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(43, 328)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(209, 30)
        self._label4.TabIndex = 8
        self._label4.Text = "Commission :"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(43, 390)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(209, 30)
        self._label5.TabIndex = 9
        self._label5.Text = "Net Pay :"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(278, 390)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(209, 30)
        self._label6.TabIndex = 12
        self._label6.Text = " "
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(278, 328)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(209, 30)
        self._label7.TabIndex = 11
        self._label7.Text = " "
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(278, 270)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(209, 30)
        self._label8.TabIndex = 10
        self._label8.Text = " "
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._button1.Location = System.Drawing.Point(43, 515)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(108, 35)
        self._button1.TabIndex = 13
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._button2.Location = System.Drawing.Point(232, 515)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(108, 35)
        self._button2.TabIndex = 14
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._button3.Location = System.Drawing.Point(419, 515)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(108, 35)
        self._button3.TabIndex = 15
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self.ClientSize = System.Drawing.Size(599, 601)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Prog198REALONE"
        self.ResumeLayout(False)
        self.PerformLayout()



    def Button2Click(self, sender, e): #Exit
        Application.Exit()

    def Button1Click(self, sender, e): #Calc
        sale = float(self._textBox1.Text)
        apay = float(self._textBox2.Text)
        if sale < 10000:
            comrate = 0.05
        elif sale >= 10000 and sale < 15000:
            comrate = 0.10
        elif sale >= 15000 and sale <18000:
            comrate = 0.12
        elif sale >= 18000 and sale < 22000:
            comrate = 0.14
        elif sale >= 20000:
            comrate = 0.16
        else: 
            pass                                    
        

    def Button3Click(self, sender, e): #Clear
        pass