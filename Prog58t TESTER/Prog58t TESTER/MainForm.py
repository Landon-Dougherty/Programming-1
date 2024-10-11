import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label3 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 186)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(561, 50)
        self._button1.TabIndex = 2
        self._button1.Text = "Calculate Change"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(24, 21)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(246, 38)
        self._textBox1.TabIndex = 3
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(24, 71)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(246, 45)
        self._label2.TabIndex = 5
        self._label2.Text = "Total Due"
        self._label2.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(47, 135)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(204, 45)
        self._button2.TabIndex = 6
        self._button2.Text = "Clear Data"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(350, 135)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(204, 45)
        self._button3.TabIndex = 7
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(327, 71)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(246, 45)
        self._label3.TabIndex = 8
        self._label3.Text = "Total Paid"
        self._label3.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(327, 21)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(246, 38)
        self._textBox2.TabIndex = 9
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 248)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(293, 32)
        self._label1.TabIndex = 10
        self._label1.Text = "Total : "
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(314, 248)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(259, 32)
        self._label4.TabIndex = 11
        self._label4.Text = "Paid : "
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(163, 290)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(293, 28)
        self._label5.TabIndex = 12
        self._label5.Text = "Change :"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(12, 359)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(293, 32)
        self._label6.TabIndex = 13
        self._label6.Text = "Quarters Due :"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(311, 405)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(262, 32)
        self._label7.TabIndex = 14
        self._label7.Text = "Pennies Due :"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(12, 405)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(293, 32)
        self._label8.TabIndex = 15
        self._label8.Text = "Nickels Due :"
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(311, 359)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(262, 32)
        self._label9.TabIndex = 16
        self._label9.Text = "Dimes Due:"
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(199, 322)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(218, 32)
        self._label10.TabIndex = 17
        self._label10.Text = "Dollars Due :"
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Black
        self.ClientSize = System.Drawing.Size(602, 458)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog58t"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()

    def Button1Click(self, sender, e):
        Total  = float(self._textBox1.Text)
        Paid   = float(self._textBox2.Text)
        Change = float(Paid - Total)
        self._label5.Text = "Change : " + str(Change)
        DollarsDue = int(Change / 1)
        Change = Change - DollarsDue
        QuartersDue = int(Change / 0.25)
        self._label6.Text = "Quarters Due: " + str(QuartersDue)
        Change = Change - (QuartersDue * 0.25)
        DimesDue = int(Change / 0.10)
        self._label9.Text = "Dimes Due: " + str(DimesDue)
        Change = Change - (DimesDue * 0.10)
        NickelsDue = int(Change / 0.05)
        self._label8.Text = "Nickels Due: " + str(NickelsDue)
        Change = Change - (NickelsDue * 0.05)
        PenniesDue = Change / 0.01
        self._label7.Text = "Pennies Due: " + str(round(PenniesDue,0))




        
        self._label1.Text = "Total : " + str(Total)
        self._label4.Text = "Paid : " + str(Paid)
        self._label10.Text = "Dollars Due :" + str(DollarsDue)

        
 
    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label1.Text   = "Total : " 
        self._label4.Text = "Paid : " 
        self._label5.Text = "Change : " 
        self._label10.Text = "Dollars Due : "
        self._label6.Text = "Quarters Due : " 
        self._label9.Text = "Dimes Due : "
        self._label8.Text = "Nickels Due : " 
        self._label7.Text = "Pennies Due : "

    def MainFormLoad(self, sender, e):
        pass