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
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._button5 = System.Windows.Forms.Button()
        self._button6 = System.Windows.Forms.Button()
        self._button7 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._button8 = System.Windows.Forms.Button()
        self._button9 = System.Windows.Forms.Button()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(42, 50)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(309, 34)
        self._textBox1.TabIndex = 0
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(42, 253)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(309, 34)
        self._textBox2.TabIndex = 1
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label1.Location = System.Drawing.Point(42, 146)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(308, 38)
        self._label1.TabIndex = 2
        self._label1.Text = "Operation"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(486, 91)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(75, 60)
        self._button1.TabIndex = 3
        self._button1.Text = "+"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(486, 187)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(75, 60)
        self._button2.TabIndex = 4
        self._button2.Text = "^"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(600, 187)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(75, 60)
        self._button3.TabIndex = 6
        self._button3.Text = "/"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.Location = System.Drawing.Point(600, 91)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(75, 60)
        self._button4.TabIndex = 5
        self._button4.Text = "-"
        self._button4.UseVisualStyleBackColor = True
        self._button4.Click += self.Button4Click
        # 
        # button5
        # 
        self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button5.Location = System.Drawing.Point(715, 187)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(75, 60)
        self._button5.TabIndex = 8
        self._button5.Text = "//"
        self._button5.UseVisualStyleBackColor = True
        self._button5.Click += self.Button5Click
        # 
        # button6
        # 
        self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button6.Location = System.Drawing.Point(715, 91)
        self._button6.Name = "button6"
        self._button6.Size = System.Drawing.Size(75, 60)
        self._button6.TabIndex = 7
        self._button6.Text = "X"
        self._button6.UseVisualStyleBackColor = True
        self._button6.Click += self.Button6Click
        # 
        # button7
        # 
        self._button7.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button7.Location = System.Drawing.Point(577, 281)
        self._button7.Name = "button7"
        self._button7.Size = System.Drawing.Size(125, 60)
        self._button7.TabIndex = 9
        self._button7.Text = "Mod"
        self._button7.UseVisualStyleBackColor = True
        self._button7.Click += self.Button7Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label2.Location = System.Drawing.Point(150, 9)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(78, 38)
        self._label2.TabIndex = 10
        self._label2.Text = "Number 1 "
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label3.Location = System.Drawing.Point(161, 290)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(78, 38)
        self._label3.TabIndex = 11
        self._label3.Text = "Number 2"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button8
        # 
        self._button8.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button8.Location = System.Drawing.Point(486, 396)
        self._button8.Name = "button8"
        self._button8.Size = System.Drawing.Size(304, 60)
        self._button8.TabIndex = 12
        self._button8.Text = "Clear"
        self._button8.UseVisualStyleBackColor = True
        self._button8.Click += self.Button8Click
        # 
        # button9
        # 
        self._button9.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._button9.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button9.Location = System.Drawing.Point(486, 494)
        self._button9.Name = "button9"
        self._button9.Size = System.Drawing.Size(304, 60)
        self._button9.TabIndex = 13
        self._button9.Text = "Exit"
        self._button9.UseVisualStyleBackColor = False
        self._button9.Click += self.Button9Click
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(43, 430)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(308, 81)
        self._label4.TabIndex = 14
        self._label4.Text = "Output :"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self.ClientSize = System.Drawing.Size(871, 624)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._button9)
        self.Controls.Add(self._button8)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button7)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button6)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Prog140"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    def MainFormLoad(self, sender, e):
        pass

    def Button1Click(self, sender, e): #Add
         num1 = float(self._textBox1.Text)
         num2 = float(self._textBox2.Text)
         total = num1 + num2
         self._label4.Text = "Output : " + str(total)

    def Button4Click(self, sender, e): #Minus
         num1 = float(self._textBox1.Text)
         num2 = float(self._textBox2.Text)
         total = num1 - num2
         self._label4.Text = "Output : " + str(total)

    def Button6Click(self, sender, e): #Multiply
         num1 = float(self._textBox1.Text)
         num2 = float(self._textBox2.Text)
         total = num1 * num2
         self._label4.Text = "Output : " + str(total)


    def Button2Click(self, sender, e): #To The Power Of
         num1 = float(self._textBox1.Text)
         num2 = float(self._textBox2.Text)
         total = num1**num2
         self._label4.Text = "Output : " + str(total)


    def Button3Click(self, sender, e): #Divide
         num1 = float(self._textBox1.Text)
         num2 = float(self._textBox2.Text)
         total = num1/num2
         self._label4.Text = "Output : " + str(total)

    def Button5Click(self, sender, e): #Floor Divide
         num1 = float(self._textBox1.Text)
         num2 = float(self._textBox2.Text)
         total = num1//num2
         self._label4.Text = "Output : " + str(total)

    def Button7Click(self, sender, e): #Module
         num1 = float(self._textBox1.Text)
         num2 = float(self._textBox2.Text)
         total = num1%num2
         self._label4.Text = "Output : " + str(total)

    def Button8Click(self, sender, e): #Clear
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label4.Text = "Output : "

    def Button9Click(self, sender, e): #Exit
        Application.Exit()
        
        
        