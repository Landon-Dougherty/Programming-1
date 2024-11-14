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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._label3 = System.Windows.Forms.Label()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label1.Location = System.Drawing.Point(63, 64)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(240, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter Calories in Food :"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label2.Location = System.Drawing.Point(96, 142)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(216, 23)
        self._label2.TabIndex = 1
        self._label2.Text = "Enter Grams of Fat :"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(349, 145)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 26)
        self._textBox1.TabIndex = 2
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(349, 64)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 26)
        self._textBox2.TabIndex = 3
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Goldenrod
        self._button1.Location = System.Drawing.Point(53, 304)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(111, 69)
        self._button1.TabIndex = 4
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label3.Location = System.Drawing.Point(119, 211)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(298, 31)
        self._label3.TabIndex = 5
        self._label3.Text = "% Of Calories From Fat :"
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Goldenrod
        self._button2.Location = System.Drawing.Point(225, 304)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(111, 69)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Goldenrod
        self._button3.Location = System.Drawing.Point(397, 304)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(111, 69)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Black
        self.ClientSize = System.Drawing.Size(587, 438)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog268"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button2Click(self, sender, e): #Clear
        pass

    def Button3Click(self, sender, e): #Exit
        Application.Exit()

    def Button1Click(self, sender, e):
        cal = float(self._textBox2.Text)
        fat = float(self._textBox1.Text)
        nfat = float(fat*9)
        per = float(nfat/cal) * 100.00
        self._label3.Text = "% Of Calories From Fat : " + str(per) + "%" 
        
        
        
        #PAGE119
        
