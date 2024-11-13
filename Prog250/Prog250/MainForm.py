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
        self._panel3 = System.Windows.Forms.Panel()
        self._panel4 = System.Windows.Forms.Panel()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._radioButton4 = System.Windows.Forms.RadioButton()
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._checkBox3 = System.Windows.Forms.CheckBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._panel1.SuspendLayout()
        self._panel2.SuspendLayout()
        self._panel3.SuspendLayout()
        self._panel4.SuspendLayout()
        self.SuspendLayout()
        # 
        # panel1
        # 
        self._panel1.BackColor = System.Drawing.Color.Olive
        self._panel1.Controls.Add(self._label1)
        self._panel1.Controls.Add(self._radioButton4)
        self._panel1.Controls.Add(self._radioButton3)
        self._panel1.Controls.Add(self._radioButton2)
        self._panel1.Controls.Add(self._radioButton1)
        self._panel1.Location = System.Drawing.Point(26, 24)
        self._panel1.Name = "panel1"
        self._panel1.Size = System.Drawing.Size(359, 219)
        self._panel1.TabIndex = 0
        # 
        # panel2
        # 
        self._panel2.BackColor = System.Drawing.Color.Olive
        self._panel2.Controls.Add(self._label2)
        self._panel2.Controls.Add(self._checkBox3)
        self._panel2.Controls.Add(self._checkBox2)
        self._panel2.Controls.Add(self._checkBox1)
        self._panel2.Location = System.Drawing.Point(427, 24)
        self._panel2.Name = "panel2"
        self._panel2.Size = System.Drawing.Size(359, 219)
        self._panel2.TabIndex = 1
        # 
        # panel3
        # 
        self._panel3.BackColor = System.Drawing.Color.Olive
        self._panel3.Controls.Add(self._textBox1)
        self._panel3.Controls.Add(self._label5)
        self._panel3.Controls.Add(self._label4)
        self._panel3.Location = System.Drawing.Point(26, 275)
        self._panel3.Name = "panel3"
        self._panel3.Size = System.Drawing.Size(359, 219)
        self._panel3.TabIndex = 2
        # 
        # panel4
        # 
        self._panel4.BackColor = System.Drawing.Color.Olive
        self._panel4.Controls.Add(self._label7)
        self._panel4.Controls.Add(self._label6)
        self._panel4.Controls.Add(self._label3)
        self._panel4.Location = System.Drawing.Point(427, 275)
        self._panel4.Name = "panel4"
        self._panel4.Size = System.Drawing.Size(359, 219)
        self._panel4.TabIndex = 3
        # 
        # radioButton1
        # 
        self._radioButton1.FlatAppearance.BorderColor = System.Drawing.Color.DimGray
        self._radioButton1.FlatAppearance.BorderSize = 12
        self._radioButton1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(29, 21)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(258, 24)
        self._radioButton1.TabIndex = 0
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Standard Adult"
        self._radioButton1.UseVisualStyleBackColor = True
        # 
        # radioButton2
        # 
        self._radioButton2.FlatAppearance.BorderColor = System.Drawing.Color.DimGray
        self._radioButton2.FlatAppearance.BorderSize = 12
        self._radioButton2.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(29, 70)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(258, 24)
        self._radioButton2.TabIndex = 1
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Child (12 Or Younger)"
        self._radioButton2.UseVisualStyleBackColor = True
        # 
        # radioButton3
        # 
        self._radioButton3.FlatAppearance.BorderColor = System.Drawing.Color.DimGray
        self._radioButton3.FlatAppearance.BorderSize = 12
        self._radioButton3.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(29, 119)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(258, 24)
        self._radioButton3.TabIndex = 2
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Student"
        self._radioButton3.UseVisualStyleBackColor = True
        # 
        # radioButton4
        # 
        self._radioButton4.FlatAppearance.BorderColor = System.Drawing.Color.DimGray
        self._radioButton4.FlatAppearance.BorderSize = 12
        self._radioButton4.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._radioButton4.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton4.Location = System.Drawing.Point(29, 165)
        self._radioButton4.Name = "radioButton4"
        self._radioButton4.Size = System.Drawing.Size(258, 24)
        self._radioButton4.TabIndex = 3
        self._radioButton4.TabStop = True
        self._radioButton4.Text = "Senior Citizen"
        self._radioButton4.UseVisualStyleBackColor = True
        # 
        # checkBox1
        # 
        self._checkBox1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._checkBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox1.Location = System.Drawing.Point(30, 21)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Size = System.Drawing.Size(287, 36)
        self._checkBox1.TabIndex = 0
        self._checkBox1.Text = "Yoga "
        self._checkBox1.UseVisualStyleBackColor = True
        # 
        # checkBox2
        # 
        self._checkBox2.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._checkBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox2.Location = System.Drawing.Point(30, 87)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(287, 36)
        self._checkBox2.TabIndex = 1
        self._checkBox2.Text = "Karate"
        self._checkBox2.UseVisualStyleBackColor = True
        # 
        # checkBox3
        # 
        self._checkBox3.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._checkBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox3.Location = System.Drawing.Point(30, 144)
        self._checkBox3.Name = "checkBox3"
        self._checkBox3.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._checkBox3.Size = System.Drawing.Size(287, 36)
        self._checkBox3.TabIndex = 2
        self._checkBox3.Text = "Personal Trainer"
        self._checkBox3.UseVisualStyleBackColor = True
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label1.Location = System.Drawing.Point(227, 11)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(117, 46)
        self._label1.TabIndex = 4
        self._label1.Text = "Select Membership"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label2.Location = System.Drawing.Point(224, 11)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(117, 34)
        self._label2.TabIndex = 5
        self._label2.Text = "Options"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label3.Location = System.Drawing.Point(103, 0)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(185, 35)
        self._label3.TabIndex = 6
        self._label3.Text = "Membership Fees"
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label4.Location = System.Drawing.Point(86, 0)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(172, 36)
        self._label4.TabIndex = 7
        self._label4.Text = "Membership Length"
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label5.Location = System.Drawing.Point(86, 72)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(159, 33)
        self._label5.TabIndex = 8
        self._label5.Text = "Enter # Of Months"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Tai Le", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(64, 108)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(216, 29)
        self._textBox1.TabIndex = 9
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label6.Location = System.Drawing.Point(30, 69)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(258, 36)
        self._label6.TabIndex = 10
        self._label6.Text = "Monthly Fee :"
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label7.Location = System.Drawing.Point(30, 108)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(258, 36)
        self._label7.TabIndex = 11
        self._label7.Text = "Total :"
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(26, 531)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(235, 80)
        self._button1.TabIndex = 4
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(293, 531)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(235, 80)
        self._button2.TabIndex = 5
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(551, 531)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(235, 80)
        self._button3.TabIndex = 6
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Black
        self.ClientSize = System.Drawing.Size(827, 623)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._panel4)
        self.Controls.Add(self._panel3)
        self.Controls.Add(self._panel2)
        self.Controls.Add(self._panel1)
        self.Name = "MainForm"
        self.Text = "Prog250"
        self._panel1.ResumeLayout(False)
        self._panel2.ResumeLayout(False)
        self._panel3.ResumeLayout(False)
        self._panel3.PerformLayout()
        self._panel4.ResumeLayout(False)
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        mfee = 0
        m = int(self._textBox1.Text)
        if self._radioButton1.Checked:
            mfee = 40.0
        elif self._radioButton2.Checked:
            mfee = 20.0
        elif self._radioButton3.Checked:
            mfee = 25.0
        else:
            mfee = 30.0
        if self._checkBox1.Checked:
            mfee += 10.0
        if self._checkBox1.Checked:
            mfee +=30.0
        if self._checkBox1.Checked:
            mfee +=50.0
        self._label6.Text = "Monthly Fee:   $" + str(mfee)
        
        