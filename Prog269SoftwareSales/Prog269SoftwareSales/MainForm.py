import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._panel1 = System.Windows.Forms.Panel()
        self._panel2 = System.Windows.Forms.Panel()
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._panel1.SuspendLayout()
        self._panel2.SuspendLayout()
        self.SuspendLayout()
        # 
        # panel1
        # 
        self._panel1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._panel1.Controls.Add(self._label4)
        self._panel1.Controls.Add(self._label3)
        self._panel1.Controls.Add(self._label2)
        self._panel1.Controls.Add(self._textBox3)
        self._panel1.Controls.Add(self._textBox2)
        self._panel1.Controls.Add(self._textBox1)
        self._panel1.Controls.Add(self._label1)
        self._panel1.Location = System.Drawing.Point(134, 23)
        self._panel1.Name = "panel1"
        self._panel1.Size = System.Drawing.Size(385, 214)
        self._panel1.TabIndex = 0
        # 
        # panel2
        # 
        self._panel2.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._panel2.Controls.Add(self._label9)
        self._panel2.Controls.Add(self._label8)
        self._panel2.Controls.Add(self._label7)
        self._panel2.Controls.Add(self._label6)
        self._panel2.Controls.Add(self._label5)
        self._panel2.Location = System.Drawing.Point(28, 261)
        self._panel2.Name = "panel2"
        self._panel2.Size = System.Drawing.Size(432, 158)
        self._panel2.TabIndex = 1
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label1.Font = System.Drawing.Font("Microsoft Tai Le", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(17, 11)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(189, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter Packages To Buy"
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(216, 59)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 20)
        self._textBox1.TabIndex = 1
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(216, 100)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 20)
        self._textBox2.TabIndex = 2
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(216, 141)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(100, 20)
        self._textBox3.TabIndex = 3
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label2.Font = System.Drawing.Font("Microsoft Tai Le", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(100, 56)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(97, 23)
        self._label2.TabIndex = 4
        self._label2.Text = "Package A:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label3.Font = System.Drawing.Font("Microsoft Tai Le", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(98, 100)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(99, 23)
        self._label3.TabIndex = 5
        self._label3.Text = "Package B:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label4.Font = System.Drawing.Font("Microsoft Tai Le", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(98, 139)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(97, 23)
        self._label4.TabIndex = 6
        self._label4.Text = "Package C:"
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._button1.Location = System.Drawing.Point(28, 22)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(89, 59)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._button2.Location = System.Drawing.Point(28, 99)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(89, 59)
        self._button2.TabIndex = 2
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._button3.Location = System.Drawing.Point(28, 178)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(89, 59)
        self._button3.TabIndex = 3
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = False
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label5.Font = System.Drawing.Font("Microsoft Tai Le", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(14, 10)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(60, 23)
        self._label5.TabIndex = 7
        self._label5.Text = "Cost:"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label6.Font = System.Drawing.Font("Microsoft Tai Le", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(91, 13)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(189, 23)
        self._label6.TabIndex = 7
        self._label6.Text = "Package A:"
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label7.Font = System.Drawing.Font("Microsoft Tai Le", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(91, 49)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(189, 23)
        self._label7.TabIndex = 8
        self._label7.Text = "Package B"
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label8.Font = System.Drawing.Font("Microsoft Tai Le", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(91, 85)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(189, 23)
        self._label8.TabIndex = 9
        self._label8.Text = "Package C:"
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label9.Font = System.Drawing.Font("Microsoft Tai Le", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(91, 121)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(189, 23)
        self._label9.TabIndex = 10
        self._label9.Text = "Total :"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(64, 0, 64)
        self.ClientSize = System.Drawing.Size(531, 440)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._panel2)
        self.Controls.Add(self._panel1)
        self.Name = "MainForm"
        self.Text = "Prog269SoftwareSales"
        self._panel1.ResumeLayout(False)
        self._panel1.PerformLayout()
        self._panel2.ResumeLayout(False)
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        packa = int(self._textBox1.Text)
        packb = int(self._textBox2.Text)
        packc = int(self._textBox3.Text)
        pricea = 99 * packa
        priceb = 199 * packb
        pricec = 299 * packc
        if packa < 10:
            pricea = pricea 
        elif packa >= 10 and packa <= 19:
            pricea = pricea * 0.8
        elif packa >= 20 and packa <= 49:
            pricea = pricea * 0.7
        elif packa >= 50 and packa <= 99:
            pricea = pricea * 0.6
        elif packa >= 100:
            pricea = pricea * 0.5
         
        if packb < 10:
            priceb = priceb 
        elif packb >= 10 and packb <= 19:
            priceb = priceb * 0.8
        elif packa >= 20 and packb <= 49:
            priceb = priceb * 0.7
        elif packb >= 50 and packb <= 99:
            priceb = priceb * 0.6
        elif packb >= 100:
            priceb = priceb * 0.5
        
        if packc < 10:
            pricec = pricec 
        elif packc >= 10 and packc <= 19:
            pricec = pricec * 0.8
        elif packc >= 20 and packc <= 49:
            pricec = pricec * 0.7
        elif packc >= 50 and packc <= 99:
            pricec = pricec * 0.6
        elif packc >= 100:
            pricec = pricec * 0.5
          
        self._label6.Text = "Package A: $ " + str(pricea)
        self._label7.Text = "Package B: $ " + str(priceb)
        self._label8.Text = "Package C: $" +  str(pricec)
        self._label9.Text = "Total: $" + str(pricea+priceb+pricec)
        