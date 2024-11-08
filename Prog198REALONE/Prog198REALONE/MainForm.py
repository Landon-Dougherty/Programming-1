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
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(198, 52)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(183, 30)
        self._textBox1.TabIndex = 0
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(198, 139)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(183, 30)
        self._textBox2.TabIndex = 1
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(198, 222)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(183, 30)
        self._textBox3.TabIndex = 2
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(28, 52)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(123, 30)
        self._label1.TabIndex = 3
        self._label1.Text = "Score 1 :"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(28, 225)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(123, 30)
        self._label2.TabIndex = 4
        self._label2.Text = "Score 3 :"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(28, 142)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(123, 30)
        self._label3.TabIndex = 4
        self._label3.Text = "Score 2 :"
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(73, 298)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(278, 39)
        self._label4.TabIndex = 5
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label4.VisibleChanged += self.MainFormLoad
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(98, 347)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(219, 30)
        self._label5.TabIndex = 6
        self._label5.Text = "Avg Score :"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._button1.Location = System.Drawing.Point(37, 399)
        self._button1.Name = "button1"
        self._button1.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._button1.Size = System.Drawing.Size(75, 57)
        self._button1.TabIndex = 7
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._button2.Location = System.Drawing.Point(166, 399)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(75, 57)
        self._button2.TabIndex = 8
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._button3.Location = System.Drawing.Point(306, 399)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(75, 57)
        self._button3.TabIndex = 9
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self.ClientSize = System.Drawing.Size(475, 468)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Prog198REALONE"
        self.ResumeLayout(False)
        self.PerformLayout()


    def MainFormLoad(self, sender, e):
        pass



    def Button2Click(self, sender, e):
        Application.Exit() #Exit
        

    def Button3Click(self, sender, e): #Clear
        self._label4.Text = ""
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._label5.Text = "Avg Score :"

    def Button1Click(self, sender, e):
        one = round(float(self._textBox1.Text),2)
        two = round(float(self._textBox2.Text),2)
        thr = round(float(self._textBox3.Text),2)
        avg = round(((one+two+thr) / 3.0),2)
        self._label5.Text = "Avg Score : " + str(avg)
        if avg >= 95.0:
            self._label4.Text = "Congratulations!"
        else:
            self._label4.Text = ""