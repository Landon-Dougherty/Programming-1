import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(58, 58)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(276, 45)
        self._label1.TabIndex = 0
        self._label1.Text = "Class A Seats Sold -->"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(58, 163)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(276, 45)
        self._label2.TabIndex = 1
        self._label2.Text = "Class B Seats Sold -->"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.White
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(58, 268)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(276, 45)
        self._label3.TabIndex = 2
        self._label3.Text = "Class C Seats Sold -->"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(58, 461)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(276, 45)
        self._label4.TabIndex = 3
        self._label4.Text = "Total Revenue Generated :"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.White
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(449, 461)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(276, 45)
        self._label5.TabIndex = 4
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(416, 58)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(322, 34)
        self._textBox1.TabIndex = 5
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(416, 174)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(322, 34)
        self._textBox2.TabIndex = 6
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(416, 279)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(322, 34)
        self._textBox3.TabIndex = 7
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._button1.Location = System.Drawing.Point(33, 548)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(108, 67)
        self._button1.TabIndex = 8
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._button2.Location = System.Drawing.Point(147, 548)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(108, 67)
        self._button2.TabIndex = 9
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._button3.Location = System.Drawing.Point(261, 548)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(108, 67)
        self._button3.TabIndex = 10
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self.ClientSize = System.Drawing.Size(863, 638)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog186"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button2Click(self, sender, e): #Exit
        Application.Exit()

    def Button1Click(self, sender, e): #Calc
        classa = float(self._textBox1.Text)
        if self._textBox1.Text == "":
            classa = 0
        classb = float(self._textBox2.Text)
        classc = float(self._textBox3.Text)
        self._label5.Text = str((classa*15) + (classb*12) + (classc*9))

    def Button3Click(self, sender, e): #Clear
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._label5.Text = ""