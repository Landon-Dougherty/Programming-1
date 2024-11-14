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
        self._label2.Click += self.Label2Click
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
        self._label3.Click += self.Label3Click
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
        self._label4.Text = "Runner 3:"
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
        self._label5.Text = "Runner 2:"
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
        self._label6.Text = "Runner 1:"
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
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self.ClientSize = System.Drawing.Size(777, 600)
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
        self.ResumeLayout(False)
        self.PerformLayout()
