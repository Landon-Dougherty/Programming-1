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
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(21, 14)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(161, 40)
        self._textBox1.TabIndex = 0
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(21, 182)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(161, 40)
        self._textBox2.TabIndex = 1
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(21, 363)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(161, 40)
        self._textBox3.TabIndex = 2
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(188, 8)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(181, 56)
        self._label1.TabIndex = 3
        self._label1.Text = "<-- Input A"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(188, 176)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(181, 56)
        self._label2.TabIndex = 4
        self._label2.Text = "<-- Input B"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(188, 357)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(181, 56)
        self._label3.TabIndex = 5
        self._label3.Text = "<-- Input C"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(328, 18)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(95, 406)
        self._label4.TabIndex = 6
        self._label4.Text = """|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|"""
        self._label4.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(387, 181)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(192, 47)
        self._label5.TabIndex = 7
        self._label5.Text = "----->"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(406, 252)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(341, 151)
        self._label6.TabIndex = 8
        self._label6.Text = "Ax^2 + Bx + C = 0"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(406, 9)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(341, 151)
        self._label7.TabIndex = 9
        self._label7.Text = "Ax^2 + Bx + C = 0"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(486, 184)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(261, 44)
        self._label8.TabIndex = 10
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveBorder
        self.ClientSize = System.Drawing.Size(771, 439)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Prog58b"
        self.ResumeLayout(False)
        self.PerformLayout()

