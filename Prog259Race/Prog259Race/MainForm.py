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
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._textBox5 = System.Windows.Forms.TextBox()
        self._textBox6 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._panel1 = System.Windows.Forms.Panel()
        self._label8 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self._label15 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._panel1.SuspendLayout()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(84, 113)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(107, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "Runner 1:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label2.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(84, 178)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(107, 23)
        self._label2.TabIndex = 1
        self._label2.Text = "Runner 2:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label3.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(84, 241)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(107, 23)
        self._label3.TabIndex = 2
        self._label3.Text = "Runner 3:"
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(230, 116)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(121, 20)
        self._textBox1.TabIndex = 3
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(230, 180)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(121, 20)
        self._textBox2.TabIndex = 4
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(230, 244)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(121, 20)
        self._textBox3.TabIndex = 5
        # 
        # textBox4
        # 
        self._textBox4.Location = System.Drawing.Point(535, 244)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(121, 20)
        self._textBox4.TabIndex = 8
        # 
        # textBox5
        # 
        self._textBox5.Location = System.Drawing.Point(535, 180)
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(121, 20)
        self._textBox5.TabIndex = 7
        # 
        # textBox6
        # 
        self._textBox6.Location = System.Drawing.Point(535, 116)
        self._textBox6.Name = "textBox6"
        self._textBox6.Size = System.Drawing.Size(121, 20)
        self._textBox6.TabIndex = 6
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label4.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(388, 244)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(107, 23)
        self._label4.TabIndex = 11
        self._label4.Text = "Seconds"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label5.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(388, 181)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(107, 23)
        self._label5.TabIndex = 10
        self._label5.Text = "Seconds"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label6.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(388, 116)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(107, 23)
        self._label6.TabIndex = 9
        self._label6.Text = "Seconds"
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._label7.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(180, 42)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(381, 37)
        self._label7.TabIndex = 12
        self._label7.Text = "Enter Your Runners and The Times That They Ran"
        # 
        # panel1
        # 
        self._panel1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center
        self._panel1.Controls.Add(self._label15)
        self._panel1.Controls.Add(self._label14)
        self._panel1.Controls.Add(self._label13)
        self._panel1.Controls.Add(self._label12)
        self._panel1.Controls.Add(self._label11)
        self._panel1.Controls.Add(self._label9)
        self._panel1.Controls.Add(self._label10)
        self._panel1.Controls.Add(self._label8)
        self._panel1.Location = System.Drawing.Point(84, 332)
        self._panel1.Name = "panel1"
        self._panel1.Size = System.Drawing.Size(572, 171)
        self._panel1.TabIndex = 13
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label8.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(3, 0)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(107, 23)
        self._label8.TabIndex = 14
        self._label8.Text = "Results"
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label10.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(65, -99)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(107, 23)
        self._label10.TabIndex = 18
        self._label10.Text = "Results"
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label9.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(74, 44)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(107, 23)
        self._label9.TabIndex = 19
        self._label9.Text = "First Place:"
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label11.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 11, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(74, 82)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(107, 23)
        self._label11.TabIndex = 20
        self._label11.Text = "Second Place:"
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label12.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(74, 120)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(107, 23)
        self._label12.TabIndex = 21
        self._label12.Text = "Third Place:"
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label13.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.Location = System.Drawing.Point(209, 44)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(147, 23)
        self._label13.TabIndex = 22
        # 
        # label14
        # 
        self._label14.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label14.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._label14.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label14.Location = System.Drawing.Point(209, 81)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(147, 23)
        self._label14.TabIndex = 23
        # 
        # label15
        # 
        self._label15.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label15.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._label15.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label15.Location = System.Drawing.Point(209, 120)
        self._label15.Name = "label15"
        self._label15.Size = System.Drawing.Size(147, 23)
        self._label15.TabIndex = 24
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._button1.ForeColor = System.Drawing.Color.Coral
        self._button1.Location = System.Drawing.Point(178, 530)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(74, 58)
        self._button1.TabIndex = 14
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._button2.ForeColor = System.Drawing.Color.Coral
        self._button2.Location = System.Drawing.Point(338, 530)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(74, 58)
        self._button2.TabIndex = 15
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._button3.ForeColor = System.Drawing.Color.Coral
        self._button3.Location = System.Drawing.Point(487, 530)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(74, 58)
        self._button3.TabIndex = 16
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = False
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self.ClientSize = System.Drawing.Size(777, 600)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._panel1)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox5)
        self.Controls.Add(self._textBox6)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog259Race"
        self._panel1.ResumeLayout(False)
        self.ResumeLayout(False)
        self.PerformLayout()

    def Button1Click(self, sender, e):
        n1 = str(self._textBox1.Text)
        s1 = int(self._textBox6.Text)
        n2 = str(self._textBox2.Text)
        s2 = int(self._textBox5.Text)
        n3 = str(self._textBox3.Text)
        s3 = int(self._textBox4.Text)
        
        lst = [s1,s2,s3]
        lst.sort()
        first = lst[0]
        second = lst[1]
        third = lst[2]
        
        if lst[0] == s1:
            first = n1
        elif lst[0] == s2:
            first = n2
        elif lst[0] == s3:
            first = n3
        if lst[1] == s1:
            second = n1
        elif lst[1] == s2:
            second = n2
        elif lst[1] == s3:
            second = n3
        if lst[2] == s1:
            third = n1
        elif lst[2] == s2:
            third = n2
        elif lst[2] == s3:
            third = n3
        else:
            return
        
        
        self._label13.Text = str(first)
        self._label14.Text = str(second)
        self._label15.Text = str(third)
        