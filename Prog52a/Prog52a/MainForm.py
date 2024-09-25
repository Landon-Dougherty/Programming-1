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
        self._label6 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(73, 27)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(180, 51)
        self._label1.TabIndex = 0
        self._label1.Text = "Length:"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(73, 78)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(180, 51)
        self._label2.TabIndex = 1
        self._label2.Text = "Width:"
        
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(29, 205)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(252, 51)
        self._label3.TabIndex = 2
        self._label3.Text = "Area:"
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(29, 256)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(258, 51)
        self._label4.TabIndex = 3
        self._label4.Text = "Perimeter:"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.MediumSlateBlue
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.SystemColors.Control
        self._label5.Location = System.Drawing.Point(281, 205)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(260, 51)
        self._label5.TabIndex = 4
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.MediumSlateBlue
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.SystemColors.Control
        self._label6.Location = System.Drawing.Point(281, 266)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(260, 51)
        self._label6.TabIndex = 5
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.DimGray
        self._button1.FlatAppearance.BorderSize = 6
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.Control
        self._button1.Location = System.Drawing.Point(23, 336)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(175, 81)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.DimGray
        self._button2.FlatAppearance.BorderSize = 6
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.Control
        self._button2.Location = System.Drawing.Point(226, 336)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(175, 81)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DimGray
        self._button3.FlatAppearance.BorderSize = 6
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.Control
        self._button3.Location = System.Drawing.Point(440, 336)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(175, 81)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(281, 30)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(260, 30)
        self._textBox1.TabIndex = 9
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(281, 81)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(260, 30)
        self._textBox2.TabIndex = 10
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self.ClientSize = System.Drawing.Size(661, 433)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog52a"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()



    def Button1Click(self, sender, e):
        length = int(self._textBox1.Text)
        width = int(self._textBox2.Text)
        area = length * width 
        perim = 2 * length + 2 * width 
        self._label5.Text = str(area)
        self._label6.Text = str(perim)
        # + - * / %     ** pow     // diivde & round down 
        # int (Integer): a whole number positive or negative
        # float (Floating-Point Number): any number with a decimal 
        # st (String): a string of tex

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label5.Text = ""
        self._label6.Text = ""

    def Button3Click(self, sender, e):
        Applicaton.Exit()

    def MainFormLoad(self, sender, e):
        pass