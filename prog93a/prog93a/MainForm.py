import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label6 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(270, 86)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(197, 45)
        self._textBox1.TabIndex = 0
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(192, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(357, 45)
        self._label1.TabIndex = 1
        self._label1.Text = "Enter KW/H Used"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(108, 159)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(522, 45)
        self._label2.TabIndex = 2
        self._label2.Text = "Base Charge (Kw/H * 0.475):"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(108, 219)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(522, 45)
        self._label3.TabIndex = 3
        self._label3.Text = "Surcharge (10%) :"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(108, 281)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(522, 45)
        self._label4.TabIndex = 4
        self._label4.Text = "City Tax (3%)"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(108, 341)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(522, 45)
        self._label5.TabIndex = 5
        self._label5.Text = "Your Total :"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(40, 68)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(142, 35)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(40, 109)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(142, 35)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(192, 0, 0)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(563, 68)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(142, 76)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(108, 404)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(522, 45)
        self._label6.TabIndex = 9
        self._label6.Text = "Total After May 20th : "
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(64, 0, 64)
        self.ClientSize = System.Drawing.Size(752, 458)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "prog93a"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    def MainFormLoad(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        kwh = float(self._textBox1.Text) 
        price = kwh * 0.0475
        self._label2.Text = "Base Charge (Kw/H * 0.475):" + str(round(price,2))
        newprice = price * 0.1
        self._label3.Text = "Surcharge (10%) :" + str(round(newprice,2))
        newerprice = price * 0.03
        self._label4.Text = "City Tax (3%) : " + str(round(newerprice,2))
        total = price + newprice + newerprice 
        self._label5.Text = "Your Total : " + str(round(total,2))
        totalaftermay = total * 1.04
        self._label6.Text = "Total After May 20th : " + str(round(totalaftermay,2))

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._label2.Text = "Base Charge (Kw/H * 0.475) : "
        self._label3.Text = "Surcharge (10%) : "
        self._label4.Text = "City Tax (3%) : "
        self._label5.Text = "Your Total : "
        self._label6.Text = "Total After May 20th : " 

    def Button3Click(self, sender, e):
        Application.Exit()