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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.LightYellow
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(51, 75)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(297, 46)
        self._label1.TabIndex = 0
        self._label1.Text = "Annual Salary --->"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.LightYellow
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(51, 241)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(297, 46)
        self._label2.TabIndex = 1
        self._label2.Text = """Pay Periods Per Year --->

"""
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.LightYellow
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(51, 411)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(297, 46)
        self._label3.TabIndex = 2
        self._label3.Text = "Salary Per Pay Period --->"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(402, 81)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(353, 34)
        self._textBox1.TabIndex = 3
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(402, 247)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(353, 34)
        self._textBox2.TabIndex = 4
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(402, 411)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(353, 46)
        self._label4.TabIndex = 5
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._button1.Location = System.Drawing.Point(254, 516)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(94, 60)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._button2.Location = System.Drawing.Point(463, 516)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(94, 60)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._button3.Location = System.Drawing.Point(359, 516)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(94, 60)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Plum
        self.ClientSize = System.Drawing.Size(858, 629)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog153SalaryCalc"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button3Click(self, sender, e): #Exit
        Application.Exit()

    def Button1Click(self, sender, e): #Calculate
        num1 = float(self._textBox1.Text) 
        num2 = float(self._textBox2.Text) 
        total = float(num1/num2)
        self._label4.Text = str(total)
        

    def Button2Click(self, sender, e): #Clear
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label4.Text = ""