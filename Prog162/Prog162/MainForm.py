import time
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
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._textBox5 = System.Windows.Forms.TextBox()
        self._dateTimePicker1 = System.Windows.Forms.DateTimePicker()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self._label15 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(67, 41)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(153, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "Today's Date :"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(362, 41)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(281, 23)
        self._label2.TabIndex = 1
        self._label2.Text = "Time :"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(67, 217)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(153, 23)
        self._label3.TabIndex = 2
        self._label3.Text = "Room Information"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(362, 217)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(153, 23)
        self._label4.TabIndex = 3
        self._label4.Text = "Additional Charges"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(67, 425)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(153, 23)
        self._label5.TabIndex = 4
        self._label5.Text = "Total Charges"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(678, 283)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(99, 91)
        self._button1.TabIndex = 5
        self._button1.Text = "Calculate Charges"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 17, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(678, 485)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(99, 91)
        self._button2.TabIndex = 6
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 17, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(678, 388)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(99, 91)
        self._button3.TabIndex = 7
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(105, 283)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(96, 23)
        self._label6.TabIndex = 8
        self._label6.Text = "Nights"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(105, 351)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(96, 23)
        self._label7.TabIndex = 9
        self._label7.Text = "$/Night"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(395, 283)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(96, 23)
        self._label8.TabIndex = 10
        self._label8.Text = "Room Service :"
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(395, 351)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(96, 23)
        self._label10.TabIndex = 12
        self._label10.Text = "Misc :"
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(523, 286)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 20)
        self._textBox1.TabIndex = 13
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(523, 320)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 20)
        self._textBox2.TabIndex = 14
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(523, 354)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(100, 20)
        self._textBox3.TabIndex = 15
        # 
        # textBox4
        # 
        self._textBox4.Location = System.Drawing.Point(236, 286)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(100, 20)
        self._textBox4.TabIndex = 16
        # 
        # textBox5
        # 
        self._textBox5.Location = System.Drawing.Point(236, 351)
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(100, 20)
        self._textBox5.TabIndex = 17
        # 
        # dateTimePicker1
        # 
        self._dateTimePicker1.Location = System.Drawing.Point(47, 77)
        self._dateTimePicker1.Name = "dateTimePicker1"
        self._dateTimePicker1.Size = System.Drawing.Size(200, 20)
        self._dateTimePicker1.TabIndex = 18
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(67, 485)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(269, 23)
        self._label11.TabIndex = 19
        self._label11.Text = "Nightly Charge :"
        self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(67, 520)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(269, 23)
        self._label12.TabIndex = 20
        self._label12.Text = "Additional Charges:"
        self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.Location = System.Drawing.Point(67, 553)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(269, 23)
        self._label13.TabIndex = 21
        self._label13.Text = "Subtotal :"
        self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label14
        # 
        self._label14.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label14.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label14.Location = System.Drawing.Point(384, 494)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(269, 23)
        self._label14.TabIndex = 22
        self._label14.Text = "Tax :"
        self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label15
        # 
        self._label15.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label15.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label15.Location = System.Drawing.Point(384, 522)
        self._label15.Name = "label15"
        self._label15.Size = System.Drawing.Size(269, 23)
        self._label15.TabIndex = 23
        self._label15.Text = "Total Amount Due :"
        self._label15.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(395, 317)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(96, 23)
        self._label9.TabIndex = 11
        self._label9.Text = "Telephone :"
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self.ClientSize = System.Drawing.Size(818, 617)
        self.Controls.Add(self._label15)
        self.Controls.Add(self._label14)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._dateTimePicker1)
        self.Controls.Add(self._textBox5)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog162"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()
        
        


    def MainFormLoad(self, sender, e):
            self._label2.Text = time.strftime("Time : %I: %M: %S: %p")
        

    def Button3Click(self, sender, e): #Exit
        Applicaton.Exit() 
        
        

    def Button1Click(self, sender, e): #Calc
        nights = float(self._textBox4.Text) 
        ncharge = float(self._textBox5.Text)
        service = float(self._textBox1.Text)
        telephone = float(self._textBox2.Text)
        misc = float(self._textBox3.Text)
        
        tncharge = float(nights*ncharge)
        additional = float(service+telephone+misc)
        subtotal = float(tncharge + additional)
        tax = float(subtotal*0.08)
        total = float(subtotal + tax)
        
        self._label11.Text = "Nightly Charge : " + str(tncharge)
        self._label12.Text = "Additional Charges : " + str(additional)
        self._label13.Text = "Subtotal : " + str(subtotal)
        self._label14.Text = "Tax : " + str(tax)
        self._label15.Text = "Total Amount Due : " + str(total)