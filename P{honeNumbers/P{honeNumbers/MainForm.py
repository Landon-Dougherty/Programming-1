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
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.FromArgb(192, 192, 0)
        self._label1.Location = System.Drawing.Point(10, 8)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(756, 273)
        self._label1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(192, 192, 0)
        self._button1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center
        self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(10, 311)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(225, 117)
        self._button1.TabIndex = 1
        self._button1.Text = "Reveal Numbers"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(192, 192, 0)
        self._button2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center
        self._button2.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(271, 311)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(225, 117)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear Numbers"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(192, 192, 0)
        self._button3.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center
        self._button3.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(529, 311)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(225, 117)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit Application"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(19, 34)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(734, 22)
        self._label2.TabIndex = 4
        self._label2.Click += self.Label2Click
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(21, 239)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(734, 22)
        self._label3.TabIndex = 5
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(19, 139)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(734, 22)
        self._label4.TabIndex = 6
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(21, 85)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(734, 22)
        self._label5.TabIndex = 7
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(21, 190)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(734, 22)
        self._label6.TabIndex = 8
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(776, 440)
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
        self.Text = "P{honeNumbers"
        self.ResumeLayout(False)



    def Button1Click(self, sender, e):
        self._label2.Text = "Italian House - (608) 754-2226"
        self._label5.Text = "Tucson Airport - (520) 573-8100"
        self._label4.Text = "Subway -  (608) 758-9410"
        self._label6.Text = "Mercy North - (608) 314-3605"
        self._label3.Text = "McDonalds - (608) 752-7521"

    def Button2Click(self, sender, e):
        self._label2.Text = ""
        self._label5.Text = ""
        self._label4.Text = ""
        self._label6.Text = ""
        self._label3.Text = ""
        

    def Button3Click(self, sender, e):
        Application.Exit()

    def Label2Click(self, sender, e):
        pass