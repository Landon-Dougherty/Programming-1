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
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(2, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(649, 30)
        self._textBox1.TabIndex = 0
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(2, 69)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(649, 30)
        self._textBox2.TabIndex = 1
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(2, 128)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(649, 30)
        self._textBox3.TabIndex = 2
        # 
        # textBox4
        # 
        self._textBox4.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.Location = System.Drawing.Point(2, 188)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(649, 30)
        self._textBox4.TabIndex = 3
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Pixel, 0)
        self._label1.Location = System.Drawing.Point(655, 12)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(121, 205)
        self._label1.TabIndex = 4
        self._label1.Text = """Enter Numbers Here
<--"""
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Black
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ButtonFace
        self._label2.Location = System.Drawing.Point(2, 339)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(312, 58)
        self._label2.TabIndex = 5
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(128, 64, 64)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._button1.Location = System.Drawing.Point(2, 234)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(209, 92)
        self._button1.TabIndex = 6
        self._button1.Text = "Execute"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(128, 64, 64)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._button2.Location = System.Drawing.Point(222, 234)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(209, 92)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(128, 64, 64)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._button3.Location = System.Drawing.Point(442, 234)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(209, 92)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit Application"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Black
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ButtonFace
        self._label3.Location = System.Drawing.Point(337, 339)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(314, 58)
        self._label3.TabIndex = 9
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Transparent
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(111, 397)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(143, 28)
        self._label4.TabIndex = 10
        self._label4.Text = "Sum "
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Transparent
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(442, 397)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(143, 28)
        self._label5.TabIndex = 11
        self._label5.Text = "Average"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self.ClientSize = System.Drawing.Size(783, 434)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Prog54b"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        num1 = int(self._textBox1.Text)
        num2 = int(self._textBox2.Text)
        num3 = int(self._textBox3.Text)
        num4 = int(self._textBox4.Text)
        Sum  = num1 + num2 + num3 + num4
        Avg  = Sum // 4.0
        self._label2.Text = str(Sum)
        self._label3.Text = str(Avg)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._textBox4.Text = ""
        self._label2.Text   = ""
        self._label3.Text   = ""

    def Button3Click(self, sender, e):
        Application.Exit()